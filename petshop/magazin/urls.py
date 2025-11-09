from django.urls import path
from . import views
urlpatterns = [
	path("", views.index, name="index"),
    path("info/", views.info, name="info"),
    path("exemplu", views.afis_template, name="ex"),
    path("exemplu1", views.afis_ex, name="alb"),
    path("log/", views.log, name="log"),
    path("despre/", views.despre, name="despre"),
    path("produse/", views.pag_produse, name="produse"),
    path("servicii/", views.in_lucru, name="in_lucru"),
    path("contact/", views.in_lucru, name="in_lucru"),
    path("cos_virtual/", views.in_lucru, name="in_lucru"),
    path("blog/", views.in_lucru, name="in_lucru"),
    path('produse/<int:pk>/', views.pag_prod, name='pag_prod'),
    path('categorii/<str:slug_categorie>', views.pag_categorie, name='pag_categorie'),
    path('api/filtru/', views.ajax_filtru, name='ajax_filtru'),
]