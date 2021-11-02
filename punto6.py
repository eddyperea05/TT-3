mascotas = {
    'gato': [],
    'perro': [],
    'loro': [],
    'pez': [],
}
while(True):
    menu = input("Especies. \n1. Agregar Especies\n2. Ver especies\n3. Salir ")
    if(menu == "1"):
        opcion = input(
            "Por favor ingrese el nombre de de la especie (Gato, perro, loro, pez) ").lower()
        if((opcion == "gato" or opcion == "perro") or (opcion == "loro" or opcion == "pez")):
            if(len(mascotas[opcion]) < 4):
                mascotas[opcion].append(input(f"Ingrese la raza de {opcion} "))
                print("Se ha agregado")
            else:
                print("Esta especie ya esta llena ")
        else:
            print("Esta especie no existe")
    elif(menu == "2"):
        opcion = input(
            "Por favor ingrese el nombre de de la especie (Gato, perro, loro, pez) ").lower()
        if((opcion == "gato" or opcion == "perro") or (opcion == "loro" or opcion == "pez")):
            print(mascotas[opcion])
        else:
            print("Esa especie no exite")
    elif(menu == "3"):
        print("Adiós")
        break
    else:
        print("Opción incorrecta, por favor vuelva a intentar")
