from django.contrib import admin
from django.urls import path, include
from views.api.localizacao import RegiaoViewSet, RegiaoCreateViewSet, CidadeViewSet, CidadeCreateViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cidade/', CidadeCreateViewSet.as_view()),
    path('cidade/<int:pk>', CidadeViewSet.as_view()),
    path('regiao/', RegiaoCreateViewSet.as_view()),
    path('regiao/<int:pk>', RegiaoViewSet.as_view()),
]
'''
from core import views

urlpatterns = [
    path('persons/', views.PersonList.as_view()),
    path('persons/<int:pk>/', views.PersonDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

'''
