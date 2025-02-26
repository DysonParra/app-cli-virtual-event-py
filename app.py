"""
@fileoverview    {FileName}

@version         2.0

@author          Dyson Arley Parra Tilano <dysontilano@gmail.com>

@copyright       Dyson Parra
@see             github.com/DysonParra

History
@version 1.0     Implementation done.
@version 2.0     Documentation added.
"""
import os, ctypes
from datetime import datetime


VK_MOUSE_CLIC_EVENT_LEFT		= 1
VK_MOUSE_CLIC_EVENT_RIGHT 		= 2
VK_MOUSE_CLIC_EVENT_MIDDLE 		= 4
VK_MOUSE_CLIC_EVENT_LEFT_DOUBLE = 7

VK_MOUSE_MOVE_EVENT_LEFT		= 10
VK_MOUSE_MOVE_EVENT_RIGHT		= 20
VK_MOUSE_MOVE_EVENT_UP			= 30
VK_MOUSE_MOVE_EVENT_DOWN		= 40


def runVirtualKeyEvent(eventCode):
	"""
	Hace de Wrapper para llamar a la funcion de C
	"""
	return libVirtualEvent.runVirtualKeyEvent(eventCode)


def runVirtualMouseClicEvent(eventCode):
	"""
	Hace de Wrapper para llamar a la funcion de C
	"""
	return libVirtualEvent.runVirtualMouseClicEvent(eventCode)


def runVirtualMouseMoveEvent(eventCode, pixelQuantity):
	"""
	Hace de Wrapper para llamar a la funcion de C
	"""
	return libVirtualEvent.runVirtualMouseMoveEvent(eventCode, pixelQuantity)


def main():
	"""
	Entrada principal del sistema.
	"""
	DATE_FORMAT ="%Y-%m-%d %H:%M:%S"
	print(f"\nStart date: {datetime.now().strftime(DATE_FORMAT)}\n")

	# Carga la biblioteca virtualEvent (python de ser de 32-bit).
	libFile = "virtual_event_x86.dll"
	global libVirtualEvent
	libVirtualEvent = ctypes.CDLL(f"{os.getcwd()}/{libFile}")

	# Se definen los tipos de los argumentos y el tipo del retorno.
	libVirtualEvent.runVirtualKeyEvent.argtypes = (ctypes.c_int,)
	libVirtualEvent.runVirtualMouseClicEvent.argtypes = (ctypes.c_int,)
	libVirtualEvent.runVirtualMouseMoveEvent.argtypes = (ctypes.c_int,ctypes.c_int,)

	#Llama a las funciones de virtualEvent.
	runVirtualKeyEvent(91)

	print(f"\nEnd date:   {datetime.now().strftime(DATE_FORMAT)}")


if __name__ == "__main__":
	main()
