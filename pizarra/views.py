from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from .models import PostIt



# Login
def login_view(request):

    if request.user.is_authenticated:
        return redirect("pizarra")


    if request.method == "POST":

        usuario = request.POST["usuario"]
        clave = request.POST["clave"]

        user = authenticate(
            request,
            username=usuario,
            password=clave
        )

        if user is not None:

            login(request, user)
            return redirect("pizarra")

        else:

            messages.error(request, "Usuario o contraseña incorrectos")


    return render(
        request,
        "pizarra/login.html"
    )



# Logout
def logout_view(request):

    logout(request)
    messages.success(request, "Sesión cerrada correctamente")

    return redirect("login")



# Perfil
@login_required(login_url="login")
def perfil(request):

    usuario = request.user

    if request.method == "POST":

        accion = request.POST.get("accion")


        if accion == "datos":

            usuario.first_name = request.POST.get("nombre", "").strip()
            usuario.last_name = request.POST.get("apellido", "").strip()
            usuario.email = request.POST.get("email", "").strip()

            usuario.save()

            messages.success(request, "Tus datos se actualizaron correctamente")

            return redirect("perfil")


        elif accion == "clave":

            formulario_clave = PasswordChangeForm(usuario, request.POST)

            if formulario_clave.is_valid():

                usuario_actualizado = formulario_clave.save()

                update_session_auth_hash(request, usuario_actualizado)

                messages.success(request, "Tu contraseña se actualizó correctamente")

                return redirect("perfil")

            else:

                for error in formulario_clave.errors.values():
                    messages.error(request, error.as_text())

                return redirect("perfil")


    tareas_totales = PostIt.objects.count()
    tareas_pendientes = PostIt.objects.filter(completada=False).count()
    tareas_completadas = PostIt.objects.filter(completada=True).count()

    return render(
        request,
        "pizarra/perfil.html",
        {
            "tareas_totales": tareas_totales,
            "tareas_pendientes": tareas_pendientes,
            "tareas_completadas": tareas_completadas,
        }
    )



# Página principal
@login_required(login_url="login")
def pizarra(request):

    tareas = PostIt.objects.filter(
        completada=False
    )

    return render(
        request,
        "pizarra/pizarra.html",
        {
            "tareas": tareas
        }
    )



# Lista completados
@login_required(login_url="login")
def completados(request):

    tareas = PostIt.objects.filter(
        completada=True
    )

    return render(
        request,
        "pizarra/completados.html",
        {
            "tareas": tareas
        }
    )



# Crear post-it
@login_required(login_url="login")
def crear(request):

    if request.method == "POST":

        titulo = request.POST["titulo"]
        detalle = request.POST["detalle"]


        PostIt.objects.create(
            titulo=titulo,
            detalle=detalle
        )


        return redirect("pizarra")


    return render(
        request,
        "pizarra/editar.html"
    )



# Detalle
@login_required(login_url="login")
def detalle(request,id):

    tarea = get_object_or_404(
        PostIt,
        id=id
    )


    return render(
        request,
        "pizarra/detalle.html",
        {
            "tarea": tarea
        }
    )



# Editar
@login_required(login_url="login")
def editar(request,id):

    tarea = get_object_or_404(
        PostIt,
        id=id
    )


    if request.method=="POST":

        tarea.titulo=request.POST["titulo"]
        tarea.detalle=request.POST["detalle"]

        tarea.save()


        return redirect("pizarra")


    return render(
        request,
        "pizarra/editar.html",
        {
            "tarea": tarea
        }
    )



# Completar
@login_required(login_url="login")
def completar(request,id):

    tarea=get_object_or_404(
        PostIt,
        id=id
    )

    tarea.completada=True
    tarea.save()


    return redirect("pizarra")



# Eliminar
@login_required(login_url="login")
def eliminar(request,id):

    tarea=get_object_or_404(
        PostIt,
        id=id
    )

    tarea.delete()


    return redirect("pizarra")