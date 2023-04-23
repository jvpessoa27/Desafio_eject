from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='produtos'),
    path('criar/', views.registrar_produto, name='registrar_produto'),
    path('<id>/editar', views.editar_produto, name='editar_produto'),
    path('detalhar', views.detalhar, name='detalhar_produto'),
    path('<id>/deletar', views.deletar, name='deletar_produto'),
]
