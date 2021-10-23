import math

def calculeCircule():
    return {'radio': float(input("Ingrese por favor el radio del circulo "))}

def calculeRectangulo():
    return {
        'alto': float(input("Por favor ingrese el alto del rectangulo ")),
        'largo': float(input("Por favor ingrese el largo del rectangulo "))
    }

def calculeTyP():
    return {
        'base': float(input("Ingrese la base por favor ")),
        'altura': float(input("Ingrese la alto por favor "))
    }

def calculeParalele():
    return {
        'largo': float(input("Por favor ingrese el largo ")),
        'ancho': float(input("Por favor ingrese el ancho ")),
        'alto': float(input("Por favor ingrese el alto: "))
    }

dicc = {
    '1': calculeCircule,
    '2': calculeRectangulo,
    '3': calculeTyP,
    '4': calculeTyP,
    '5': calculeParalele
}

def menu(index):
    return {
        '1': lambda radio: math.pi*(radio**2),
        '2': lambda alto, largo: alto*largo,
        '3': lambda base, altura: (base * altura)/2,
        '4': lambda base, altura: (base * altura),
        '5': lambda largo, ancho, alto: 2*largo*ancho+2*largo*alto+2*ancho*alto
    }[index](**dicc[index]())

menutext = "Hola, este es un programa para calcular el area. Tenemos las siguientes opciones:\n1. Circulo\n2. Rectángulo\n3. Triangulo\n4. Paralelogramo\n5. Paralelepípedo: "

while(True):
    try:
        print(menu(input(menutext)))
    except ValueError:
        print('Debe ingresar solo numeros')
    except KeyError:
        print('Debe ingresar un valor del menu')
    if(input("Desea calcular más areas? si/no: ").lower()=="no"):
        break