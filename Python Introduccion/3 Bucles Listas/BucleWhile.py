#Blue While
import math

numero=0
while numero<=20:
    print(numero)
    numero+=1

numero1=int(input("Escriba un numero: "))

while numero1<=0:
    print("Porfavor ingrese un numero positivo")
    numero1 = int(input("Vuelve a ingresar un numero positivo: "))
print(f"El resultado de la raiz cuadrada es: {math.sqrt(numero1):.2f}")