import random

caracteres = list("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
Longitud = int(input("Escribe el numero de caracteres de tu contraseña: "))

for i in range(Longitud):
   Contraseña = random.choices(caracteres, k=Longitud)

contraseña = ''.join(Contraseña)
print(f"La contraseña generada es: {contraseña}")
x = input("Presione enter para salir...")
