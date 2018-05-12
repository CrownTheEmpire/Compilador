from Pila import Pila
from Lexico import Lexico
from Sintactico import Sintactico

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
    print ("pila: ", end=" ")
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
    
def ejercicio2():
    idReglas = [3, 3] #la regla E, se encuentra especificada en la columna 3
    #la primera regla E -> <id>+E, tiene una longitud de 3
    #la segunda regla E -> <id>, tiene una longitud de 1
    lonReglas = [3, 1]
    tablaLR =  {(0,Lexico._tiposInt['IDENTIFICADOR']): 2,
                (0,3): 1,
                (1,Lexico._tiposInt['$']): -1,
                (2,Lexico._tiposInt['OPSUMA']): 3,
                (2,Lexico._tiposInt['$']): -3,
                (3,Lexico._tiposInt['IDENTIFICADOR']): 2,
                (3,3): 4,
                (4,Lexico._tiposInt['$']): -2}
    
    
    #Preparar la pila
    pila = Pila()
    fila = 0
    columna = 0
    accion = 0
    aceptacion = 0
    
    #Establecer la cadena de entrada
    lexico = Lexico("alpha + betha - delta")

    #Adecuar la pila
    pila.push(Lexico._tiposInt['$'])
    pila.push(0);
    
    #solicitar el simbolo al Lexico "a"
    lexico.sigSimbolo()
    #verificar si el simbolo en pila.top() tiene un desplazamiento o transicion con
    #respecto a lexico.tipo conforme a la tablaLR
    
    while not aceptacion:  
        
        fila = pila.top()
        columna = lexico.tipo
        accion = tablaLR.get((fila,columna), 0)
        
        #aceptacion = accion == -1
        
        print()
        print("entrada:", lexico.simbolo)
        print("pila:", end = " ")
        pila.muestra()
        print()
        print("accion:", accion, "Tipo:", lexico.tipo)
        
        if accion > 0:
            pila.push(lexico.tipo)
            pila.push(accion)
            
            #solicitar el simbolo al Lexico
            lexico.sigSimbolo()
        
        elif accion < 0:
            if accion == -1:
                aceptacion = 1
                break
                
            regla = (-1) * (accion + 2)
            print("REGLA:", regla+1)
            print("Longitud:", lonReglas[regla])
            """for cantidad in range(lonReglas[regla]):
                pila.pop()
                pila.pop()"""
            i = 0;
            while i < lonReglas[regla]:
                pila.pop()
                print("pop")
                pila.pop()
                print("pop")
                i += 1
                
            #sigue una transicion, se calcula entonces
            #print("idRegla:", idReglas[regla])
            fila = pila.top()
            #print("fila:", fila)
            columna = idReglas[regla]
            #print("ACCION:", tablaLR.get((fila, columna),0))
            accion = tablaLR.get((fila, columna),0)

            #Se realiza la transicion
            pila.push(idReglas[regla])
            pila.push(accion)

        else:
            break

        input("...")
    
        
    if aceptacion:
        print ("ACEPTADO")
        
    else:
        print ("ERROR")

def ejercicio3():
    Reglas = ["E", "E"]
    idReglas = [3, 3] #la regla E, se encuentra especificada en la columna 3
    #la primera regla E -> <id>+E, tiene una longitud de 3
    #la segunda regla E -> <id>, tiene una longitud de 1
    lonReglas = [3, 1]
    tablaLR =  {(0,Lexico._tiposInt['IDENTIFICADOR']): 2,
                (0,3): 1,
                (1,Lexico._tiposInt['$']): -1,
                (2,Lexico._tiposInt['OPSUMA']): 3,
                (2,Lexico._tiposInt['$']): -3,
                (3,Lexico._tiposInt['IDENTIFICADOR']): 2,
                (3,3): 4,
                (4,Lexico._tiposInt['$']): -2}
    
    
    #Preparar la pila
    pila = Pila()
    fila = 0
    columna = 0
    accion = 0
    aceptacion = 0
    
    #Establecer la cadena de entrada
    lexico = Lexico("alpha + betha - delta")

    #Adecuar la pila
    pila.push('$')
    pila.push(0);
    
    #solicitar el simbolo al Lexico "a"
    lexico.sigSimbolo()
    #verificar si el simbolo en pila.top() tiene un desplazamiento o transicion con
    #respecto a lexico.tipo conforme a la tablaLR
    
    while not aceptacion:  
        
        fila = pila.top()
        columna = lexico.tipo
        accion = tablaLR.get((fila,columna), 0)
        
        #aceptacion = accion == -1
        
        print()
        print("entrada:", lexico.simbolo)
        print("pila:", end = " ")
        pila.muestra()
        print()
        print("accion:", accion, "Tipo:", lexico.tipo)
        
        if accion > 0:
            pila.push(lexico.simbolo)
            pila.push(accion)
            
            #solicitar el simbolo al Lexico
            lexico.sigSimbolo()
        
        elif accion < 0:
            if accion == -1:
                aceptacion = 1
                break
                
            regla = (-1) * (accion + 2)
            print("REGLA:", regla+1)
            print("Longitud:", lonReglas[regla])

            i = 0;
            while i < lonReglas[regla]:
                pila.pop()
                print("pop")
                pila.pop()
                print("pop")
                i += 1
                
            #sigue una transicion, se calcula entonces
            #print("idRegla:", idReglas[regla])
            fila = pila.top()
            #print("fila:", fila)
            columna = idReglas[regla]
            #print("ACCION:", tablaLR.get((fila, columna),0))
            accion = tablaLR.get((fila, columna),0)

            #Se realiza la transicion
            pila.push(Reglas[regla])
            pila.push(accion)

        else:
            break

        input("...")
    
        
    if aceptacion:
        print ("ACEPTADO")
        
    else:
        print ("ERROR")
    
    
#ejemplo1()
#ejemplo2()
#ejemplo3()
#ejercicio1()
#ejercicio2()
#ejercicio3()

try:
    f = open("entrada.txt")
    entrada = f.read()
    f.close()
        
except:
    print("Error de lectura, archivo de entrada no disponible.")
    exit(0)

s = Sintactico()
s.getLexico().setEntrada(entrada)
s.cargarGramatica("compilador.lr")
print(s.getReglas())
r = s.analizar()
print(r);

