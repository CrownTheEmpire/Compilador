class Nodo:
	"""docstring for Nodo"""

	_tabular = 1 #Se utilizara para mostrar el arbol de manera mas clara

	def __init__(self, simbolo = ""):
		self.simbolo = simbolo



class Programa(Nodo):
	"""docstring for Programa"""
	def __init__(self, pila, numRegla):
		pila.pop()
		self.definiciones = pila.pop().getNodo()

	def mostrar(self):
		arbol = "Programa"
		Nodo._tabular += 1

		arbol += "\n"

		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += self.definiciones.mostrar()
		Nodo._tabular -= 1
		return arbol



class Definiciones(Nodo):
	"""docstring for Definiciones"""
	def __init__(self, pila, numRegla):
		if numRegla == 2:
			self.definiciones = None
			self.definicion = None
			return
                
		pila.pop()
		self.definiciones = pila.pop().getNodo()
		print("TIPILLO: ", type(self.definiciones))
		pila.pop()
		self.definicion = pila.pop().getNodo()
		print("TIPILLO2: ", type(self.definicion))

	def mostrar(self):
		arbol = "Definiciones"

		if self.definicion == None:
			return arbol

		Nodo._tabular += 1

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += self.definicion.mostrar()

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"
		
		arbol += self.definiciones.mostrar()

		Nodo._tabular -= 1
		return arbol

class Definicion(Nodo):
	"""docstring for Definicion"""
	def __init__(self, pila, numRegla):
		print("NUMERO: ", numRegla)
		pila.pop()
		if numRegla == 4:
			self.def_Var_Func = pila.pop().getNodo()
		elif numRegla == 5:
			self.def_Var_Func = pila.pop().getNodo()

		print("Tipo 3:", type(self.def_Var_Func))

	def mostrar(self):
		arbol = "Definicion"
		Nodo._tabular += 1

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += self.def_Var_Func.mostrar()

		Nodo._tabular -= 1
		return arbol



class DefVar(Nodo):
	"""docstring for DefVar"""
	def __init__(self, pila, numRegla):
		pila.pop() #Quita el estado
		pila.pop() #Quita el ';'
		pila.pop() #Quita el estado
		self.listaVar = pila.pop().getNodo()
		print(type(self.listaVar))

		pila.pop()
		self.identificador = pila.pop().getSimbolo()

		print(type(self.identificador))
		print(self.identificador)
		pila.pop()
		self.tipo = pila.pop().getSimbolo()
		
	def mostrar(self):
		arbol = "DefVar"
		Nodo._tabular += 1

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += str(self.tipo)

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"
		
		arbol += str(self.identificador)

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"
		
		arbol += self.listaVar.mostrar()

		Nodo._tabular -= 1
		return arbol



class ListaVar(Nodo):
	"""docstring for ListaVar"""
	def __init__(self, pila, numRegla):
		if numRegla == 8:
			pila.pop() #Quita el estado
			self.listaVar = pila.pop().getNodo()
			print("TIPESCO: ", type(self.listaVar))

			pila.pop()
			self.identificador = pila.pop().getSimbolo()
			pila.pop() #Quita el estado
			pila.pop() #Se encarga de retirar la ',' de la pila

		else:
			self.listaVar = None
			self.identificador = "VACIO"
	
	def mostrar(self):
		arbol = "ListaVar"

		if self.listaVar == None:
			return arbol

		Nodo._tabular += 1

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += str(self.identificador)

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"
		
		arbol += self.listaVar.mostrar()

		Nodo._tabular -= 1
		return arbol



class DefFunc(Nodo):
	"""docstring for DefFunc"""
	def __init__(self, pila, numRegla):
		pila.pop()
		self.bloqueFunc = pila.pop().getNodo()
		print("BloqueFunc: ", type(self.bloqueFunc))

		pila.pop() #Quita el estado
		pila.pop() #Quita el parentesis de cierre ')'
		pila.pop() #Quita el estado
		self.parametros = pila.pop().getNodo()

		print("Parametros", type(self.parametros))

		pila.pop() #Quita el estado
		pila.pop() #Quita el parentesis de apertura '('
		pila.pop() #Quita el estado
		self.identificador = pila.pop().getSimbolo()
		pila.pop()
		self.tipo = pila.pop().getSimbolo()


	def mostrar(self):
		arbol = "DefFunc"

		Nodo._tabular += 1

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += str(self.tipo)

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += str(self.identificador)

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"
		
		arbol += self.parametros.mostrar()

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"
		
		arbol += self.bloqueFunc.mostrar()

		Nodo._tabular -= 1
		return arbol
	


