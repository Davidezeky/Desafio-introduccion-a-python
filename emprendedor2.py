
p = int(input("ingrese el precio de subscriptores: "))
u = int(input("ingrese la cantidad de usuarios: "))
up = int(input("ingrese la cantidad de usuarios premium: "))
gt = int(input("ingrese gasto total: "))


preciopremium = 1.5 * p

up *= preciopremium

utilidades = p * u + up - gt

print(f"las utilidades del proyecto son {utilidades}")