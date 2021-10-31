mascotas = {
    'Gato' : [],
    'Perro' : [],
    'Loro' : [],
    'Pez' : [],
}

menu = "Especies. \n1. Agregar Especies\n2. Ver especies\3. Salir"

while(True):
    opcion = input("Por favor ingrese el nombre de de la especie").lower()
    if((opcion == "Gato" or opcion == "Perro") or (opcion == "Loro" or opcion == "Pez")):
        if(len(mascotas[opcion])<4):
            mascotas[opcion].append(input(f"Ingrese la raza de {opcion}"))
        else:
            print("Esta especie ya esta llena")
    else:
        print("Esta especie no existe")
    