# Ejercicio 4
#Obtener el precio final que se tiene que pagar si se aplica el
#36% de descuento del total de la compra

precio = float(input('Cual es el precio inicial?: '))
descuento = precio * 0.36
precioFinal = precio-descuento

print(f'El precio final es de {precioFinal:.2f}')