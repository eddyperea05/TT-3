def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

list = []
palabra=""
validador = True

while(validador):
    palabra = input("Por favor ingrese un articulo de la vida cotidiana ")
    if(has_numbers(palabra)):
        print("Contiene numero, por favor validar nuevamente")
    else:
        list.append(palabra)
        print("Se ha agregado la palabra")
    entrada = input("Desea seguir agregado? (Si/No) ").lower()
    if(entrada == "no"):
        validador = False
print(list)