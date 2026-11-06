import random

def jugar_adivinanza():
    # 1. Configuración de los datos correctos
    USUARIO_CORRECTO = "admin"
    CONTRASENA_CORRECTA = "python2026"
    # El sistema genera un número aleatorio entre 1 y 100
    NUMERO_SECRETO = random.randint(1, 100)
    
    intentos_numero = 0
    
    print("==================================================")
    print("  ¡BIENVENIDO AL DESAFÍO DE ACCESO DE SEGURIDAD!  ")
    print("==================================================")
    print("Debes adivinar el Usuario, la Contraseña y el Número Secreto.\n")

    # FASE 1: Adivinar el Nombre de Usuario
    while True:
        usuario_ingresado = input("1/3. Introduce el Nombre de Usuario: ").strip()
        if usuario_ingresado == USUARIO_CORRECTO:
            print("¡Usuario correcto! Continuemos...\n")
            break
        else:
            print("❌ Usuario incorrecto. Inténtalo de nuevo (Pista: empieza por 'ad').\n")

    # FASE 2: Adivinar la Contraseña
    while True:
        contrasena_ingresada = input("2/3. Introduce la Contraseña: ").strip()
        if contrasena_ingresada == CONTRASENA_CORRECTA:
            print("¡Contraseña correcta! Último paso...\n")
            break
        else:
            print("❌ Contraseña incorrecta. Inténtalo de nuevo (Pista: incluye el nombre de este lenguaje y el año actual).\n")

    # FASE 3: Adivinar el Número Secreto
    print("3/3. El sistema ha generado un número secreto entre 1 y 100. ¡Adivínalo!")
    
    while True:
        entrada = input("¿Cuál crees que es el número?: ").strip()
        
        # Validación para asegurarse de que el usuario introduce un número entero
        if not entrada.isdigit():
            print("Por favor, introduce un número válido.")
            continue
            
        intento = int(entrada)
        intentos_numero += 1
        
        if intento < NUMERO_SECRETO:
            print("🔮 El número secreto es MAYOR.")
        elif intento > NUMERO_SECRETO:
            print("🔮 El número secreto es MENOR.")
        else:
            print(f"\n🎉 ¡EXCELENTE! Has adivinado el número secreto ({NUMERO_SECRETO}) en {intentos_numero} intentos.")
            break

    # Final del juego
    print("\n==================================================")
    print("   🔓 ¡ACCESO CONCEDIDO! Has completado el juego.   ")
    print("==================================================")

# Ejecutar el juego
if __name__ == "__main__":
    jugar_adivinanza()
