import sys

print("Escribe tu texto y presiona Ctrl+D (o Ctrl+Z en Windows) para terminar.")

# Lee cada línea de la entrada estándar (stdin)
try:
    for linea in sys.stdin:
        # La línea leída incluye el salto de línea, por lo que strip() lo elimina
        print(f"Línea leída: {linea.strip()}")
except KeyboardInterrupt:
    # Esto maneja la interrupción si el usuario presiona Ctrl+C en lugar de Ctrl+D
    print("\n\nProceso interrumpido por el usuario.")
except EOFError:
    # Este error se lanza si se detecta el fin de archivo
    print("\n\n¡Fin de archivo detectado! El programa ha terminado.")