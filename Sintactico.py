from Lexico import Lexico
from Pila import Pila

class Sintactico:
    def __init__(self):
        self.__lexico = Lexico();
        self.__reglas = []
        self.__idReglas = []
        self.__lonReglas = []
        self.__tablaLR = []

    def getLexico(self):
        return self.__lexico                                                                       

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
        aceptacion = 0
    
        #Establecer la cadena de entrada
        #self.__lexico = Lexico("void funcionA(){ } \n int funcionB(float suma){  }")

        #Adecuar la pila
        pila.push('$')
        pila.push(0)
    
        #solicitar el simbolo al Lexico
        self.__lexico.sigSimbolo()
        #verificar si el simbolo en pila.top() tiene un desplazamiento o transicion con
        #respecto a lexico.tipo conforme a la tablaLR
    
        while not aceptacion:
            fila = pila.top()
            columna = self.__lexico.tipo
            accion = int(self.__tablaLR[fila][columna]) #Hacer que el vector almacene enteros!!!
        
        
            print()
            print("entrada:", self.__lexico.simbolo)
            print("pila:", end = " ")
            pila.muestra()
            print()
            print("accion:", accion, "Tipo:", self.__lexico.tipo)
        
            if accion > 0:
                pila.push(self.__lexico.simbolo)
                pila.push(accion)
                
                #solicitar el simbolo al Lexico
                self.__lexico.sigSimbolo()
            
            elif accion < 0:
                if accion == -1:
                    aceptacion = 1
                    break
                    
                regla = (-1) * (accion + 2)
                print("REGLA:", regla+1)
                print("Longitud:", self.__lonReglas[regla])
    
                i = 0;
                while i < int(self.__lonReglas[regla]): #Hacer que el vector almacene enteros!!!
                    pila.pop()
                    pila.pop()
                    i += 1
                print("pop *", i * 2)
                    
                #sigue una transicion, se calcula entonces
                fila = pila.top()
                columna = self.__idReglas[regla]
                accion = int(self.__tablaLR[int(fila)][int(columna)]) #Hacer que el vector almacene enteros!!!
    
                #Se realiza la transicion
                pila.push(self.__reglas[regla])
                pila.push(accion)
    
            else:
                break
    
            #input("...")
        
        
        if aceptacion:
            return (1, "Aceptado")
            
        else:
            return (0, "No aceptado.")
            

"""s = Sintactico()
s.cargarGramatica("compilador.lr")

print(s.getReglas())
print(s.getIdReglas())
print(s.getLonReglas())
print(s.getTablaLR())

s.analizar()"""
    