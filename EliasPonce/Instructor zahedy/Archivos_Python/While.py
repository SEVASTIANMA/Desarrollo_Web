opcion = ""

# El ciclo se repite mientras la opción NO sea "3"
while opcion != "3":
    print("\n--- MENÚ DE BIENVENIDA ---")
    print("1. Recibir un saludo")
    print("2. Ver una frase motivacional")
    print("3. Salir")
    
    opcion = input("Elige una opción (1-3): ")
    
    if opcion == "1":
        print("¡Hola! Qué gusto tenerte por aquí practicando Python.")
    elif opcion == "2":
        print("El éxito es la suma de pequeños esfuerzos repetidos día tras día.")
    elif opcion == "3":
        print("Saliendo del programa... ¡Hasta luego!")
    else:
        print("Opción inválida. Por favor, elige 1, 2 o 3.")
