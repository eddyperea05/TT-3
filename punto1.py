def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def mientras(list, limit,text):
    while(len(list) < limit):
        palabra = input(f"Por favor ingrese un {text}: ")
        if(has_numbers(palabra)):
            print("Contiene numero, por favor validar nuevamente")
        else:
            list.append(palabra)
            print("Se ha agregado la palabra")

#Se agregan los artuculos de la vida cotidiana
listArticulos = []
text = "articulo de la vida cotidiana"
#mientras(listArticulos,10,text)
print(listArticulos)
#Se agregan lo animales
listAnimales = []
text = "animal"
mientras(listAnimales,7,text)
print(listAnimales, len(listAnimales))
opcion = input("Desea terminar con el procedimiento? (Si/No)").lower()
if(opcion == "si"):
    listArticulos += listAnimales
    print(listArticulos)
else:
    del listArticulos[:]
    del listAnimales[:]
    print(listArticulos,listAnimales)
#Transforación de lista a Tupla
tuple = tuple(listArticulos)
print(tuple,len(tuple))
print(tuple[1])