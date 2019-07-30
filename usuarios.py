#SELECT########################################################################
#Recupera todos los usuarios del fichero y los devuelve como lista
def recuperarUsuarios():
	fichero = open(r"db\usuarios.dat","r")
	usuarios = []
	for linea in fichero:
		linea=linea.replace('\n','')
		usuario = linea.split(";")
		usuarios.append(usuario)
	fichero.close()
	return usuarios
	
#Recupera un usuario en concreto por su id		
def recuperarUsuarioPorId(id):
	fichero = open(r"db\usuarios.dat","r")
	for linea in fichero:
		linea=linea.replace('\n','')
		usuario = linea.split(";")
		if (usuario[0]==id):
			return usuario
			fichero.close()
	return 0
	fichero.close()

#Recupera un usuario en concreto por su nombre
def recuperarUsuarioPorNombre(nombre):
	fichero = open(r"db\usuarios.dat","r")
	for linea in fichero:
		linea=linea.replace('\n','')
		usuario = linea.split(";")
		if (usuario[1]==nombre):
			return usuario
	return 0
	fichero.close()

#Recupera una lista de usuarios en base a su apellido
def recuperaUsuariosPorApellido(apellido):
	fichero = open(r"db\usuarios.dat","r")
	usuarios = []
	for linea in fichero:
		linea = linea.replace('\n','')
		usuario = linea.split(";")
		if (usuario[2]==apellido or usuario[3]==apellido):
			usuarios.append(usuario)
	return usuarios
	fichero.close()

#CREATES#######################################################################
#Crea un usuario el id se calcula en el momento
def crearUsuario(nombre, apellido1, apellido2, fechaNacimiento):
	fichero = open(r"db\usuarios.dat","a")
	cadena = montarUsuario(str(proximoID()),nombre,apellido1,apellido2,fechaNacimiento)
	fichero.write(cadena)
	#print(cadena)
	fichero.close()

#UPDATES#######################################################################
#actualiza un usuario pasandole todos los parámetros
def actualizarUsuarioPorId(id,nombre,apellido1,apellido2,fechaNacimiento):
	usuarios = recuperarUsuarios()
	cadena = ""
	for usuario in usuarios:
		if usuario[0] != id:
			cadena = cadena + montarUsuario(usuario[0],usuario[1],usuario[2],usuario[3],usuario[4])
	cadena = cadena + montarUsuario(id,nombre,apellido1,apellido2,fechaNacimiento)
	fichero = open(r"db\usuarios.dat","w")
	fichero.write(cadena)

#DELETES#######################################################################
#elimina el usuario que coincida con el id que se le pase
def eliminarUsuarioPorId(id):
	usuarios = recuperarUsuarios()
	cadena = ""
	for usuario in usuarios:
		if usuario[0] != id:
			cadena = cadena + montarUsuario(usuario[0],usuario[1],usuario[2],usuario[3],usuario[4])
	fichero = open(r"db\usuarios.dat","w")
	fichero.write(cadena)

#UTILES########################################################################
#Devuelve el próximo id del fichero de usuarios
#TODO hay que hacerlo común
def proximoID():
	listaId = []
	fichero = open(r"db\usuarios.dat","r")
	for linea in fichero:
		usuario = linea.split(";")
		listaId.append(usuario[0])
	listaId.sort()
	ultimoID = listaId[-1]
	siguienteID = int(ultimoID) + 1
	fichero.close()
	return siguienteID
	
#Monta la cadena necesaria para buscar, eliminar o crear un usuario
def montarUsuario(id,nombre,apellido1,apellido2,fechaNacimiento):
	cadena = id + ";" + nombre + ";" + apellido1 + ";" + apellido2 + ";" + fechaNacimiento + "\n"
	return cadena