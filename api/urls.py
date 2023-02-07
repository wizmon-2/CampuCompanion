from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('check/', views.VerifyTokenView.as_view(), name='check'),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]