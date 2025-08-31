# Autor: Jesús David Quintero
# Código de prueba

# 1. Solicita un número del 1-10 y lo imprime
texto = input("numero del 1-10: ")
print(texto)

# 2. Solicita un número para multiplicar y muestra su tabla
m = input("numero del 1-10 para multiplicar: ")
mn = int(m)

def multiply():
    """Imprime la tabla de multiplicar de un número del 1 al 10."""
    for i in range(1, 11):
        print(f"{mn} * {i} = {mn*i}")

multiply()

# 3. Calcula el factorial de un número
def factorial_de_un_numero():
    """Calcula el factorial de un número entero no negativo ingresado por el usuario."""
    num_factorial_str = input("ingresa el número para calcular el factorial: ")
    num_factorial = int(num_factorial_str)
    
    # Maneja casos especiales para 0 y números negativos
    if num_factorial < 0:
        return "El factorial no está definido para números negativos."
    elif num_factorial == 0:
        return 1
    else:
        # Calcula el factorial usando un bucle
        resultado = 1
        for i in range(1, num_factorial + 1):
            resultado *= i
        return f"El factorial de {num_factorial} es: {resultado}"

# Llama a la función para ejecutar la tercera parte del script
print(factorial_de_un_numero())