class Parametros(Nodo):
	"""docstring for Parametros"""
	def __init__(self, pila, numRegla):
		if numRegla == 10:
			self.tipo = ""
			self.identificador = ""
			self.listaParam = None

		elif numRegla == 11:
			pila.pop()
			self.listaParam = pila.pop().getNodo()
			pila.pop() #Quita el estado
			self.identificador = pila.pop().getSimbolo()
			pila.pop()
			self.tipo = pila.pop().getSimbolo()

	def mostrar(self):
		arbol = "Parametros"

		if self.listaParam == None:
			return arbol

		Nodo._tabular += 1

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += str(self.tipo)

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += str(self.identificador)

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"
		
		arbol += self.listaParam.mostrar()

		Nodo._tabular -= 1
		return arbol



class ListaParam(Nodo):
	"""docstring for ListaPAram"""
	def __init__(self, pila, numRegla):
		if numRegla == 12:
			self.tipo = ""
			self.identificador = ""
			self.listaParam = None

		elif numRegla == 13:
			pila.pop()
			self.listaParam = pila.pop().getNodo()
			pila.pop() #Quita el estado
			self.identificador = pila.pop().getSimbolo()
			pila.pop()
			self.tipo = pila.pop().getSimbolo()
			pila.pop()
			pila.pop() #Quita la ','

	def mostrar(self):
		arbol = "ListaParam"

		if self.listaParam == None:
			return arbol

		Nodo._tabular += 1

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += ","

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += str(self.tipo)

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += str(self.identificador)

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"
		
		arbol += self.listaParam.mostrar()

		Nodo._tabular -= 1
		return arbol
		


class BloqFunc(Nodo):
	"""docstring for BloqFunc"""
	def __init__(self, pila, numRegla):
		pila.pop()
		pila.pop() #Quita el '}'
		pila.pop()
		self.defLocales = pila.pop().getNodo()
		pila.pop()
		pila.pop() #Quita el '{'

	def mostrar(self):
		arbol = "BloqFunc"

		Nodo._tabular += 1

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"
		
		arbol += self.defLocales.mostrar()

		Nodo._tabular -= 1
		return arbol
		
class DefLocales(Definicion):
	"""docstring for DefLocales"""
	def __init__(self, pila, numRegla):
		if numRegla == 15:
			self.defLocal = None
			self.defLocales = None

		elif numRegla == 16:
			pila.pop()
			self.defLocales = pila.pop().getNodo()
			pila.pop()
			self.defLocal = pila.pop().getNodo()

	def mostrar(self):
		arbol = "DefLocales"

		if self.defLocal == None:
			return arbol

		Nodo._tabular += 1

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += ","

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += self.defLocal.mostrar()

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += self.defLocales.mostrar()

		Nodo._tabular -= 1
		return arbol
		

class DefLocal(Definicion):
	"""docstring for DefLocal"""
	def __init__(self, pila, numRegla):
		pila.pop()
		self.defVar_Sentencia = pila.pop().getNodo()

	def mostrar(self):
		arbol = "DefLocal"

		Nodo._tabular += 1

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += self.defVar_Sentencia.mostrar()

		Nodo._tabular -= 1
		return arbol
		
class Sentencias(Nodo):
	"""docstring for Sentencia"""
	def __init__(self, pila, numRegla):
		if numRegla == 19:
			self.sentencia = None
			self.sentencias = None

		elif numRegla == 20:
			pila.pop()
			self.sentencias = pila.pop().getNodo()
			pila.pop()
			self.sentencia = pila.pop().getNodo()
	
	def mostrar(self):
		arbol = "Sentencias"

		if self.sentencia == None:
			return arbol

		Nodo._tabular += 1

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += self.sentencia.mostrar()

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += self.sentencias.mostrar()

		_tabular -= 1
		return arbol

