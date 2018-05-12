class Pila:
    def __init__(self):
        self.__lista = []

    def push(self, x):
        self.__lista.append(x)

    def pop(self):
        x = self.__lista[-1]
        del self.__lista[-1]
        return x

    def top(self):
        return self.__lista[-1]

    def muestra(self):
        i = len(self.__lista)-1
        while i >= 0:
            print (self.__lista[i], end=" ")
            i -= 1

    def __str__(self):
        return self.__lista                                                                        
            


