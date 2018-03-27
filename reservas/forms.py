from django.forms import *
from django import forms
from reservas.models import *


class formulario_reservas(ModelForm):
	class Meta:
		model = Reserva
		fields = ['mesa', 'actualizacion', 'contacto']

