from django.urls import path
from . import views

urlpatterns = [
    path('tareas/', views.TareaListCreate.as_view(), name='tareas-list-create'),
    path('tareas/<int:pk>/', views.TareaRetrieveUpdateDestroy.as_view(), name='tarea-detail'),
    path('ordenar/', views.ordenar_lista, name='ordenar-lista'),
    path('contar-palabras/', views.contar_palabras, name='contar-palabras'),
]
