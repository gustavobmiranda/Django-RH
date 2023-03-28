from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from relogioponto.models import Funcionarios, Ferias, RegistroPonto, Setor, SaldoDiario, HorasExtras, Periodo
from relogioponto.forms import FuncionariosForm, FeriasForm, RegistroPontoForm, SetorForm, SaldoDiarioForm, HorasExtrasForm, PeriodoForm

#funcionarios
@login_required
def lista_funcionarios(request):
    funcionarios = Funcionarios.objects.all()
    return render(request, 'relogioponto/lista_funcionarios.html', {'funcionarios': funcionarios})
@login_required
def novo_funcionario(request):
    if request.method == "POST":
        form = FuncionariosForm(request.POST)
        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.save()
            return redirect('lista_funcionarios')
    else:
        form = FuncionariosForm()
    return render(request, 'relogioponto/novo_funcionario.html', {'form': form})
@login_required
def edita_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionarios, pk=pk)
    if request.method == "POST":
        form = FuncionariosForm(request.POST, instance=funcionario)
        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.save()
            return redirect('lista_funcionarios')
    else:
        form = FuncionariosForm(instance=funcionario)
    return render(request, 'relogioponto/edita_funcionario.html', {'form': form})
@login_required
def deleta_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionarios, pk=pk)
    funcionario.delete()
    return redirect('lista_funcionarios')

#ferias
def lista_ferias(request):
    ferias = Ferias.objects.all()
    return render(request, 'relogioponto/lista_ferias.html', {'ferias': ferias})

def nova_ferias(request):
    if request.method == "POST":
        form = FeriasForm(request.POST)
        if form.is_valid():
            ferias = form.save(commit=False)
            ferias.save()
            return redirect('lista_ferias')
    else:
        form = FeriasForm()
    return render(request, 'relogioponto/nova_ferias.html', {'form': form})

def edita_ferias(request, pk):
    ferias = get_object_or_404(Ferias, pk=pk)
    if request.method == "POST":
        form = FeriasForm(request.POST, instance=ferias)
        if form.is_valid():
            ferias = form.save(commit=False)
            ferias.save()
            return redirect('lista_ferias')
    else:
        form = FeriasForm(instance=ferias)
    return render(request, 'relogioponto/edita_ferias.html', {'form': form})

def deleta_ferias(request, pk):
    ferias = get_object_or_404(Ferias, pk=pk)
    ferias.delete()
    return redirect('lista_ferias')

#registroponto
def lista_registro_ponto(request):
    registro_ponto = RegistroPonto.objects.all()
    return render(request, 'relogioponto/lista_registro_ponto.html', {'registro_ponto': registro_ponto})

def novo_registro_ponto(request):
    if request.method == "POST":
        form = RegistroPontoForm(request.POST)
        if form.is_valid():
            registro_ponto = form.save(commit=False)
            registro_ponto.save()
            return redirect('lista_registro_ponto')
    else:
        form = RegistroPontoForm()
    return render(request, 'relogioponto/novo_registro_ponto.html', {'form': form})

def edita_registro_ponto(request, pk):
    registro_ponto = get_object_or_404(RegistroPonto, pk=pk)
    if request.method == "POST":
        form = RegistroPontoForm(request.POST, instance=registro_ponto)
        if form.is_valid():
            registro_ponto = form.save(commit=False)
            registro_ponto.save()
            return redirect('lista_registro_ponto')
    else:
        form = RegistroPontoForm(instance=registro_ponto)
    return render(request, 'relogioponto/edita_registro_ponto.html', {'form': form})

def deleta_registro_ponto(request, pk):
    registro_ponto = get_object_or_404(RegistroPonto, pk=pk)
    registro_ponto.delete()
    return redirect('lista_registro_ponto')

#setor
def lista_setor(request):
    setor = Setor.objects.all()
    return render(request, 'relogioponto/lista_setor.html', {'setor': setor})

def novo_setor(request):
    if request.method == "POST":
        form = SetorForm(request.POST)
        if form.is_valid():
            setor = form.save(commit=False)
            setor.save()
            return redirect('lista_setor')
    else:
        form = SetorForm()
    return render(request, 'relogioponto/novo_setor.html', {'form': form})

