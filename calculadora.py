import os

def validar_dato(dato):
    while not type(dato) == float:
        try:
            dato = float(dato)
        except ValueError:
            dato = input("Por favor, sólo ingresos numéricos: ")
    return dato
            
def calcular(num_1, num_2, operacion):
    match operacion:
        case "a":
            resultado = num_1 + num_2
        case "b":
            resultado = num_1 - num_2
        case "c":
            resultado = round(num_1 * num_2, 3)
        case "d":
            if num_2 != 0:
                resultado = num_1 / num_2
            else:
                resultado = "Error! no se puede dividir por 0."
    return f"Resultado: {resultado}"     
    
opcion = ""

while opcion.lower() != "e":
    os.system('cls')
    print("""
    a-Sumar
    b-Restar
    c-Multiplicar
    d-Dividir
    e-Salir
    """)
    opcion = input("Ingrese opción: ")
    if opcion.lower() in ['a', 'b', 'c', 'd']:
        numero_1 = input("Ingrese primer número: ")
        numero_1 = validar_dato(numero_1)
        numero_2 = input("Ingrese segundo número: ")
        numero_2 = validar_dato(numero_2)
        print(calcular(numero_1, numero_2, opcion))
    elif opcion == "e":
        print("Gracias por utilizar la app!")
        continue
    else:
        print("Opción de operación inválida!")
    input("Pulse ENTER para continuar >>>")