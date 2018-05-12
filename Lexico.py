class Lexico:
    #Comprobar la adicion de esta linea en el Hub, y verificar el comportamiento de la rama actual y la 'master'
    _tiposInt = {'ERROR': -1, 'IDENTIFICADOR': 0, 'ENTERO': 1, 'REAL': 2,
                 'CADENA': 3, 'TIPO': 4, 'OPSUMA': 5, 'OPMUL': 6, 'OPRELAC': 7,
                 'OPOR': 8, 'OPAND': 9, 'OPNOT': 10, 'OPIGUALDAD': 11, ';': 12,
                 ',': 13, '(': 14, ')': 15, '{': 16, '}': 17, '=': 18, 'if': 19,
                 'while': 20, 'return': 21, 'else': 22, '$': 23}
    
    _tiposCad = {-1: 'ERROR', 0: 'IDENTIFICADOR', 1: 'ENTERO', 2: 'REAL',
                 3: 'CADENA', 4: 'TIPO', 5: 'OPSUMA', 6: 'OPMUL', 7: 'OPRELAC',
                 8: 'OPOR', 9: 'OPAND', 10: 'OPNOT', 11: 'OPIGUALDAD', 12: ';',
                 13: ',', 14: '(', 15: ')', 16: '{', 17: '}', 18: '=', 19: 'if',
                 20: 'while', 21: 'return', 22: 'else', 23: '$'}
    
    #constructor
    def __init__(self, fuente=""):
        #Privadas
        self.__fuente = fuente
        self.__ind = 0
        self.__continua = 0
        self.__c = ''
        self.__estado = 0

        #Publicas
        self.simbolo = ""
        self.tipo = 0
        
    #Metodos privados
    def __sigCaracter(self):
        if self.terminado():
            return '$'

        caracter = self.__fuente[self.__ind]
        self.__ind += 1
        return caracter

    def __sigEstado(self, estado):
        self.__estado = estado
        self.simbolo += self.__c
        
    def __aceptacion(self, estado):
        self.__sigEstado(estado)
        self.__continua = 0

    def __esLetra(self, c):
        return c.isalpha() or c == "_"

    def __esDigito(self, c):
        return c.isdigit()

    def __esEspacio(self, c):
        return c.isspace()

    #Verificar retroceso cuando se llegue al final de la entrada
    def __retroceso(self):
        if self.__c != '$':
            self.__ind -= 1
            
        self.__continua = 0

    #Metodos publicos
    def setEntrada(self, fuente):
        self.__fuente = fuente
        

    def tipoAcad(self, tipo):
        return self._tiposCad[tipo]
        
    def sigSimbolo(self):
        self.__estado = 0
        self.__continua = 1
        self.simbolo = ""

        #inicio del automata
        while self.__continua:
            
            self.__c = self.__sigCaracter()

            if self.__estado == 0:
                if self.__esLetra(self.__c):
                    self.__sigEstado(1)

                elif self.__esDigito(self.__c):
                    self.__sigEstado(2)

                
                elif self.__c == '+' or self.__c == '-':
                    self.__aceptacion(self._tiposInt['OPSUMA'])

                elif self.__c == '*' or self.__c == '/':
                    self.__aceptacion(self._tiposInt['OPMUL'])

                elif self.__c == '=':
                    self.__sigEstado(7)

                elif self.__c == '<' or self.__c == '>':
                    self.__sigEstado(9)

                elif self.__c == '!':
                    self.__sigEstado(11)

                elif self.__c == '&':
                    self.__sigEstado(13)

                elif self.__c == '|':
                    self.__sigEstado(15)

                elif self.__c == '(':
                    self.__aceptacion(self._tiposInt['('])

                elif self.__c == ')':
                    self.__aceptacion(self._tiposInt[')'])

                elif self.__c == '{':
                    self.__aceptacion(self._tiposInt['{'])

                elif self.__c == '}':
                    self.__aceptacion(self._tiposInt['}'])

                elif self.__c == ';':
                    self.__aceptacion(self._tiposInt[';'])

                elif self.__c == ',':
                    self.__aceptacion(self._tiposInt[','])

                elif self.__c == '"':
                    self.__sigEstado(20)

                elif self.__c == '$':
                    self.__aceptacion(self._tiposInt['$'])

                elif self.__esEspacio(self.__c):
                    #Ignorar los espacios en blanco; hacer nada.
                    pass

                else:
                    self.__aceptacion(self._tiposInt['ERROR'])

            elif self.__estado == 1:
                if self.__esLetra(self.__c) or self.__esDigito(self.__c):
                    self.__sigEstado(1)

                else:
                    self.__estado = self._tiposInt['IDENTIFICADOR']
                    self.__continua = 0
                    self.__retroceso()
                    

            elif self.__estado == 2:
                if self.__esDigito(self.__c):
                    self.__sigEstado(2)

                elif self.__c == '.':
                    self.__sigEstado(3)

                elif self.__esLetra(self.__c):
                    self.__aceptacion(self._tiposInt['ERROR'])

                else:
                    self.__estado = self._tiposInt['ENTERO']
                    self.__continua = 0
                    self.__retroceso()
                    
            elif self.__estado == 3:
                if self.__esDigito(self.__c):
                    self.__sigEstado(4)

                else:
                    self.__aceptacion(self._tiposInt['ERROR'])

            elif self.__estado == 4:
                if self.__esDigito(self.__c):
                    self.__sigEstado(4)

                elif self.__esLetra(self.__c):
                    self.__aceptacion(self._tiposInt['ERROR'])

                else:
                    self.__estado = self._tiposInt['REAL']
                    self.__continua = 0
                    self.__retroceso()

            elif self.__estado == 7:
                if self.__c == '=':
                    self.__aceptacion(self._tiposInt['OPIGUALDAD'])

                else:
                    self.__estado = self._tiposInt['=']
                    self.__continua = 0
                    self.__retroceso()

            elif self.__estado == 9:
                if self.__c == '=':
                    self.__aceptacion(self._tiposInt['OPRELAC'])

                else:
                    self.__estado = self._tiposInt['OPRELAC']
                    self.__continua = 0
                    self.__retroceso()

            elif self.__estado == 11:
                if self.__c == '=':
                    self.__aceptacion(self._tiposInt['OPIGUALDAD'])

                else:
                    self.__estado = self._tiposInt['OPNOT']
                    self.__continua = 0
                    self.__retroceso()

            elif self.__estado == 13:
                if self.__c == '&':
                    self.__aceptacion(self._tiposInt['OPAND'])

                else:
                    self.__aceptacion(self._tiposInt['ERROR'])

            elif self.__estado == 15:
                if self.__c == '|':
                    self.__aceptacion(self._tiposInt['OPOR'])

                else:
                    self.__aceptacion(self._tiposInt['ERROR'])

            elif self.__estado == 20:
                if self.terminado():
                    self.__aceptacion(self._tiposInt['ERROR'])
                
                if self.__c != '"' :
                    self.__sigEstado(20)

                else:
                    self.__estado = self._tiposInt['CADENA']
                    self.__continua = 0
                    #self.__retroceso()
                    
            
            else:
                self.__aceptacion(self._tiposInt['ERROR'])

        
        if self.simbolo == "if":
            self.__estado = self._tiposInt['if']

        elif self.simbolo == "else":
            self.__estado = self._tiposInt['else']

        elif self.simbolo == "while":
            self.__estado = self._tiposInt['while']

        elif self.simbolo == "return":
            self.__estado = self._tiposInt['return']

        elif self.simbolo == "int" or self.simbolo == "float" or self.simbolo == "void":
            self.__estado = self._tiposInt['TIPO']
        
        self.tipo = self.__estado
        return self.simbolo, self._tiposCad[self.__estado], self.tipo 

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


"""l = Lexico("int, float, void,  return;")
while not l.terminado():
    print(l.sigSimbolo())"""