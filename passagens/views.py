from django.shortcuts import render

from passagens.forms import PassagemForms


def index(request):
    form = PassagemForms()
    context = {
        'form': form,
    }
    return render(request, 'index.html', context=context)


def revisao_consulta(request):

    if request.method == 'POST':
        formulario = PassagemForms(request.POST)
        context = {
            'formulario': formulario,
        }
        return render(request, 'minha_consulta.html', context=context)
