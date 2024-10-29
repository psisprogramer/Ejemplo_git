from modulo_1 import*
print("CALCULADORA\n")
print("1. suma")
print("2. resta")
print("3. multiplicación")
print("4. división")
print("5. otra cosa")
print("0. Salir")                        
opcion = input("--Ingresa una opción: ")

while True:
        if opcion == "1":
                n1 = float(input("Ingresa el primer número: "))
                n2 = float(input("Ingresa el segundo número: "))
                resultado = suma(n1, n2)
                print("El resultado de la suma es: ", resultado)
        if opcion == "2":
                n1 = float(input("Ingresa el primer número: "))
                n2 = float(input("Ingresa el segundo número: "))
                resultado = resta(n1, n2)
                print("El resultado de la resta es: ", resultado)
        if opcion == "3":
                n1 = float(input("Ingresa el primer número: "))
                n2 = float(input("Ingresa el segundo número: "))        
                resultado = multiplicacion(n1, n2)
                print("El resultado de la multiplicación es: ", resultado)
        if opcion == "4":
                n1 = float(input("ingresa el primer numero: "))
                n2 = float(input("Ingresa el segundo número: "))
                if n2 != 0:
                        resultado = division(n1, n2)
                        print("El resultado de la división es: ", resultado)  
                else:
                        print("No se puede dividir por cero.")
        if opcion == "0":
                print("Gracias por utilizar nuestra calculadora.")
                break
        else:
                print("Opción inválida.")
