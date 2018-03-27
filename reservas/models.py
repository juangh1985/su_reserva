# Create your models here.
#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Mesa(models.Model):
	codigo=models.CharField('Codigo',max_length=30,blank=True,null=True)
	nombre=models.CharField('Mesa',max_length=30,blank=True,null=True)
	def __unicode__(self):
		return '%s' % (self.nombre)

class Reserva(models.Model):
	mesa=models.ForeignKey(Mesa,max_length=30,blank=True,null=True)
	actualizacion= models.DateTimeField('Reserva',auto_now=False)
	contacto=models.CharField('Contacto',max_length=30,blank=True,null=True)

	def __unicode__(self):
		return '%s' % (self.mesa)
