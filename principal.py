from Pila import Pila
from Lexico import Lexico

def ejemplo1():
    pila = Pila()

    pila.push(2)
    pila.push(3)
    pila.push(4)
    pila.push(5)
    pila.muestra()
    print ()
    print (pila.top())
    print (pila.top())
    print (pila.pop())
    print (pila.pop())

def ejemplo2():
    lexico = Lexico("+-+")
    while not lexico.terminado():
        lexico.sigSimbolo()
        print (lexico.simbolo)

def ejemplo3():
    print()
    tablaLR =  {(0,Lexico._tiposInt['IDENTIFICADOR']): 2,
                (0,2): 1,
                (1,Lexico._tiposInt['$']): -1,
                (2,Lexico._tiposInt['$']): -2}

    #Preparar la pila
    pila = Pila()
    fila = 0
    columna = 0
    accion = 0
    aceptacion = 0
    lexico = Lexico("a")

    pila.push(Lexico._tiposInt['$'])
    pila.push(0);
    lexico.sigSimbolo()

    #para saber que accion realizar
    fila = pila.top()
    columna = lexico.tipo
    accion = tablaLR.get((fila,columna), 0)

    #mostrar lo que esta sucediendo
    print ("pila: ", end = " ")
    pila.muestra()
    print ()
    print ("lex.tipo: ", lexico.tipo)
    print ("accion: ", accion)

    pila.push (lexico.tipo)
    pila.push (accion)
    print (lexico.sigSimbolo())
    print (lexico.tipo)

    fila = pila.top()
    print("fila:", fila, "pilaTop:", pila.top())
    columna = lexico.tipo
    print("columna:", columna, "l.tipo:", lexico.tipo)
    accion = tablaLR.get((fila,columna), 0)
    print("Futari:",tablaLR.get((fila,columna), 0))

    pila.muestra()
    print()
    print ("entrada: ", lexico.simbolo)
    print ("accion: ", accion)

    pila.pop()
    pila.pop()

    fila = pila.top()
    columna = 2
    accion = tablaLR.get((fila,columna), 0)

    #transicion
    pila.push(2)
    pila.push(accion)
    pila.muestra()
    print()
    print("entrada: ", lexico.simbolo)
    print("accion: ", accion)

    fila = pila.top()
    columna = lexico.tipo
    accion = tablaLR.get((fila,columna), 0)
    
    pila.muestra()
    print()
    print("entrada: ", lexico.simbolo)
    print("accion: ", accion)
    print()
    aceptacion = accion == -1;
    if aceptacion:
        print("aceptacion")

def ejercicio1():
    tablaLR =  {(0,Lexico._tiposInt['IDENTIFICADOR']): 2,
                (0,3): 1,
                (1,Lexico._tiposInt['$']): -1,
                (2,Lexico._tiposInt['OPSUMA']): 3,
                (3,Lexico._tiposInt['IDENTIFICADOR']): 4,
                (4,Lexico._tiposInt['$']): -2}
    
    #Preparar la pila
    pila = Pila()
    fila = 0
    columna = 0
    accion = 0
    aceptacion = 0
    
    #Establecer la cadena de entrada
    lexico = Lexico("a+b")

    #Adecuar la pila
    pila.push(Lexico._tiposInt['$'])
    pila.push(0);
    #solicitar el simbolo al Lexico "a"
    lexico.sigSimbolo()
    #verificar si el simbolo en pila.top() tiene un desplazamiento o transicion con
    #respecto a lexico.tipo conforme a la tablaLR
    fila = pila.top()
    columna = lexico.tipo
    accion = tablaLR.get((fila,columna), 0)
    #sabemos que la accion va a ser d2, o sea accion = 2, numero positivo,
    #indica transicion o desplazamiento, entonces apilamos estos valores.
    pila.push(lexico.tipo)
    pila.push(accion)
    
    #Mostrar el progreso del algoritmo
    print()
    pila.muestra()
    print()
    
    
    #pedimos el siguiente simbolo "+"
    lexico.sigSimbolo()
    #verificar accion
    fila = pila.top()
    columna = lexico.tipo
    accion = tablaLR.get((fila,columna), 0)
    #sabemos que nos dara el desplazamiento 3; accion = 3, entonces apilamos
    pila.push(lexico.tipo)
    pila.push(accion)
    
    print()
    pila.muestra()
    print()
    
    #pedimos el siguiente simbolo "b"
    lexico.sigSimbolo()
    #verificar accion
    fila = pila.top()
    columna = lexico.tipo
    accion = tablaLR.get((fila,columna), 0)
    #sabemos que nos dara el desplazamiento 4; accion = 4, entonces apilamos
    pila.push(lexico.tipo)
    pila.push(accion)
    
    print()
    pila.muestra()
    print()
    
    #pedimos el siguiente simbolo "$" (llegamos al final de la entrada)
    lexico.sigSimbolo()
    #verificar accion
    fila = pila.top()
    columna = lexico.tipo
    accion = tablaLR.get((fila,columna), 0)
    #sabemos que nos dara la transicion -2; accion = -2, entonces -desapilamos-
    #Desapilaremos el doble del tamaño de la regla, la regla es E-> <id>+<id>
    #la longitud seria 3, nosotros desapilaremos 6 elementos.
    pila.pop()
    pila.pop()
    pila.pop()
    pila.pop()
    pila.pop()
    pila.pop()
    
    print()
    pila.muestra()
    print()
    
    #continuamos sin pedir el siguiente simbolo, debido a que la ultima accion fue
    #una reduccion, verificamos que accion sigue
    fila = pila.top() #seria 0
    columna = 3 #nos quedamos en la columna 3, donde esta la regla en la matriz
    accion = tablaLR.get((fila,columna), 0)
    
    print()
    pila.muestra()
    print()
    
    #la accion resulta ser una transicion, entonces apilamos
    pila.push(3)#la representacion de la regla E en la matriz
    pila.push(accion)
    
    print()
    pila.muestra()
    print()
        
    #Como lo anterior fue una transicion, continuamos sin solicitar nuevo simbolo
    fila = pila.top()
    print("fila:",fila)
    columna = lexico.tipo
    print("columna:",columna)
    accion = tablaLR.get((fila,columna),0)
    print("accion: ",accion)
    print()
    pila.muestra()
    print()
    
    #la accion resulta ser -1, es decir, aceptacion.abs
    aceptacion = accion == -1
    
    if aceptacion:
        print("Aceptado")
        
ejemplo1()
ejemplo2()
ejemplo3()
ejercicio1()