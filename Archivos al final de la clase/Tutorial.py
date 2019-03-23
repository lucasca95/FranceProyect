def square(nb):
    resul=nb*nb #resul es variable local a la funcion
    return resul


if (True):
    print('Hello world')
else:
    print('Chau')

studentsList=[] #lista vacia
studentsList.append("Carl")
studentsList.append("Paul")
print(studentsList)
print(" ")

studentsDic={} #diccionario vacio
studentsDic["Mono"]=22
studentsDic["Martin"]=22
studentsDic["Lucas"]=23
print(studentsDic["Mono"])
print(studentsDic)
print(" ")


for s in studentsList:
    print(s)
print(" ")

for s in studentsDic:
    print(s)
print(" ")

print("Calculamos 3 al cubo con funcion")
print(square(3))
print(" ")

print(" ")
print('Fin de programa')