def edita_setor(request, pk):
    setor = get_object_or_404(Setor, pk=pk)
    if request.method == "POST":
        form = SetorForm(request.POST, instance=setor)
        if form.is_valid():
            setor = form.save(commit=False)
            setor.save()
            return redirect('lista_setor')
    else:
        form = SetorForm(instance=setor)
    return render(request, 'relogioponto/edita_setor.html', {'form': form})

def deleta_setor(request, pk):
    setor = get_object_or_404(Setor, pk=pk)
    setor.delete()
    return redirect('lista_setor')

#saldodiario
def lista_saldo_diario(request):
    saldo_diario = SaldoDiario.objects.all()
    return render(request, 'relogioponto/lista_saldo_diario.html', {'saldo_diario': saldo_diario})

def novo_saldo_diario(request):
    if request.method == "POST":
        form = SaldoDiarioForm(request.POST)
        if form.is_valid():
            saldo_diario = form.save(commit=False)
            saldo_diario.save()
            return redirect('lista_saldo_diario')
    else:
        form = SaldoDiarioForm()
    return render(request, 'relogioponto/novo_saldo_diario.html', {'form': form})

def edita_saldo_diario(request, pk):
    saldo_diario = get_object_or_404(SaldoDiario, pk=pk)
    if request.method == "POST":
        form = SaldoDiarioForm(request.POST, instance=saldo_diario)
        if form.is_valid():
            saldo_diario = form.save(commit=False)
            saldo_diario.save()
            return redirect('lista_saldo_diario')
    else:
        form = SaldoDiarioForm(instance=saldo_diario)
    return render(request, 'relogioponto/edita_saldo_diario.html', {'form': form})

def deleta_saldo_diario(request, pk):
    saldo_diario = get_object_or_404(SaldoDiario, pk=pk)
    saldo_diario.delete()
    return redirect('lista_saldo_diario')

#horaextra
def lista_horas_extras(request):
    horas_extras = HorasExtras.objects.all()
    return render(request, 'relogioponto/lista_horas_extras.html', {'horas_extras': horas_extras})

def nova_hora_extra(request):
    if request.method == "POST":
        form = HorasExtrasForm(request.POST)
        if form.is_valid():
            hora_extra = form.save(commit=False)
            hora_extra.save()
            return redirect('lista_horas_extras')
    else:
        form = HorasExtrasForm(request.POST)
    return render(request, 'relogioponto/nova_hora_extra.html', {'form': form})

def edita_hora_extra(request, pk):
    hora_extra = get_object_or_404(HorasExtras, pk=pk)
    if request.method == "POST":
        form = HorasExtrasForm(request.POST, instance=hora_extra)
        if form.is_valid():
            hora_extra = form.save(commit=False)
            hora_extra.save()
            return redirect('lista_horas_extras')
    else:
        form = HorasExtrasForm(instance=hora_extra)
    return render(request, 'relogioponto/edita_hora_extra.html', {'form': form})

def deleta_hora_extra(request, pk):
    hora_extra = get_object_or_404(HorasExtras, pk=pk)
    hora_extra.delete()
    return redirect('lista_horas_extras')

#periodo
def lista_periodos(request):
    periodos = Periodo.objects.all()
    return render(request, 'relogioponto/lista_periodos.html', {'periodos': periodos})

def novo_periodo(request):
    if request.method == "POST":
        form = PeriodoForm(request.POST)
        if form.is_valid():
            periodo = form.save(commit=False)
            periodo.save()
            return redirect('lista_periodos')
    else:
        form = PeriodoForm()
    return render(request, 'relogioponto/novo_periodo.html', {'form': form})

def edita_periodo(request, pk):
    periodo = get_object_or_404(Periodo, pk=pk)
    if request.method == "POST":
        form = PeriodoForm(request.POST, instance=periodo)
        if form.is_valid():
            periodo = form.save(commit=False)
            periodo.save()
            return redirect('lista_periodos')
    else:
        form = PeriodoForm(instance=periodo)
    return render(request, 'relogioponto/edita_periodo.html', {'form': form})

def deleta_periodo(request, pk):
    periodo = get_object_or_404(Periodo, pk=pk)
    periodo.delete()
    return redirect('lista_periodos')

#home
def home(request):
    return render(request, 'relogioponto/home.html')

def logout_view(request):
    logout(request)
    return redirect('home')