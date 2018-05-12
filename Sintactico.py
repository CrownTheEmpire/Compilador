from Lexico import Lexico
from Lexico import TipoSimbolo
from Pila import Pila
from Pila import Terminal
from Pila import NoTerminal
from Pila import Estado
from ArbolSintactico import *


class Sintactico:
    def __init__(self):
        self.__lexico = Lexico()
        self.__pila = Pila()
        self.__nodoArbol = None
        self.__reglas = []
        self.__idReglas = []
        self.__lonReglas = []
        self.__tablaLR = []

    def getLexico(self):
        return self.__lexico  

    def getPila(self):
        return self.__pila

    def getNodoArbol(self):
        return self.__nodoArbol

    def getReglas(self):
        return self.__reglas

    def getIdReglas(self):
        return self.__idReglas

    def getLonReglas(self):
        return self.__lonReglas

    def getTablaLR(self):
        return self.__tablaLR

    def cargarGramatica(self, nombreArchivo):
        lineas = []
        try:
            f = open(nombreArchivo)
            lineas = f.readlines()
            f.close()
        
        except:
            print("Error de lectura, archivo no disponible.")

        lim = int(lineas[0]) #Obtener el numero de reglas; indicado en la primera linea del archivo

        #Recuperar los datos de las reglas; iterar segun la cantidad de reglas.
        i = 1
        while i <= lim:
            #print("cadena[",i,"]",listaCadenas[i])
            linea = lineas[i].split()
            #print("linea:", linea)
            self.__idReglas.append(linea[0]) #la primera columna contiene el "id" de la regla.
            self.__lonReglas.append(linea[1]) #la segunda columna contiene la "longitud" de la regla.
            self.__reglas.append(linea[2]) #la tercer columna contiene la regla
            i += 1

        #Despues de leer las reglas, obtener la cantidad de filas y columnas contenida en la siguiente
        # linea, es decir: donde se quedo el iterador
        filas = lineas[i].split()[0] #numero de filas contenido en la primera columna
        columnas = lineas[i].split()[1] #numero de columnas contenido en la segunda columna

        #Obtener la tabla LR contenida en el resto del archivo
        i += 1
        while i < len(lineas):
            fila = lineas[i].split()
            #print("fila[",i-lim-2,"] =", fila)
            self.__tablaLR.append(fila)
            i += 1


    def analizar(self):
        if len(self.__reglas) == 0:
            return -1, "Error, no existe Gramatica"

        #Preparar la pila
        pila = Pila()
        fila = 0
        columna = 0
        accion = 0
        aceptacion = False
    
        #Establecer la cadena de entrada
        #self.__lexico = Lexico("void funcionA(){ } \n int funcionB(float suma){  }")

        #Adecuar la pila
        pila.push(Terminal(TipoSimbolo._tipoInt['$'], "$"))
        pila.push(Estado(0))
    
        #solicitar el simbolo al Lexico
        self.__lexico.sigSimbolo()

        raiz = Nodo()

        #verificar si el simbolo en pila.top() tiene un desplazamiento o transicion con
        #respecto a lexico.tipo conforme a la tablaLR
        while not aceptacion:
            fila = pila.top().getId()
            columna = self.__lexico.tipo
            accion = int(self.__tablaLR[fila][columna]) #Hacer que el vector almacene enteros!!!
        
            print()
            print("entrada:", self.__lexico.simbolo)
            print("pila:", end = " ")
            pila.muestra()
            print()
            print("accion:", accion, "Tipo:", self.__lexico.tipo)
        
            if accion > 0:
                pila.push( Terminal(self.__lexico.tipo, self.__lexico.simbolo) ) #Terminal self.lexico.simbolo
                pila.push( Estado(accion) ) #Estado
                
                #solicitar el simbolo al Lexico
                self.__lexico.sigSimbolo()
            
            elif accion < 0:
                if accion == -1:
                    aceptacion = True
                    pila.pop()
                    self.__nodoArbol = pila.pop().getNodo()
                    break
                    
                regla = (-1) * (accion + 2)
                #print("REGLA:", regla+1, self.__reglas[regla])
                #print("Longitud:", self.__lonReglas[regla])


                #i = 0;
                """while i < int(self.__lonReglas[regla]): #Hacer que el vector almacene enteros!!!
                    pila.pop() #quita el Estado
                    pila.pop() #quita el Terminal o el NoTerminal
                    i += 1
                print("pop *", i * 2)"""

                nodoArbol = self.crearNodo(regla+1, pila)
                
                #sigue una transicion, se calcula entonces
                fila = pila.top().getId()
                columna = self.__idReglas[regla]
                accion = int(self.__tablaLR[int(fila)][int(columna)]) #Hacer que el vector almacene enteros!!!
    
                #Se realiza la transicion
                noTerminal = NoTerminal(regla, self.__lexico.simbolo) #, self.__reglas[regla]
                noTerminal.setNodo(nodoArbol)
                pila.push( noTerminal )
                pila.push( Estado(accion) )
    
            else:
                break
            
            #input("...")

