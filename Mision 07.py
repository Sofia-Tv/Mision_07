#Autor Sofía Trujillo Vargas
#Seguir usando la función while para crear ciclos

def probarDivisiones(divi,divnio):
    cociente = 0
    while divi >= divnio:
        divi = divi - divnio
        cociente = cociente + 1
    print("Este es el cociente",cociente,"este es el residuo",divi)

def encontrarMayor():
    x = 0
    y = 0
    while x != -1:
        x = int(input("Pon un número entero positivo: "))
        if x >= y:
            y = x

    print("Este es el mayor: ",y)
    input("Int para seguir")

def main():
    x = -1
    while x != 3:
        print("""¡¡¡BIENVENIDO!!!. Misión 07 . Ciclos While
        1. Calcular Divisiones
        2. Encontar el Mayor
        3. Sailir""")
        opción = int(input("¿Que quires hacer?"))

        if opción == 1:
            dividendo = int(input("Dame el dividendo, el que esta adentro de la casita: "))
            divisor = int(input("Dame el divisor, el que esta afuera de la casita"))
            probarDivisiones(dividendo,divisor)

        if opción == 2:
            encontrarMayor()

        if opción == 3:
            print("Ten Buen Día!!!")

        else:
            print(x,"Este no es un valor válido")
            input("Int para continuar")



main()

