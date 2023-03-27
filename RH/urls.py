"""RH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from relogioponto import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views



urlpatterns = [

    path('admin/', admin.site.urls),
    
    # URLs para listagem
    path('lista_funcionarios/', views.lista_funcionarios, name='lista_funcionarios'),
    path('lista_setor/', views.lista_setor, name='lista_setor'),
    path('lista_periodo/', views.lista_periodos, name='lista_periodo'),
    path('lista_registro_ponto/', views.lista_registro_ponto, name='lista_registro_ponto'),
    path('lista_ferias/', views.lista_ferias, name='lista_ferias'),
    path('lista_saldo_diario/', views.lista_saldo_diario, name='lista_saldo_diario'),
    path('lista_horas_extras/', views.lista_horas_extras, name='lista_horas_extras'),

     # URLs para adicionar novos registros
    path('novo_funcionario/', views.novo_funcionario, name='novo_funcionario'),
    path('novo_setor/', views.novo_setor, name='novo_setor'),
    path('novo_periodo/', views.novo_periodo, name='novo_periodo'),
    path('novo_registro_ponto/', views.novo_registro_ponto, name='novo_registro_ponto'),
    path('nova_ferias/', views.nova_ferias, name='nova_ferias'),
    path('novo_saldo_diario/', views.novo_saldo_diario, name='novo_saldo_diario'),
    path('nova_hora_extra/', views.nova_hora_extra, name='nova_hora_extra'),

    # URLs para editar registros
    path('edita_funcionario/<int:pk>/', views.edita_funcionario, name='edita_funcionario'),
    path('edita_setor/<int:pk>/', views.edita_setor, name='edita_setor'),
    path('edita_periodo/<int:pk>/', views.edita_periodo, name='edita_periodo'),
    path('edita_registro_ponto/<int:pk>/', views.edita_registro_ponto, name='edita_registro_ponto'),
    path('edita_ferias/<int:pk>/', views.edita_ferias, name='edita_ferias'),
    path('edita_saldo_diario/<int:pk>/', views.edita_saldo_diario, name='edita_saldo_diario'),
    path('edita_hora_extra/<int:pk>/', views.edita_hora_extra, name='edita_hora_extra'),

    # URLs para deletar registros
    path('deleta_funcionario/<int:pk>/', views.deleta_funcionario, name='deleta_funcionario'),
    path('deleta_setor/<int:pk>/', views.deleta_setor, name='deleta_setor'),
    path('deleta_periodo/<int:pk>/', views.deleta_periodo, name='deleta_periodo'),
    path('deleta_registro_ponto/<int:pk>/', views.deleta_registro_ponto, name='deleta_registro_ponto'),
    path('deleta_ferias/<int:pk>/', views.deleta_ferias, name='deleta_ferias'),
    path('deleta_saldo_diario/<int:pk>/', views.deleta_saldo_diario, name='deleta_saldo_diario'),
    path('deleta_hora_extra/<int:pk>/', views.deleta_hora_extra, name='deleta_hora_extra'),
    path('', views.home, name='home'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.logout_view, name='logout'),

]
