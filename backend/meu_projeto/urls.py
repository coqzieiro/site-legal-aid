"""
URL configuration for meu_projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, re_path, include  # Adicione o re_path
from django.shortcuts import render


# urlpatterns = [
#     path('', homepage, name='home'),  # Página inicial
#     path('api/', include('app.urls')),  # Rotas da API
#     path('admin/', admin.site.urls),  # Admin do Django
# ]


# Função que renderiza o index.html do frontend
def render_frontend(request):
    return render(request, 'index.html')

# Rotas do Django
urlpatterns = [
    path('', render_frontend, name='home'),  # Página inicial
    path('cadastrar/', render_frontend, name='cadastrar'),  # Página de cadastro
    path('api/', include('app.urls')),  # Rotas da API
    path('admin/', admin.site.urls),  # Admin do Django
    re_path(r'^.*$', render_frontend),  # Garante que outras rotas do frontend funcionem
]
