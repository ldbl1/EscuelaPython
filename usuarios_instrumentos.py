from usuarios import *
from instrumentos import * 
#SELECTS#######################################################################
#Recupera todos los instrumentos de un usuario
def recuperaInstrumentosDeUsuarioPorIDDeUsuario(idUsuario):
	#Busco todos los datos del usuario y los guardo en usuario
	usuario = recuperarUsuarioPorId(idUsuario)

	#Busco los instrumentos del usuario
	fichero_usuarios_instrumentos = open(r"db\usuarios_instrumentos.dat","r")
	instrumentosDef = []
	for linea in fichero_usuarios_instrumentos:
		linea=linea.replace('\n','')
		instrumento_usuario = linea.split(";")
		if (instrumento_usuario[0] == idUsuario):
			#voy añadiendo a la lista los nombres de los instrumentos que tenga
			instrumentosDef.append((recuperarInstrumentoPorId(instrumento_usuario[1]))[1])

	fichero_usuarios_instrumentos.close()
	#Hago append para que salga como una sublista de usuario
	usuario.append(instrumentosDef)
	return usuario

#Recupera todos los usuarios de un instrumento
def recuperaUsuariosDeUnInstrumento(idInstrumento):
	#Busco todos los datos del usuario y los guardo en usuario
	instrumento = recuperarInstrumentoPorId(idInstrumento)

	#Busco los usuarios del instrumento
	fichero_usuarios_instrumentos = open(r"db\usuarios_instrumentos.dat","r")
	usuariosDef = []
	for linea in fichero_usuarios_instrumentos:
		linea=linea.replace('\n','')
		instrumento_usuario = linea.split(";")
		if (instrumento_usuario[1] == idInstrumento):
			#voy añadiendo a la lista los nombres de los instrumentos que tenga
			usuariosDef.append((recuperarUsuarioPorId(instrumento_usuario[0])))

	fichero_usuarios_instrumentos.close()
	#Hago append para que salga como una sublista de usuario
	instrumento.append(usuariosDef)
	return instrumento

#CREATES#######################################################################
#Crea una vinculacion de un usuario a un instrumento
def crearVinculacionUsuarioConInstrumento(idUsuario,idInstrumento):
	#Comprobamos que no exista ya la vinculación
	fichero_usuarios_instrumentos = open(r"db\usuarios_instrumentos.dat","r")
	for linea in fichero_usuarios_instrumentos:
		linea=linea.replace('\n','')
		instrumento_usuario = linea.split(";")
		if (instrumento_usuario[0] == idUsuario and instrumento_usuario[1] == idInstrumento):
			return 0
	fichero_usuarios_instrumentos.close()

	fichero = open(r"db\usuarios_instrumentos.dat","a")
	cadena = montarUsuario_Instrumentos(idUsuario,idInstrumento)
	print("La cadena a escribir")
	print(cadena)
	fichero.write(cadena)
	fichero.close()
	return 1

#UPDATES#######################################################################
#Se desestima de momento

#DELETES#######################################################################
#Elimina la vinculacion de un usuario a un instrumento
def eliminarUnInstrumentoDeUnUsuario(idInstrumento,idUsuario):
	#Comprobamos que exista ya la vinculación
	fichero_usuarios_instrumentos = open(r"db\usuarios_instrumentos.dat","r")
	cadena = ""
	for linea in fichero_usuarios_instrumentos:
		linea=linea.replace('\n','')
		usuario_instrumento = linea.split(";")
		if not (usuario_instrumento[0] != idUsuario and usuario_instrumento[1] != idInstrumento):
			cadena = cadena + montarUsuario_Instrumentos(usuario_instrumento[0],usuario_instrumento[1])
	fichero_usuarios_instrumentos.close()
	fichero = open(r"db\usuarios_instrumentos.dat","w")
	fichero.write(cadena)
	fichero.close()

#Elimina todos los instrumentos de un usuario
def eliminarTodosLosInstrumentosDeUnUsuario(idUsuario):
	return 0
	#TODO

#Elimina todos los usuarios de un instrumento
def eliminarTodosLosUsuariosDeUnInstrumento(idInstrumento):
	return 0
	#TODO

#UTILES########################################################################
def montarUsuario_Instrumentos(idUsuario,idInstrumento):
	cadena = idUsuario + ";" + idInstrumento + "\n"
	return cadena

def testtrutru(a,b):

	if a and b:
		print("OK")
	else:
		print("KO")