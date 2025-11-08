from django.urls import path
from . import views
urlpatterns = [
	path("", views.index, name="index"),
    path("info/", views.info, name="info"),
    path("pag1", views.pag1, name="f"),
    path("pag2", views.pag2, name="g"),
    path("exemplu", views.afis_template, name="ex"),
    path("exemplu1", views.afis_ex, name="alb"),
]