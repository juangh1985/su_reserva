# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from reservas.models import *

class Mesa_Admin(admin.ModelAdmin):
	list_display=['nombre', 'codigo']
admin.site.register(Mesa,Mesa_Admin)

class Reserva_Admin(admin.ModelAdmin):
	pass
admin.site.register(Reserva,Reserva_Admin)
