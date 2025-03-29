# from django.shortcuts import render
# Create your views here.

from django.shortcuts import render, redirect
from .models import CustomUser  # Import your custom user model
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required

# ----------------------Register----------------------
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            else:
                # user = User.objects.create_user(username=username, email=email, password=password)
                user = CustomUser.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Registration successful! Please log in.")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
    
    return render(request, 'register.html')

# ----------------------Login----------------------
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('after_login')  # Redirect to homepage after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')

def after_login(request):
    return render(request, 'After_Login.html')

def home(request):
    return render(request, 'home.html')

# ----------------------AfterLogin-Password-Change----------------------
@login_required
def after_login(request):
    qr_codes = QRCodeEntry.objects.filter(user=request.user)
    if request.method == "POST" and "change_password" in request.POST:
        new_password = request.POST.get("new_password1")
        confirm_password = request.POST.get("new_password2")

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.", extra_tags="profile")
            # password_changed = True 
        elif request.user.check_password(new_password):
            messages.error(request, "Try a new password.", extra_tags="profile")
            # password_changed = True 
        else:
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Password has been successfully changed!", extra_tags="profile")
            return redirect('after_login')

    return render(request, "after_login.html", {'qr_codes': qr_codes})

# ----------------------Log-Out----------------------
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

# ----------------------QR-Generation----------------------
import qrcode
from django.core.files.base import ContentFile
from .models import QRCodeEntry
from io import BytesIO

@login_required
def generate_qr_code(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        qr_type = request.POST.get("qr_type")
        
        # Handle different content types
        if qr_type == "url":
            content = request.POST.get("content")  # URL input
            file = None
        else:
            file = request.FILES.get("content")  # File upload
            if file:
                content = file.name  # Store file name
            else:
                content = None

        # Validate required fields
        if not title or not description or not content:
            messages.error(request, "All fields are required.", extra_tags="qr")
            return redirect("after_login")

        # Construct the file URL
        if qr_type == "url":
            file_url = content  # Use the URL directly
        else:
            file_url = f"http://192.168.9.197:8000/media-file/{content}"

        print("File URL in QR code:", file_url)  # Debugging

        # Generate QR Code
        qr = qrcode.make(file_url)
        qr_image_io = BytesIO()
        qr.save(qr_image_io, format="PNG")

        # Save to database
        qr_entry = QRCodeEntry(
            user=request.user,
            title=title,
            description=description,
            qr_type=qr_type,
            content=content,  # Store file name or URL
            file=file,  # Save the uploaded file
        )
        qr_entry.qr_image.save(f"{title}.png", ContentFile(qr_image_io.getvalue()), save=True)
        qr_entry.save()

        messages.success(request, "QR Code generated successfully!", extra_tags="qr")
        return redirect("after_login")

    return redirect("after_login")

# ----------------------After-QR-Scanned----------------------
from django.http import FileResponse, Http404
import os
from django.conf import settings

def serve_qr_file(request, file_name):
    """ Serve a file from the media folder when a QR code is scanned """
    file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', file_name)
    print("File path:", file_path)  # Debugging

    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='application/octet-stream')
    else:
        raise Http404("File not found")
