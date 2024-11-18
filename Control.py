import TV;
class Control:
    def __init__(self):
        self.__tv = None  

    def getTv(self) -> TV:
        return self.__tv

    def setTv(self, tv: TV) -> None:
        self.__tv = tv

    def enlazar(self, tv: TV) -> None:
        self.__tv = tv
        tv.setControl(self)

    def turnOn(self) -> None:
        if self.__tv:
            self.__tv.turnOn()

    def turnOff(self) -> None:
        if self.__tv:
            self.__tv.turnOff()

    def canalUp(self) -> None:
        if self.__tv:
            self.__tv.canalUp()

    def canalDown(self) -> None:
        if self.__tv:
            self.__tv.canalDown()

    def volumenUp(self) -> None:
        if self.__tv:
            self.__tv.volumenUp()

    def volumenDown(self) -> None:
        if self.__tv:
            self.__tv.volumenDown()

    def setCanal(self, canal: int) -> None:
        if self.__tv:
            self.__tv.setCanal(canal)

    def setVolumen(self, volumen: int) -> None:
        if self.__tv:
            self.__tv.setVolumen(volumen)