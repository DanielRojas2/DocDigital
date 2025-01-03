from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.ModeloImportador import ModeloImportador
from ..forms.ImportadorForm import ImportadorForm

@login_required
def listar_importador(request):
    lista_importadores = ModeloImportador.objects.all()

    paginator = Paginator(lista_importadores, 5)
    page_number = request.GET.get('page',1)
    
    if request.method == 'POST':
        importador_form = ImportadorForm(request.POST)
        if importador_form.is_valid():
            importador_form.save()
            return redirect("importadores")
    else:
        importador_form = ImportadorForm()
    
    try:
        importadores = paginator.page(page_number)
    except PageNotAnInteger:
        importadores = paginator.page(1)
    except EmptyPage:
        importadores = paginator.page(paginator.num_pages)
    
    return render(
        request, 'importador/importadores.html',
        {
            'importadores': importadores,
            'importador_form': importador_form
        }
    )

@login_required
def editar_importador(request, pk):
    importador = get_object_or_404(ModeloImportador, pk=pk)
    
    if request.method == 'POST':
        editar_importador_form = ImportadorForm(
            request.POST, instance=importador
        )
        if editar_importador_form.is_valid():
            editar_importador_form.save()
            return redirect("importadores")
    else:
        editar_importador_form = ImportadorForm(instance=importador)
    
    return render(
        request, 'importador/editar_importador.html',
        {
            'editar_importador_form': editar_importador_form
        }
    )

@login_required
def eliminar_importador(request, pk):
    importador = get_object_or_404(ModeloImportador, pk=pk)
    importador.delete()
    return redirect("importadores")
