#Conjuntos
A={1,2,3,4}
B={2,3,5,6}
C={3,4,6,7}

print("A y B")
print(A|B)
print(A&B)
print(A-B)

print("A y C")
print(A|C)  
print(A&C)
print(A-C)

print("B y C")
print(B|C)
print(B&C)
print(B-C)

#Diferencia simetrica
print(A^B) #No toma encuenta el 2 y el 3
print(B^C) #No toma encuenta el 3 y el 6