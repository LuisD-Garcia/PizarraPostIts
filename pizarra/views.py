from django.shortcuts import render, redirect, get_object_or_404

from .models import PostIt



# Página principal
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
def completar(request,id):

    tarea=get_object_or_404(
        PostIt,
        id=id
    )

    tarea.completada=True
    tarea.save()


    return redirect("pizarra")



# Eliminar
def eliminar(request,id):

    tarea=get_object_or_404(
        PostIt,
        id=id
    )

    tarea.delete()


    return redirect("pizarra")