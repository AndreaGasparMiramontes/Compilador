class EP:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        cadena = self.name
        try:
            cadena = cadena + "\n" + str(self.id)
        except AttributeError:
            pass
        try:
            cadena = cadena + " " + str(self.mas)
        except AttributeError:
            pass
        try:
            cadena = cadena + " " + str(self.E)
        except AttributeError:
            pass
        
        return cadena