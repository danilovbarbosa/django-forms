from django.shortcuts import render

from passagens.forms import PassagemForms, PessoaForms


def index(request):
    form = PassagemForms()
    pessoas_form = PessoaForms()
    context = {
        'form': form,
        'pessoas_form': pessoas_form,
    }
    return render(request, 'index.html', context=context)


def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForms(request.POST)
        pessoa_form = PessoaForms(request.POST)

        if form.is_valid():
            context = {
                'form': form,
                'pessoa_form': pessoa_form,
            }
            return render(request, 'minha_consulta.html', context=context)
        else:
            context = {
                'form': form,
                'pessoa_form': pessoa_form,
            }
            return render(request, 'index.html', context=context)
