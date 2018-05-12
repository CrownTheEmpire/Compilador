from Lexico import TipoSimbolo
from ArbolSintactico import Nodo

class ElementoPila():
    """docstring for ElementoPila"""
    def __init__(self, simbolo = "", id = 0, nodo = None):
        self.simbolo = simbolo
        self.id = id

    def __str__(self):
        return str(self.simbolo)
        
    def esEstado(self):
        return False

    def esTerminal(self):
        return False

    def esNoTerminal(self):
        return False

    def getSimbolo(self):
        return self.simbolo

    def getId(self):
        return self.id

    def getNodo(self):
        return self.nodo

    def setNodo(self, nodo):
        self.nodo = nodo

class Estado(ElementoPila):
    """docstring for Estado"""
    def __init__(self, id):
        super(Estado, self).__init__()
        self.id = id
        self.simbolo = str(id)

    def esEstado(self):
        return True

class Terminal(ElementoPila):
    """docstring for Terminal"""
    def __init__(self, id, simbolo):
        super(Terminal, self).__init__()
        self.id = id
        self.simbolo = simbolo

    def esTerminal(self):
        return True

class NoTerminal(ElementoPila):
    """docstring for NoTerminal"""
    def __init__(self, id, simbolo):
        super(NoTerminal, self).__init__()
        self.id = id
        self.simbolo = simbolo
    
    def esNoTerminal(self):
        return True


class Pila:
    def __init__(self):
        self.__lista = []

    def push(self, elementoPila):
        self.__lista.append(elementoPila)

    def pop(self):
        elementoPila = self.__lista[-1]
        del self.__lista[-1]
        return elementoPila

    def top(self):
        return self.__lista[-1]

    def muestra(self):
        i = len(self.__lista)-1
        while i >= 0:
            print (self.__lista[i], end=" ")
            i -= 1

    def __str__(self):
        return self.__lista                                                                        
            


