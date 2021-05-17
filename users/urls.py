from django.contrib.auth import views
from django.urls import path

from users.views import sign_up

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('registration/', sign_up, name="registration"),
]
