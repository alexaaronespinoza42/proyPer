#Ejercicio 1 if

numero1 = float(input('Escribe un numero: '))
numero2  = float(input('Escribe otro numero: '))

if numero1%2==0 and numero2%2==0:
    print('Ambos son pares')    
elif numero1%2==0 and numero2%2!=0:
    print(f'Solo {numero1} es un numero par')
elif numero1%2!=0 and numero2%2==0:
    print(f'Solo {numero2} es un numero par')
else:
    print('Ningun numero es par')

