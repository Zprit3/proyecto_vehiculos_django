from django.shortcuts import render, redirect
from .forms import VehiculoForm, RegistroUsuarioForm
from .models import Vehiculo
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    return render(request, 'vehiculo/index.html')

def agregar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/agregar_vehiculo.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            content_type = ContentType.objects.get_for_model(Vehiculo)
            permission_view = Permission.objects.get(codename='view_vehiculo', content_type=content_type)
            user.user_permissions.add(permission_view)

            if user.is_staff: #Si el usuario es staff, le asigna el permiso de add_vehiculo
                permission_add = Permission.objects.get(codename='add_vehiculo', content_type=content_type)
                user.user_permissions.add(permission_add)
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
@permission_required('vehiculo.view_vehiculo', raise_exception=True)
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    context = {'vehiculos': vehiculos}
    return render(request, 'vehiculo/listar_vehiculos.html', context)

@login_required #Esto es un extra
def profile(request):
    return render(request, 'vehiculo/profile.html')