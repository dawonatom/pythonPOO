num1 = float(input("Pon un Numero en formato numerico: "))
num2 = float(input("Pon un Numero en formato numerico: "))

def encontrar_menor(a, b):
    if a < b:
        return a
    else:
        return b
    
def encontrar_mayor(a, b):
    if a < b:
        return b
    else:
        return a

# Llamas a las funciones y les pasas los números que el usuario ingresó
menor = encontrar_menor(num1, num2)
mayor = encontrar_mayor(num1, num2)

print(f"El numero menor es: {menor}")
print(f"El numero mayor es: {mayor}")