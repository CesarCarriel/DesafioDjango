from django.contrib import admin
from django.urls import path
from views.api.localizacao import RegiaoViewSet, RegiaoCreateViewSet, CidadeViewSet, CidadeCreateViewSet
from views.api.imovel import ListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cidade/', CidadeCreateViewSet.as_view()),
    path('cidade/<int:pk>', CidadeViewSet.as_view()),
    path('regiao/', RegiaoCreateViewSet.as_view()),
    path('regiao/<int:pk>', RegiaoViewSet.as_view()),
    path('propriedades', ListView.as_view({'get': 'list'})),
]
