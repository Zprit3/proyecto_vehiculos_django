from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from vehiculo import views as vehiculo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vehiculo.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', vehiculo_views.register, name='register'),
]