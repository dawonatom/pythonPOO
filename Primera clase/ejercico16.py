# Se inicializa el resultado en 1, ya que cualquier numero multiplicado por 1 es el mismo
resultado = 1

# Se itera a traves de los primeros 20 numeros naturales (del 1 al 20)
for i in range(1, 21):
    # En cada iteracion, se multiplica el resultado actual por el numero 'i'
    resultado = resultado * i

# Se imprime el resultado final
print(f"La multiplicación de los primeros 20 números naturales es: {resultado}")