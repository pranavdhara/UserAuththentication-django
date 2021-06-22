from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,PasswordChangeView,LogoutView


urlpatterns = [
    path('',views.index, name='index'),
    path('signup/',views.signup, name='signup'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('update/',PasswordChangeView.as_view(template_name='registration/change_password.html',success_url = '/'), name='change-pass'),
]