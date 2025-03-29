from django.urls import path
from .views import register, user_login, home, user_logout, after_login, generate_qr_code

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('home/', home, name='home'),
    path('logout/', user_logout, name='logout'),
    path('after_login/', after_login, name='after_login'),
    path("generate_qr/", generate_qr_code, name="generate_qr_code"),
]

