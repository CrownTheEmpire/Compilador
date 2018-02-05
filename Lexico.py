class Lexico:
    _tiposInt = {'ERROR': -1, 'IDENTIFICADOR': 0, 'OPADIC': 1, 'OPMULT': 2, 'PESOS': 3, 'ENTERO': 4}
    _tiposCad = {-1:'ERROR', 0: 'IDENTIFICADOR', 1: 'OPADIC', 2: 'OPMULT', 3: 'PESOS', 4: 'ENTERO'}
    
    #constructor
    def __init__(self, fuente=""):
        #Privadas
        self.__fuente = fuente
        self.__ind = 0
        self.__continua = 0
        self.__c = ''
        self.__estado = 0

        #publicas
        self.simbolo = ""
        self.tipo = 0
        
    #Metodos privados
    def __sigCaracter(self):
        if self.terminado():
            return '$'

        caracter = self.__fuente[self.__ind]
        self.__ind = self.__ind + 1
        return caracter

    def __sigEstado(self, estado):
        self.__estado = estado
        self.simbolo += self.__c
        
    def __aceptacion(self, estado):
        self.__sigEstado(estado)
        self.__continua = 0
        #print("Esto es: ", self.__estado, " y: ", self.__continua)

    def __esLetra(self, c):
        return c.isalpha() or c == "_"

    def __esDigito(self, c):
        return c.isdigit()

    def __esEspacio(self, c):
        return c.isspace()

    def __retroceso(self):
        if self.__c != '$':
            self.__ind += 1
            
        self.__continua = 0

    #Metodos publicos
    def entrada(self, fuente):
        self.__fuente = fuente
        

    def tipoAcad(self, tipo):
        self.__aceptacion(3)
        return self._tiposCad[tipo]
        
    def sigSimbolo(self):
        self.__estado = 0
        self.__continua = 1
        self.simbolo = ""

        #inicio del automata
        while self.__continua:
            
            self.__c = self.__sigCaracter()

            #ignorar cualquier espacio
            while self.__esEspacio(self.__c):
                self.__c = self.__sigCaracter()

            if self.__estado == 0:
                if self.__c == '+' or self.__c == '-':
                    self.__aceptacion(self._tiposInt['OPADIC'])

                elif self.__c == '*' or self.__c == '/':
                    self.__aceptacion(self._tiposInt['OPMULT'])

                elif self.__c == '$':
                    self.__aceptacion(self._tiposInt['PESOS'])

                else:
                    self.__aceptacion(self._tiposInt['ERROR'])

            elif self.__estado == 1:
                pass

            elif self.__estado == 3:
                pass

            elif self.__estado == 4:
                pass

            else:
                self.__aceptacion(self._tiposInt['ERROR'])

        #para test
        return self.simbolo, self._tiposCad[self.__estado]

    def terminado(self):
        return self.__ind >= len(self.__fuente)

    #cisma
    
    def getFuente(self):
        return self.__fuente

    def getInd(self):
        return self.__ind

    def getContinua(self):
        return self.__continua

    def getC(self):
        return self.__c

    def getEstado(self):
        return self.__estado
        

l = Lexico("+ *          f    / \t -")
print (l.sigSimbolo())
print (l.sigSimbolo())
print (l.sigSimbolo())
print (l.sigSimbolo())
print (l.sigSimbolo())
input('wut?')
