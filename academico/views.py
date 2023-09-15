#from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Curso


# Create your views here.

def home(request):

    #cursosListados = Curso.objects.all()
    cursosListados = Curso.objects.all().order_by('nombre')

    #data = {
    #    'titulo': 'Gestion de Cursos',
    #    'Cursos': cursosListados
    #}
    return render(request, "gestionCursos.html", {"cursos": cursosListados})
    #return render(request, "gestionCursos.html", data)


class CursoListView(ListView):
    model = Curso
    template_name = 'gestionCursos.html'

def registrar_curso(request):
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(nombre=nombre,creditos=creditos)
    return redirect('/')


def eliminar_curso(request,id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect('/')


def edicion_curso(request,id):
    curso = Curso.objects.get(id=id)
    data = {
        'titulo': 'Edicion de Curso',
        'curso': curso
    }

    return render(request, "edicionCurso.html", data)


def editar_curso(request):
    id = int(request.POST['id'])
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(id=id)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    return redirect('/')

def contacto(request):
    return render(request, "contacto.html")