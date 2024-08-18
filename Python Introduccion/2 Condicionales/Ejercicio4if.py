saldoInicial = 0

print('1.- Ingreso de dinero')
print('2.- Retiro de dinero')
print('3.- Mostrar dinero')
print('4.- Salir')

seleccion = int(input('Elija una opcion: '))

if seleccion == 1:
    ingreso = float(input('Dinero a ingresar: '))
    saldoInicial+=ingreso
    print(f'Nuevo saldo en la cuenta: {saldoInicial}')
elif seleccion == 2:
    retiro = float(input('Dinero a retirar: '))
    if retiro>saldoInicial:
        print('Dinero insuficiente')
    else:
        retiro-=saldoInicial
        print(f'Nuevo saldo: {saldoInicial}')
elif seleccion == 3:
    print(f'El slado actua es de: {saldoInicial}')
elif seleccion == 4:
    print('Regresa pronto!')
else:
    ('Porfavor, elige un numero e intenta denuevo.')