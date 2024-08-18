
array=["futbol","pc",18.6,18,[6,7,10,4],True,False]
print(len(array))
array.append(66)
array.append(True)
print(array)

array1=["futbol","pc",18.6,18,[6,7,10,4],True,False]
array1.insert(1,88)
print(array1)

array1=["futbol","pc",18.6,18,[6,7,10,4],True,False]
array1.extend([1,88,True,100])
print(array1)

array2=[200,250,"hola"] 
array3=array1+array2
print(array3)

array=["futbol","pc",18.6,18,[6,7,10,4],True,False,"pc"]
print("pc" in array)
print("pcc" in array) # buscar datos

print(array.index("pc"))
print(array.count("pc"))
print(array.count("hola"))
print(array.count(True))

array=["futbol","pc",18.6,18,[6,7,10,4],True,False,"pc"]
array.remove("pc")
array.remove(18)
array.remove(True) #elimina datos
print(array)

array=["futbol","pc",18.6,18,[6,7,10,4],True,False,"pc"]
array.reverse()
print(array)

array=[1,2,8,-11,5]
array.sort()
print(array)

array=[1,2,8,-11,5]
array.sort(reverse=True)
print(array)

array.clear() #elimina todo