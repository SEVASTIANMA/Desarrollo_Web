### Estrategia de Validación de Entradas en Programación Defensiva

La estrategia de validación de entradas se divide en tres capas principales:

1. **Validación de Tipo de Dato:** 
   * Comprobar que el valor recibido coincida exactamente con la estructura esperada (por ejemplo, asegurar que un campo de edad sea estrictamente un número entero positivo o que un identificador sea un valor alfanumérico).

2. **Restricción de Longitud (Límites):** 
   * Definir un límite mínimo y máximo de caracteres para evitar ataques de denegación de servicio (DoS) por agotamiento de memoria o desbordamiento de búfer (*buffer overflow*).

3. **Verificación de Formato (Expresiones Regulares y Listas Blancas):** 
   * Aplicar reglas estrictas que permitan únicamente los caracteres válidos. Es preferible usar un enfoque de **lista blanca** (permitir solo lo conocido como seguro) en lugar de una lista negra (bloquear caracteres específicos).

---

### Ejemplo de Implementación Lógica (Pseudocódigo / Validación en Backend)

```text
FUNCION validarNombreUsuario(entrada):
    // 1. Verificar que no esté vacío
    SI entrada ES NULO O longitud(entrada) == 0 ENTONCES:
        RETORNAR Falso, "El campo no puede estar vacío"
    
    // 2. Verificar longitud máxima y mínima
    SI longitud(entrada) < 3 O longitud(entrada) > 20 ENTONCES:
        RETORNAR Falso, "El nombre debe tener entre 3 y 20 caracteres"
    
    // 3. Verificar formato (Solo letras y números, sin caracteres especiales)
    SI NO coincideConPatron(entrada, "^[a-zA-Z0-9]+$") ENTONCES:
        RETORNAR Falso, "El formato contiene caracteres no permitidos"
        
    RETORNAR Verdadero, "Entrada válida"