class Control:
    def __init__(self):
        self.__tv = None 

    def getTv(self):
        return self.__tv

    def setTv(self, tv):
        self.__tv = tv

    def enlazar(self, tv):
        self.__tv = tv
        tv.setControl(self) 
    def turnOn(self):
        if self.__tv:
            self.__tv.turnOn()

    def turnOff(self):
        if self.__tv:
            self.__tv.turnOff()

    def canalUp(self):
        if self.__tv:
            self.__tv.canalUp()

    def canalDown(self):
        if self.__tv:
            self.__tv.canalDown()

    def volumenUp(self):
        if self.__tv:
            self.__tv.volumenUp()

    def volumenDown(self):
        if self.__tv:
            self.__tv.volumenDown()

    def setCanal(self, canal: int):
        if self.__tv:
            self.__tv.setCanal(canal)

    def setVolumen(self, volumen: int):
        if self.__tv:
            self.__tv.setVolumen(volumen)
