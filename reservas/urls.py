from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^reservas', views.Reservas),
	url(r'^resultados', views.Resultados),
]

 



