from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import investigacion, categoria_investigacion
from .forms import estilo_investigacion, formato_categoria

# Create your views here.
def index(request):

    investigaciones = investigacion.objects.all()

    context = {
        'titulo': 'Investigaciones',
        'investigaciones': investigaciones
    }

    return render(request, 'investigaciones/index.html', context)

def CC(request):

    investigaciones_filtradas = investigacion.objects.filter(categoria='Ciencias Computacionales')

    context = {
        'titulo': 'Ciencias Computacionales',
        'investigaciones': investigaciones_filtradas
    }

    return render(request, 'investigaciones/index2.html', context)

def CT(request):

    investigaciones_filtradas = investigacion.objects.filter(categoria='Ciencias de la Tierra')

    context = {
        'titulo': 'Ciencias de la Tierra',
        'investigaciones': investigaciones_filtradas
    }

    return render(request, 'investigaciones/index2.html', context)

def CN(request):

    investigaciones_filtradas = investigacion.objects.filter(categoria='Ciencias Naturales')

    context = {
        'titulo': 'Ciencias Naturales',
        'investigaciones': investigaciones_filtradas
    }

    return render(request, 'investigaciones/index2.html', context)

def CS(request):

    investigaciones_filtradas = investigacion.objects.filter(categoria='Ciencias Sociales')

    context = {
        'titulo': 'Ciencias de Sociales',
        'investigaciones': investigaciones_filtradas
    }

    return render(request, 'investigaciones/index2.html', context)

def CM(request):

    investigaciones_filtradas = investigacion.objects.filter(categoria='Ciencias Medicas')

    context = {
        'titulo': 'Ciencias Medicas',
        'investigaciones': investigaciones_filtradas
    }

    return render(request, 'investigaciones/index2.html', context)


def detalles(request, id):
    investigacion = investigacion.objects.get(id=id)
    
    context = {
        'cientifica_investigacion': investigacion
    }

    return render(request, 'investigaciones/detalles.html', context)


def crear(request):
    form = formato_categoria()
    if request.method == "POST":
        form = formato_categoria(request.POST)
        if form.is_valid():
            investigacion.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/cientifica_investigacion/')
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "investigaciones/crear.html", context)
