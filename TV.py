class TV:
    numTV = 0

    def __init__(self, marca: Marca, estado: bool):
        self.__marca = marca
        self.__estado = estado
        self.__canal = 1 
        self.__volumen = 1 
        self.__precio = 500  
        self.__control = None 
        TV.numTV += 1 

    def getMarca(self) -> Marca:
        return self.__marca

    def setMarca(self, marca: Marca) -> None:
        self.__marca = marca

    def getCanal(self) -> int:
        return self.__canal

    def setCanal(self, canal: int) -> None:
        if self.__estado and 1 <= canal <= 120:
            self.__canal = canal

    def getPrecio(self) -> int:
        return self.__precio

    def setPrecio(self, precio: int) -> None:
        self.__precio = precio

    def getVolumen(self) -> int:
        return self.__volumen

    def setVolumen(self, volumen: int) -> None:
        if self.__estado and 0 <= volumen <= 7:
            self.__volumen = volumen

    def getControl(self):
        return self.__control

    def setControl(self, control) -> None:
        self.__control = control

    @staticmethod
    def getNumTV() -> int:
        return TV.numTV

    @staticmethod
    def setNumTV(num: int) -> None:
        TV.numTV = num

    def turnOn(self) -> None:
        self.__estado = True

    def turnOff(self) -> None:
        self.__estado = False

    def getEstado(self) -> bool:
        return self.__estado

    def canalUp(self) -> None:
        if self.__estado and self.__canal < 120:
            self.__canal += 1

    def canalDown(self) -> None:
        if self.__estado and self.__canal > 1:
            self.__canal -= 1

    def volumenUp(self) -> None:
        if self.__estado and self.__volumen < 7:
            self.__volumen += 1

    def volumenDown(self) -> None:
        if self.__estado and self.__volumen > 0:
            self.__volumen -= 1