class TV:
    numTV = 0

    def __init__(self, marca, estado: bool):
        self.__marca = marca  
        self.__estado = estado
        self.__canal = 1 
        self.__volumen = 1  
        self.__precio = 500 
        self.__control = None 
        TV.numTV += 1  

    def getMarca(self):
        return self.__marca

    def setMarca(self, marca):
        self.__marca = marca

    def getCanal(self):
        return self.__canal

    def setCanal(self, canal: int):
        if self.__estado and 1 <= canal <= 120:  # Validación de límites
            self.__canal = canal

    def getPrecio(self):
        return self.__precio

    def setPrecio(self, precio: int):
        self.__precio = precio

    def getVolumen(self):
        return self.__volumen

    def setVolumen(self, volumen: int):
        if self.__estado and 0 <= volumen <= 7:  # Validación de límites
            self.__volumen = volumen

    def getControl(self):
        return self.__control

    def setControl(self, control):
        self.__control = control

    @staticmethod
    def getNumTV():
        return TV.numTV

    @staticmethod
    def setNumTV(num: int):
        TV.numTV = num

    def turnOn(self):
        self.__estado = True

    def turnOff(self):
        self.__estado = False

    def getEstado(self):
        return self.__estado

    def canalUp(self):
        if self.__estado and self.__canal < 120:
            self.__canal += 1

    def canalDown(self):
        if self.__estado and self.__canal > 1:
            self.__canal -= 1

    def volumenUp(self):
        if self.__estado and self.__volumen < 7:
            self.__volumen += 1

    def volumenDown(self):
        if self.__estado and self.__volumen > 0:
            self.__volumen -= 1
