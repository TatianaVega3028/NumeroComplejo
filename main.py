class NumeroComplejo:
    def __init__(self, real: float, imaginario: float):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        signo = '+' if self.imaginario >= 0 else ''
        return f"{self.real} {signo} {self.imaginario}i"

    def sumar(self, otro):
        real = self.real + otro.real
        imaginario = self.imaginario + otro.imaginario
        return NumeroComplejo(real, imaginario)

    def restar(self, otro):
        real = self.real - otro.real
        imaginario = self.imaginario - otro.imaginario
        return NumeroComplejo(real, imaginario)

    def multiplicar(self, otro):
        real = self.real * otro.real - self.imaginario * otro.imaginario
        imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return NumeroComplejo(real, imaginario)

    def dividir(self, otro):
        denominador = otro.real ** 2 + otro.imaginario ** 2
        real = (self.real * otro.real + self.imaginario * otro.imaginario) / denominador
        imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / denominador
        return NumeroComplejo(real, imaginario)


# Ejemplo de uso
complejo1 = NumeroComplejo(3, 2)
complejo2 = NumeroComplejo(1, 7)

print("Número complejo 1:", complejo1)
print("Número complejo 2:", complejo2)

# Suma
resultado_suma = complejo1.sumar(complejo2)
print("Suma:", resultado_suma)

# Resta
resultado_resta = complejo1.restar(complejo2)
print("Resta:", resultado_resta)

# Multiplicación
resultado_multiplicacion = complejo1.multiplicar(complejo2)
print("Multiplicación:", resultado_multiplicacion)

# División
resultado_division = complejo1.dividir(complejo2)
print("División:", resultado_division)

