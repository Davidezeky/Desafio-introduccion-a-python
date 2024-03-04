p = int(input("ingrese el precio de subscriptores: "))
u = int(input("ingrese la cantidad de usuarios: "))
gt = int(input("ingrese gasto total: "))
utilidades_anteriores = int(input("ingrese las utilidades anteriores: "))

utilidades = p * u - gt
razon = utilidades_anteriores/utilidades

print(f"la razon de las utilidades del proyecto son: {razon:.2f}")