class Alumno:

    def __init__(self):
        self._nombre = "Desconocido"
        self._nota = 0

    def setNombre(self, nombre):
        self._nombre = nombre
    def setNota(self, nota):
        self._nota = nota

    def getNombre(self):
        return self._nombre
    def getNota(self):
        return self._nota
    
    def estatusAlumno(self):
        if self._nota >= 10:
            return "APROBADO"
        else:
            return "REPROBADO"


if __name__ == "__main__":

    miAlumno = Alumno()
    miAlumno.setNombre("Ramon Dugarte")
    miAlumno.setNota(20)
    nombre = miAlumno.getNombre()
    nota = miAlumno.getNota()
    estatus = miAlumno.estatusAlumno()

    print('''
    Alumno: %s
    Nota: %d
    Estatus: %s''' % (nombre, nota, estatus))