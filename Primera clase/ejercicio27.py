while True:
    try:
        # Se solicita la temperatura al usuario
        fahrenheit_str = input("Ingrese la temperatura en grados Fahrenheit (o 999 para salir): ")
        
        # Se convierte la entrada a un número flotante
        fahrenheit = float(fahrenheit_str)
        
        # Se verifica si la entrada es el valor de salida
        if fahrenheit == 999:
            print("Programa finalizado. ¡Gracias por usar el conversor!")
            break  # Se sale del bucle
        
        # Se realiza la conversión
        celsius = (5/9) * (fahrenheit - 32)
        
        # Se imprime el resultado formateado
        print(f"{fahrenheit:.2f} grados Fahrenheit son {celsius:.2f} grados Celsius.")

    except ValueError:
        # Se maneja el error si el usuario no ingresa un número
        print("Entrada inválida. Por favor, ingrese un valor numérico.")