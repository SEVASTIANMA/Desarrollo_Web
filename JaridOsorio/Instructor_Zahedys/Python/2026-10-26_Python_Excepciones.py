# ==========================================
# Control de Errores y Excepciones en Python
# ==========================================

def dividir_numeros():
    try:
        num1 = float(input("Ingrese el numerador: "))
        num2 = float(input("Ingrese el denominador: "))
        resultado = num1 / num2
        print(f"✅ El resultado de la división es: {resultado}")
    except ZeroDivisionError:
        print("❌ Error: No es posible dividir entre cero.")
    except ValueError:
        print("❌ Error: Debe ingresar valores numéricos válidos.")
    finally:
        print("🔄 Proceso de división finalizado.\n")

# Simulación de ejecución controlada
print("--- INICIO DE PRUEBA DE EXCEPCIONES ---")
# dividir_numeros() # Descomentar para ejecutar de forma interactiva
print("Módulo de manejo de excepciones cargado correctamente.")