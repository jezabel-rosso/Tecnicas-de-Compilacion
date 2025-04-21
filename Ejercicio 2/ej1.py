def multiplicar(a, b):
    return a * b

# Solicitar al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Calcular el producto
resultado = multiplicar(num1, num2)

# Mostrar el resultado
print(f"El resultado de {num1} * {num2} es: {resultado}")