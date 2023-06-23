from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from . forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='idnex'),
    path('contact/',views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('privacy/',views.privacy, name='privacy'),
    path('logout', auth_views.LogoutView.as_view(template_name='core/index.html'), name='logout'),
]

