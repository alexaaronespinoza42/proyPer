#Ejercicio 2 if

numero1 = float(input('Ingerese el numero 1: '))
numero2 = float(input('Ingerese el numero 2: '))
numero3 = float(input('Ingerese el numero 3: '))

if numero1>=numero2 and numero1>=numero3:
    print(f'El numero mayor es {numero1}')
elif numero2>=numero1 and numero2>=numero3:
    print(f'El numero mayor es {numero2}')
if numero3>=numero1 and numero3>=numero2:
    print(f'El numero mayor es {numero3}')
