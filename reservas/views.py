# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect, HttpRequest
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models import Count
import datetime
from reservas.forms import *
from reservas.models import *
from django.contrib import messages


from datetime import *

@login_required(login_url='/ingresar')
def Reservas(request):
	m = Mesa.objects.all()
	today = datetime.today()

	d = today.strftime("%d")
	r = Reserva.objects.filter(actualizacion__day=d)

	if request.method=='POST':
		m = request.POST.get('mesa')
		c = request.POST.get('contacto')
		f = request.POST.get('fecha')
		h = request.POST.get('hora')

		registro = str(f) + ' ' + str(h)
		seleccionada = Mesa.objects.get(id=m)
		reg = Reserva(mesa = seleccionada, actualizacion = registro, contacto =c)
		reg.save()

		messages.info(request, 'Registrado correctamente.')
		return HttpResponseRedirect('/reservas')

	context = {
	'mesas':m,
	'reservas':r,
	}
	return render(request, 'simple.html', context)



def Resultados(request):
	m = Mesa.objects.all()
	today = datetime.today()
	r=[]
	if request.method=='POST':
		f = request.POST.get('fecha')
		h = request.POST.get('hora')
		a = str(f) + " " + str(h)
		r = Reserva.objects.filter(actualizacion = a)

	context = {
	'mesas':m,
	'reservas':r,
	}
	return render(request, 'simple.html', context)
