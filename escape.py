import math

radio = int(input("ingrese el radio en kilometros:"))
gravedad = float(input("ingrese la constante g:"))

radio = radio * 1000
ve = math.sqrt(2*gravedad*radio)


print(f"la velocidad de escape es {ve:.1f} [m/s]")