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
import datetime

class Tarifa:
	def __init__(self, dia_semana, fin_semana)
		try:
			assert(dia_semana >= 0 and fin_semana >= 0)
		except:
			return("Tarifa debe ser positiva")
			sys.exit()
		self.dia_semana = dia_semana
		self.fin_semana = fin_semana

class Servicio:

	def __init__(self, inicioDeServicio, finDeServicio):
		try:
			assert(finDeServicio.second - inicioDeServicio.second <= 7*24*60*60)
		except:
			return("EL periodo del servicio debe ser menor o igual a siete dias")
			sys.exit()

		try:
			assert(finDeServicio.second - inicioDeServicio.second >= 15*60)
		except:
			return("El periodo del servicio debe ser mayor o igual a 15 minutos")
			sys.exit()

		self.inicio = inicioDeServicio
		self.fin = finDeServicio

	def calcularPrecio(self, tarifa, tiempoDeServicio):

		answer = 0

		t_dia_semana = tarifa.dia_semana
		t_fin_semana = tarifa.fin_semana

		inicioDeServicio = tiempoDeServicio.inicio
		finDeServicio = tiempoDeServicio.fin

		actual = inicioDeServicio

		while actual < finDeServicio:
			if (actual[1].weekday() == 5) or (actual[1].weekday() == 6):
				answer += t_fin_semana
			else:
				answer += t_dia_semana
			actual += datetime.timedelta(hours=1)

		return answer