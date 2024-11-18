class Marca:
    def __init__(self, nombre: str):
        self.__nombre = nombre  # Atributo privado

    # Métodos getter y setter para nombre
    def getNombre(self) -> str:
        return self.__nombre

    def setNombre(self, nombre: str) -> None:
        self.__nombre = nombre