class Sentencia(Nodo):
	"""docstring for Sentencia"""
	def __init__(self, pila, numRegla):
		self.numRegla = numRegla
		if numRegla == 21:
			pila.pop()
			pila.pop() #Quita el ';'
			pila.pop()
			self.expresion = pila.pop().getNodo()
			pila.pop()
			pila.pop() #Quita el '='
			pila.pop()
			self.identificador = pila.pop().getSimbolo()

		elif numRegla == 22:
			pila.pop()
			self.otro = pila.pop().getNodo()
			pila.pop()
			self.sentenciaBloque = pila.pop().getNodo()
			pila.pop()
			pila.pop() # Quita el ')'
			pila.pop()
			self.expresion = pila.pop().getNodo()
			pila.pop()
			pila.pop() # Quita el '('
			pila.pop()
			self.If = pila.pop().getSimbolo()

		elif numRegla == 23:
			pila.pop()
			self.bloque = pila.pop().getNodo()
			pila.pop()
			pila.pop() #Quita el ')'
			pila.pop()
			self.expresion = pila.pop().getNodo()
			pila.pop()
			pila.pop() #Quita el '('
			pila.pop()
			self.While = pila.pop().getSimbolo()

		elif numRegla == 24:
			pila.pop()
			pila.pop() #Quita el ';'
			pila.pop()
			self.valorRegresa = pila.pop().getNodo()
			pila.pop()
			self.Return = pila.pop().getSimbolo()

		elif numRegla == 25:
			pila.pop()
			pila.pop() #Quita el ';'
			pila.pop()
			self.llamadaFunc = pila.pop().getNodo()

	def mostrar(self):
		arbol = "Sentencia"

		Nodo._tabular += 1

		if self.numRegla == 21:
			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += str(self.identificador)

			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += "="


			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += self.expresion.mostrar()

			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += ";"

		elif self.numRegla == 22:
			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += str(self.If)

			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += "("

			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += self.expresion.mostrar()

			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += ")"

			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += self.sentenciaBloque.mostrar()

			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += self.otro.mostrar()


		elif self.numRegla == 23:
			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += str(self.While)

			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += "("

			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += self.expresion.mostrar()

			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += ")"

			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += self.bloque.mostrar()

		elif self.numRegla == 24:
			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += str(self.Return)

			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += self.valorRegresa.mostrar()

			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += ";"


		elif self.numRegla == 25:
			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += self.llamadaFunc.mostrar()

			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += ";"

		Nodo._tabular -= 1
		return arbol

class Otro(Nodo):
	"""docstring for Otro"""
	def __init__(self, pila, numRegla):
		if numRegla == 26:
			self.Else = ""
			self.sentenciaBloque = None

		elif numRegla == 27:
			pila.pop()
			self.sentenciaBloque = pila.pop().getNodo()
			pila.pop()
			self.Else = pila.pop().getSimbolo()

	def mostrar(self):
		arbol = "Otro"

		if sentenciaBloque == None:
			return arbol

		Nodo._tabular += 1

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += str(self.Else)

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += self.sentenciaBloque.mostrar()

		Nodo._tabular -= 1
		return arbol

	
class Bloque(Nodo):
	"""docstring for Bloque"""
	def __init__(self, pila, numRegla):
		pila.pop()
		pila.pop() #Quita el '}'
		pila.pop()
		self.sentencias = pila.pop().getNodo()
		pial.pop()
		pila.pop() #Quita el '{'
	
	def mostrar(self):
		arbol = "Bloque"

		Nodo._tabular += 1

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += "{"

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += self.sentencias.mostrar()

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += "}"

		Nodo._tabular -= 1
		return arbol


class ValorRegresa(Nodo):
	"""docstring for ValorRegresa"""
	def __init__(self, pila, numRegla):
		if numRegla == 29:
			self.expresion = None

		elif numRegla == 30:
			pila.pop()
			self.expresion = pila.pop().getNodo()

	def mostrar(self):
		arbol = "ValorRegresa"

		if self.expresion == None:
			return arbol

		Nodo._tabular += 1

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += self.expresion.mostrar()

		Nodo._tabular -= 1
		return arbol
		
		
class Argumentos(Nodo):
	"""docstring for Argumentos"""
	def __init__(self, pila, numRegla):
		if numRegla == 31:
			self.expresion = None
			self.listaArgumentos = None

		elif numRegla == 32:
			pila.pop()
			self.expresion = pila.pop().getNodo()
			pila.pop()
			self.listaArgumentos = pila.pop().getNodo()

	def mostrar(self):
		arbol = "Argumentos"

		if self.expresion == None:
			return arbol

		Nodo._tabular += 1

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += self.expresion.mostrar()

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += self.listaArgumentos.mostrar()

		Nodo._tabular -= 1
		return arbol
		


