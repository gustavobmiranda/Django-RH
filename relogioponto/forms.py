from django import forms
from .models import Funcionarios, Ferias, RegistroPonto, Setor, SaldoDiario, HorasExtras, Periodo

class FuncionariosForm(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = ['nome', 'cpf', 'cargo', 'email'] # adicionar campos

class FeriasForm(forms.ModelForm):
    class Meta:
        model = Ferias
        fields = ['funcionario', 'data_inicio', 'data_fim']

class RegistroPontoForm(forms.ModelForm):
    class Meta:
        model = RegistroPonto
        fields = ['funcionario', 'entrada', 'saida', 'horas_trabalhadas', 'data', 'saldo_diario']

class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = ['nome', 'funcionario']

class SaldoDiarioForm(forms.ModelForm):
    class Meta:
        model = SaldoDiario
        fields = ('funcionario', 'saldo')
        widgets = {
            'funcionario': forms.Select(attrs={'class': 'form-control'}),
            'saldo': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class HorasExtrasForm(forms.ModelForm):
    class Meta:
        model = HorasExtras
        fields = ['funcionario', 'inicio', 'fim']
        widgets = {
            'inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fim': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

class PeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ['funcionario', 'data_inicio', 'data_fim', 'horas_extras']
