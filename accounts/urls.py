from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('accounts/reset_pass/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('accounts/reset_pass_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset_pass_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
