from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.ModeloMercaderia import ModeloMercaderia
from ..forms.MercaderiaForm import MercaderiaForm

@login_required
def mercaderia(request):
    lista_mercaderia = ModeloMercaderia.objects.all()

    paginator = Paginator(lista_mercaderia, 5)
    page_number = request.GET.get('page', 1)

    if request.method == 'POST':
        mercaderia_form = MercaderiaForm(request.POST)
        if mercaderia_form.is_valid():
            mercaderia_form.save()
            return redirect('mercaderia')
    else:
        mercaderia_form = MercaderiaForm()

    try:
        mercaderias = paginator.page(page_number)
    except EmptyPage:
        mercaderias = paginator.page(1)
    except PageNotAnInteger:
        mercaderias = paginator.page(paginator.num_pages)
    
    return render(
        request, 'mercaderia/mercaderia.html',
        {
            'mercaderias': mercaderias,
            'mercaderia_form': mercaderia_form
        }
    )

@login_required
def editar_mercaderia(request, pk):
    mercaderia = get_object_or_404(
        ModeloMercaderia,
        pk = pk
    )

    if request.method == 'POST':
        editar_mercaderia_form = MercaderiaForm(
            request.POST, instance=mercaderia
        )
        if editar_mercaderia_form.is_valid():
            editar_mercaderia_form.save()
            return redirect('mercaderia')
    else:
        editar_mercaderia_form = MercaderiaForm(instance=mercaderia)
    
    return render(
        request, 'mercaderia/editar_mercaderia.html',
        {
            'editar_mercaderia_form':editar_mercaderia_form
        }
    )

@login_required
def eliminar_mercaderia(request, pk):
    mercaderia = get_object_or_404(ModeloMercaderia, pk=pk)
    mercaderia.delete()
    return redirect('mercaderia')
