from django.db import models

class Funcionarios(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    # Outros campos aqui

    def __str__(self):
        return self.nome

class Ferias(models.Model):
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return self.funcionario.nome

class RegistroPonto(models.Model):
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    entrada = models.DateTimeField()
    saida = models.DateTimeField()
    horas_trabalhadas = models.DecimalField(max_digits=4, decimal_places=2)
    data = models.DateField()
    saldo_diario = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.funcionario.nome} ({self.data})"

class Setor(models.Model):
    nome = models.CharField(max_length=200)
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.funcionario.nome}"

class SaldoDiario(models.Model):
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.funcionario.nome

class HorasExtras(models.Model):
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()

    def __str__(self):
        return f"{self.funcionario.nome} ({self.inicio} - {self.fim})"

class Periodo(models.Model):
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    horas_extras = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.funcionario.nome} ({self.data_inicio} - {self.data_fim})"
