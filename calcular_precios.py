##############################################################################
# Universidad Simon Bolivar
# Departamento de Computacion y Tecnologia de la Informacion
# CI3715: Ingenieria de Software I
#
# Suite de pruebas unitarias para calculadora_precios.py
# ci3715.py
#
# @author Yuni Quintero 14-10880
# @author David Cabeza 13-10191
#
# Prof. Alfonso Reinoza
# @version 1 05/18
##############################################################################

import sys
from datetime import datetime, timedelta

def es_valida_tarifa(dia_semana, fin_semana):
	try:
		assert(dia_semana >= 0 and fin_semana >= 0)
	except:
		return("Tarifa debe ser positiva")
		sys.exit(0)

def es_valido_servicio(inicio, final):

	try:
		assert(fin.second - inicio.second >= 15*60)
	except:
		return("El periodo del servicio debe ser mayor o igual a 15 minutos")
		sys.exit(0)

	try:
		assert(fin.second - inicio.second <= 7*24*60*60)
	except:
		return("EL periodo del servicio debe ser menor o igual a siete dias")
		sys.exit(0)

class Tarifa:
	def __init__(self, dia_semana, fin_semana):
		es_valida_tarifa(dia_semana, fin_semana)
		self.dia_semana = dia_semana
		self.fin_semana = fin_semana

class Servicio:

	def __init__(self, inicioDeServicio, finDeServicio):
		
		es_valido_servicio(inicioDeServicio, finDeServicio)
		self.inicio = inicioDeServicio
		self.fin = finDeServicio

def calcular_precios(tarifa, Servicio):

	answer = 0

	t_dia_semana = tarifa.dia_semana
	t_fin_semana = tarifa.fin_semana

	inicioDeServicio = Servicio.inicio
	finDeServicio = Servicio.fin

	actual = inicioDeServicio

	while actual < finDeServicio:
		if (actual.weekday() == 5) or (actual.weekday() == 6):
			answer += t_fin_semana
		else:
			answer += t_dia_semana
		actual += timedelta(hours=1)

	return answer


'''
Dominio de calcular_precios:
Recibe como primer parametro una instancia de la clase Tarifa cuyos 
dos atributos son la tarifa del dia de semana y la tarifa del fin de semana, 
calculado por horas.
El segundo parametro de la funcion es una instancia de la clase Servicio
el cual tiene como atributos dos tipos de datos datetime, uno para la fecha
de inicio del servicio y otro para la fecha del fin del servicio.
El dominio tiene como restricicon que las tarifas no deben ser valores
negativos y que el tiempo transcurrido entre la fecha de inicio y fin no
supere los 7 dias y sea mayor a 15 minutos'''