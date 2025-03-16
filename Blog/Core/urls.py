from django.urls import path
from Core import views



urlpatterns = [
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/<int:pk>/', views.detalle_estudiante, name='detalle_estudiante'),
    path('profesores/', views.lista_profesores, name='lista_profesores'),
    path('profesores/<int:pk>/', views.detalle_profesor, name='detalle_profesor'),
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('index/', views.index, name='index'),
    path("listacursos/", views.cursos, name="lista_cursos"),
    path("listaprofesores/", views.profesores, name="lista_profesores"),
    path("listaestudiantes/", views.estudiantes, name="lista_estudiantes"),
       
]
