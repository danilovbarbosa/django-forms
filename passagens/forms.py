from datetime import datetime

from django import forms
from django.forms import SelectDateWidget
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker


class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=SelectDateWidget(empty_label="Nothing"))
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
