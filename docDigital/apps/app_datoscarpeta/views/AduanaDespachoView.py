from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from ..models.ModeloAduanaDespacho import ModeloAduanaDespacho
from ..forms.AduanaDespachoForm import RegistroAduanaDespachoForm

@login_required
def lista_aduana_despacho(request):
    aduana_despacho = ModeloAduanaDespacho.objects.all()[:5]

    if request.method == 'POST':
        aduana_despacho_form = RegistroAduanaDespachoForm(request.POST)
        if aduana_despacho_form.is_valid():
            aduana_despacho_form.save()
            return redirect('recintos_aduaneros')
    else:
        aduana_despacho_form = RegistroAduanaDespachoForm()
    return render(
        request, 'aduana_despacho/recintos.html',
        {
            'aduana_despacho': aduana_despacho,
            'aduana_despacho_form':aduana_despacho_form
        }
    )

@login_required
def editar_aduana_despacho(request, pk):
    recinto = get_object_or_404(ModeloAduanaDespacho, pk=pk)
    if request.method == 'POST':
        editar_recinto_form = RegistroAduanaDespachoForm(
            request.POST, instance=recinto
        )
        if editar_recinto_form.is_valid():
            editar_recinto_form.save()
            return redirect('recintos_aduaneros')
    else:
        editar_recinto_form = RegistroAduanaDespachoForm(instance=recinto)
    return render(
        request, 'aduana_despacho/editar_recinto.html',
        {
            'editar_recinto_form':editar_recinto_form,
            'recinto':recinto
        }
    )

def elimiar_aduana_despacho(request, pk):
    recinto = get_object_or_404(ModeloAduanaDespacho, pk=pk)
    recinto.delete()
    return redirect('recintos_aduaneros')
        