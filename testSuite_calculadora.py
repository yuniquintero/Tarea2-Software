##############################################################################
# Universidad Simon Bolivar
# Departamento de Computacion y Tecnologia de la Informacion
# CI3715: Ingenieria de Software I
#
# Suite de pruebas unitarias para calcularadora_precios.py
# ci3715.py
#
# @author Yuni Quintero 14-10880
# @author David Cabeza 13-10191
#
# Prof. Alfonso Reinoza
# @version 1 05/18
##############################################################################

#from calcularadora_precios import *
import unittest

class TestSuite(unittest.TestCase):

	# Caso Frontera: El servicio dura exactamente quince minutos
	def test_frontera_1(self):
		print("-- Caso Frontera #1 --")


	# Caso Frontera: El servicio dura exactamente 7 dias.
	def test_frontera_2(self):
		print("-- Caso Frontera #2 --")

	# Caso Interior: El servicio dura 6 dias, 23 horas y 45 minutos.
	def test_interior_1(self):
		print("-- Caso Interior #1 --")

	# Caso Interior: El servicio dura 5 dias e incluye fin de semana.
	def test_interior_2(self):
		print("-- Caso Interior #2 --")

	# Caso Malicioso: El servicio dura 5 minutos.
	def test_malicioso_1(self):
		print("-- Test Malicioso #1 --")

	# Caso Malicioso: El servicio dura 15 dias y 2 horas.
	def test_malicioso_2(self):
		print("-- Test Malicioso #2 --")

	# Caso Malicioso: La tarifa es un valor negativo.
	def test_malicioso_3(self):
		print("-- Test Malicioso #3 --")

	# Caso Esquina: El servicio dura 8 dias, 1 hora.
	def test_esquina_1(self):
		print("-- Test Esquina #1 --")

	# Caso Esquina: El servicio dura 1 hora y 1 minuto.
	def test_esquina_2(self):
		print("-- Test Esquina #2 --")

if __name__ == '__main__':
	unittest.main()