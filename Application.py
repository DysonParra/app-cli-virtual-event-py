# Importamos la biblioteca ctypes
import ctypes

# Cargamos la biblioteca virtualEvent.
libVirtualEvent = ctypes.CDLL('virtual_event.dll')

VK_MOUSE_CLIC_EVENT_LEFT		= 1
VK_MOUSE_CLIC_EVENT_RIGHT 		= 2
VK_MOUSE_CLIC_EVENT_MIDDLE 		= 4
VK_MOUSE_CLIC_EVENT_LEFT_DOUBLE = 7

VK_MOUSE_MOVE_EVENT_LEFT	= 10
VK_MOUSE_MOVE_EVENT_RIGHT	= 20
VK_MOUSE_MOVE_EVENT_UP		= 30
VK_MOUSE_MOVE_EVENT_DOWN	= 40

# Se definen los tipos de los argumentos y el tipo del retorno.
libVirtualEvent.runVirtualKeyEvent.argtypes = (ctypes.c_int,)

# Se definen los tipos de los argumentos y el tipo del retorno.
libVirtualEvent.runVirtualMouseClicEvent.argtypes = (ctypes.c_int,)

# Se definen los tipos de los argumentos y el tipo del retorno.
libVirtualEvent.runVirtualMouseMoveEvent.argtypes = (ctypes.c_int,ctypes.c_int,)

# Hace de Wrapper para llamar a la funcion de C
def runVirtualKeyEvent(eventCode):
	return libVirtualEvent.runVirtualKeyEvent(eventCode)

# Hace de Wrapper para llamar a la funcion de C
def runVirtualMouseClicEvent(eventCode):
	return libVirtualEvent.runVirtualMouseClicEvent(eventCode)

# Hace de Wrapper para llamar a la funcion de C
def runVirtualMouseMoveEvent(eventCode, pixelQuantity):
	return libVirtualEvent.runVirtualMouseMoveEvent(eventCode, pixelQuantity)

#Llama a las funciones de virtualEvent.
runVirtualKeyEvent(91)

#runVirtualMouseClicEvent(VK_MOUSE_CLIC_EVENT_LEFT)
#runVirtualMouseClicEvent(VK_MOUSE_CLIC_EVENT_RIGHT)
#runVirtualMouseClicEvent(VK_MOUSE_CLIC_EVENT_MIDDLE)
#runVirtualMouseClicEvent(VK_MOUSE_CLIC_EVENT_LEFT_DOUBLE)

#runVirtualMouseMoveEvent(VK_MOUSE_MOVE_EVENT_LEFT,  20)
#runVirtualMouseMoveEvent(VK_MOUSE_MOVE_EVENT_RIGHT, 20)
#runVirtualMouseMoveEvent(VK_MOUSE_MOVE_EVENT_UP,    20)
#runVirtualMouseMoveEvent(VK_MOUSE_MOVE_EVENT_DOWN,  20)
