from django.urls import path
from . import views

app_name = 'app_prestamos'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_cliente>/', views.detalle, name='detalle'),
    path('<int:id_cliente>/prestamos/', views.prestamos, name='prestamos'),
    path('<int:id_cliente>/resultados/', views.resultados, name='resultados'),
    path('<int:id_cliente>/agregar_prestamo/', views.agregar_prestamo, name='agregar_prestamo'),

]
