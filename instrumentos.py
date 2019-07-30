#SELECTS#######################################################################
#Recupera una lista de todos los instrumentos disponibles
def recuperarInstrumentos():
	fichero = open(r"db\instrumentos.dat","r")
	instrumentos = []
	for linea in fichero:
		linea=linea.replace('\n','')
		instrumento = linea.split(";")		
		instrumentos.append(instrumento)
	fichero.close()
	return instrumentos

#Recupera un instrumento en concreto por su id		
def recuperarInstrumentoPorId(id):
	fichero = open(r"db\instrumentos.dat","r")
	for linea in fichero:
		linea=linea.replace('\n','')
		instrumento = linea.split(";")
		if (instrumento[0]==id):
			return instrumento
	fichero.close()

#Recupera un instrumento por su nombre
def recuperarInstrumentoPorNombre(nombre):
	fichero = open(r"db\instrumentos.dat","r")
	for linea in fichero:
		linea=linea.replace('\n','')
		instrumento = linea.split(";")
		if (instrumento[1]==nombre):
			return instrumento
	return 0
	fichero.close()

#CREATES#######################################################################
#Crea instrumento. El id lo recupera en el momento
def crearInstrumento(nombre):
	fichero = open(r"db\instrumentos.dat","a")
	cadena = montarInstrumento(str(proximoID()),nombre)
	fichero.write(cadena)
	#print(cadena)
	fichero.close()

#UPDATES#######################################################################
#Actualiza instrumento por ID
def actualizarInstrumentoPorId(id,nombre):
	instrumentos = recuperarInstrumentos()
	cadena = ""
	for instrumento in instrumentos:
		if instrumento[0] != id:
			cadena = cadena + montarInstrumento(instrumento[0],instrumento[1])
	cadena = cadena + montarInstrumento(id,nombre)
	fichero = open(r"db\instrumentos.dat","w")
	fichero.write(cadena)

#DELETES#######################################################################
#Elimina instrumento por ID
def eliminarInstrumentoPorID(id):
	instrumentos = recuperarInstrumentos()
	cadena = ""
	for instrumento in instrumentos:
		if instrumento[0] != id:
			cadena = cadena + montarInstrumento(instrumento[0],instrumento[1])
	fichero = open(r"db\instrumentos.dat","w")
	fichero.write(cadena)

#UTILES########################################################################
#Monta la cadena necesaria para buscar, eliminar o crear un instrumento
def montarInstrumento(id,nombre):
	cadena = id + ";"
	cadena = cadena + nombre
	cadena = cadena + "\n"
	return cadena

#Devuelve el próximo id del fichero de usuarios
#TODO hay que hacerlo común
def proximoID():
	listaId = []
	fichero = open(r"db\insturmentos.dat","r")
	for linea in fichero:
		instrumento = linea.split(";")
		listaId.append(instrumento[0])
	listaId.sort()
	ultimoID = listaId[-1]
	siguienteID = int(ultimoID) + 1
	fichero.close()
	return siguienteID
