class Vehiculo:

    def __init__(self, color, ruedas, puertas):
        self._color = color
        self._ruedas = ruedas
        self._puertas = puertas


class Coche(Vehiculo):

    def __init__(self, color, velocidad, cilindrada, puertas=4):
        Vehiculo.__init__(self, color, 4, puertas)
        self._velocidad = velocidad
        self._cilindrada = cilindrada

    def __str__(self):
        return '''
        Caracteristicas del Coche:
        Color: %s
        Nro. de Puertas: %d
        Velocidad: %.2f Km/h
        Cilindrada: %.2f cc
        ''' % (self._color, self._puertas, self._velocidad, self._cilindrada)


if __name__ == "__main__":
    miCoche = Coche("blanco", 120, 2.5)
    print(miCoche)