from django.contrib.auth.models import AbstractUser
from django.db import models

# ----------------------User-Table----------------------
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # You can add extra fields here if needed


# ----------------------QR-Table----------------------
from django.conf import settings  # Import settings to access custom user model

class QRCodeEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use custom user model
    title = models.CharField(max_length=255)
    description = models.TextField()
    qr_type = models.CharField(max_length=50)  # url, image, video, pdf
    content = models.TextField()  # Stores URL or file path
    qr_image = models.ImageField(upload_to="qr_codes/")  # Stores QR code image
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"{self.title} ({self.qr_type})"