##        print("*******", nodoArbol)
        
        
        if aceptacion:
            return (1, "Aceptado")
            
        else:
            self.__nodoArbol = Error()
            return (0, "No aceptado")
    
    def crearNodo(self, numero, pila):
        print("numero VALE: ", numero)
        if numero == 1:
            return Programa(pila, numero)

        elif numero == 2 or numero == 3:
            return Definiciones(pila, numero)

        elif numero == 4 or numero == 5:
            return Definicion(pila, numero)

        elif numero == 6:
            return DefVar(pila, numero)

        elif numero == 7:
            return ListaVar(pila, numero)

        elif numero == 8:
            return ListaVar(pila, numero)

        elif numero == 9:
            return DefFunc(pila, numero)

        elif numero == 10 or numero == 11:
            return Parametros(pila, numero)
        
        elif numero == 12 or numero == 13:
            return ListaParam(pila, numero)

        elif numero == 14:
            return BloqFunc(pila, numero)

        elif numero == 15 or numero == 16:
            return DefLocales(pila, numero)

        elif numero == 17 or numero == 18:
            return DefLocal(pila, numero)

        elif numero == 19 or numero == 20:
            return Sentencias(pila, numero)

        elif numero == 21:
            return Sentencia(pila, numero)

        elif numero == 22:
            return Sentencia(pila, numero)

        elif numero == 23:
            return Sentencia(pila, numero)

        elif numero == 24:
            return Sentencia(pila, numero)

        elif numero == 25:
            return Sentencia(pila, numero)

        elif numero == 26 or numero == 27:
            return Otro(pila, numero)

        elif numero == 28:
            return Bloque(pila, numero)

        elif numero == 29 or numero == 30:
            return ValorRegresa(pila, numero)

        elif numero == 31 or numero == 32:
            return Argumentos(pila, numero)

        elif numero == 33 or numero == 34:
            return ListaArgumentos(pila, numero)

        elif numero == 35:
            return Termino(pila,numero)

        elif numero == 36:
            return Termino(pila,numero)

        elif numero == 37:
            return Termino(pila,numero)

        elif numero == 38:
            return Termino(pila,numero)

        elif numero == 39:
            return Termino(pila,numero)

        elif numero == 40:
            return LlamadaFunc(pila, numero)

        elif numero == 41 or numero == 42:
            return SentenciaBloque(pila, numero)

        elif numero == 43:
            return Expresion(pila, numero)

        elif numero == 44:
            return Expresion(pila, numero)

        elif numero == 45:
            return Expresion(pila, numero)

        elif numero == 46:
            return Expresion(pila, numero)

        elif numero == 47:
            return Expresion(pila, numero)

        elif numero == 48:
            return Expresion(pila, numero)

        elif numero == 49:
            return Expresion(pila, numero)

        elif numero == 50:
            return Expresion(pila, numero)

        elif numero == 51:
            return Expresion(pila, numero)

        elif numero == 52:
            return Expresion(pila, numero)

        return None 


s = Sintactico()
s.cargarGramatica("compilador.lr")

"""s.getReglas()
s.getIdReglas()
s.getLonReglas()
s.getTablaLR()"""

s.getLexico().setEntrada("void main() { int a, b, c;  a = 3; b = c - (4 * a); } int hola(float msg){ print(msg); } float retorno(){ return 0.0; }")

print(s.analizar())
print(s.getNodoArbol().mostrar())