from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.ModeloPersonalAgencia import ModeloPersonalAgencia
from ..forms.PersonalAgenciaForm import PersonalAgenciaForm

@login_required
def personal_agencia(request):
    lista_personal = ModeloPersonalAgencia.objects.all()

    paginator = Paginator(lista_personal, 5)
    page_number = request.GET.get('page', 1)

    if request.method == 'POST':
        personal_agencia_form = PersonalAgenciaForm(request.POST)
        if personal_agencia_form.is_valid():
            personal_agencia_form.save()
            return redirect('personal_agencia')
    else:
        personal_agencia_form = PersonalAgenciaForm()
    
    try:
        personal = paginator.page(page_number)
    except EmptyPage:
        personal = paginator.page(1)
    except PageNotAnInteger:
        personal = paginator.page(paginator.num_pages)
    
    return render(
        request, 'personal/personal.html',
        {
            'personal': personal,
            'personal_agencia_form': personal_agencia_form
        }
    )

@login_required
def editar_personal_agencia(request, pk):
    personal = get_object_or_404(ModeloPersonalAgencia, pk=pk)
    
    if request.method == 'POST':
        editar_personal_agencia_form = PersonalAgenciaForm(
            request.POST, instance=personal
        )
        if editar_personal_agencia_form.is_valid():
            editar_personal_agencia_form.save()
            return redirect('personal_agencia')
    else:
        editar_personal_agencia_form = PersonalAgenciaForm(instance=personal)
    
    return render(
        request, 'personal/editar_personal.html',
        {
            'editar_personal_agencia_form':editar_personal_agencia_form
        }
    )

@login_required
def eliminar_personal_agencia(request, pk):
    personal = get_object_or_404(ModeloPersonalAgencia, pk=pk)
    personal.delete()
    return redirect('personal_agencia')
