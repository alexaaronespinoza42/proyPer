#Ejercicio 3 if

nombre1 = input('Escribe un nombre: ')
nombre2 = input('Escribe otro nombre: ')

if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
    print('Coincidencia')
else:
    print('No hay Coincidencia')