class ListaArgumentos(Nodo):
	"""docstring for ListaArgumentos"""
	def __init__(self, pila, numRegla):
		if numRegla == 33:
			self.expresion = None
			self.listaArgumentos = None

		elif numRegla == 34:
			pila.pop()
			self.listaArgumentos = pila.pop().getNodo()
			pila.pop()
			self.expresion = pila.pop().getNodo()
			pila.pop()
			pila.pop() #Quita la ','

	def mostrar(self):
		arbol = "ListaArgumentos"

		if self.expresion == None:
			return arbol

		Nodo._tabular += 1

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += self.expresion.mostrar()

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += self.listaArgumentos.mostrar()

		Nodo._tabular -= 1
		return arbol


class Termino(Nodo):
	"""docstring for Termino"""
	def __init__(self, pila, numRegla):
		pila.pop()

		if numRegla == 35:
			self.llamadaFunc = pila.pop().getNodo()

		else:
			print("AQUI")
			self.terminal = pila.pop().getSimbolo()
			self.llamadaFunc = None
		
	def mostrar(self):
		arbol = "Termino"

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		if self.llamadaFunc != None:
			arbol += self.llamadaFunc.mostrar()

		else:
			arbol += str(self.terminal)

		return arbol



class LlamadaFunc(Nodo):
	"""docstring for LlamadaFunc"""
	def __init__(self, pila, numRegla):
		pila.pop()
		pila.pop() #Quita el ')'
		pila.pop()
		self.argumentos = pila.pop().getNodo()
		pila.pop()
		pila.pop() #Quita el '('
		pila.pop()
		self.identificador = pila.pop().getSimbolo()

	def mostrar(self):
		arbol = "LlamadaFunc"

		Nodo._tabular += 1

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += str(self.identificador)

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += "("

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += self.argumentos.mostrar()

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += ")"

		Nodo._tabular -= 1
		return arbol


class SentenciaBloque(Nodo):
	"""docstring for SentenciaBloque"""
	def __init__(self, pila, numRegla):
		pila.pop()
		self.sentencia_bloque = pila.pop().getNodo()

	def mostrar(self):
		arbol = "SentenciaBloque"

		Nodo._tabular += 1

		arbol += "\n"
		for x in range(1,Nodo._tabular):
			arbol += "\t"

		arbol += self.sentencia_bloque.mostrar()

		Nodo._tabular -= 1
		return arbol
	
class Expresion(Nodo):
	"""docstring for Expresion"""
	def __init__(self, pila, numRegla):
		self.numRegla = numRegla
		
		pila.pop()

		if numRegla == 43:
			pila.pop() #Quita el ')'
			pila.pop()
			self.expresion = pila.pop().getNodo()
			pila.pop()
			pila.pop() #Quita el '('

		elif numRegla == 44 or numRegla == 45:
			self.expresion = pila.pop().getNodo()
			pila.pop()
			self.operador = pila.pop().getSimbolo()

		elif numRegla == 52:
			self.termino = pila.pop().getNodo()

		else:
			self.expresionDer = pila.pop().getNodo()
			pila.pop()
			self.operador = pila.pop().getSimbolo()
			pila.pop()
			self.expresionIzq = pila.pop().getNodo()



	def mostrar(self):
		arbol = "Expresion"
		Nodo._tabular += 1

		if self.numRegla == 43:
			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += "("

			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += self.expresion.mostrar()

		elif self.numRegla == 44 or self.numRegla == 45:
			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += str(self.operador)

			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += self.expresion.mostrar()

		elif self.numRegla == 52:
			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += self.termino.mostrar()
			
		else:
			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += self.expresionIzq.mostrar()

			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += str(self.operador)

			arbol += "\n"
			for x in range(1,Nodo._tabular):
				arbol += "\t"

			arbol += self.expresionDer.mostrar()

		Nodo._tabular -= 1
		return arbol
			

class Error(Nodo):
	"""docstring for Error"""

	def mostrar(self):
		return "Error, arbol inconcluso."