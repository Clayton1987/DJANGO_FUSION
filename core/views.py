#from django.shortcuts import render
from typing import Any
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from .models import Servico, Funcionario
from .forms import ContatoForm
from django.contrib import messages
from django.urls import reverse_lazy



class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.all()
        return context
    
    def form_valid(self, form, *args, **kwards):
        form.send_email()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwards) -> HttpResponse:
        messages.error(self.request, 'Erro ao enviar email')
        return super(IndexView, self).form_invalid(form, *args, **kwards)


class TesteView(TemplateView):
    template_name = 'teste.html'
    