# Ejercicio Práctico StarUML: Diagrama de Clases

## Objetivo
Representar la estructura estática de un módulo de gestión de entregas formativas mediante clases, atributos, métodos y visibilidad UML.

## Clases Propuestas en StarUML
1. **`Aprendiz`**
   - Atributos privados/protegidos: `- documento: String`, `- nombre: String`, `- ficha: String`
   - Métodos públicos: `+ registrarEntrega(entrega: Entrega): void`, `+ consultarHistorial(): List<Entrega>`
2. **`Entrega`**
   - Atributos: `- fecha: Date`, `- tema: String`, `- archivoRuta: String`, `- estado: String`
   - Métodos: `+ validarArchivo(): Boolean`, `+ marcarRevisada(): void`

## Relaciones en el Diagrama
- **`Aprendiz` "1" o--- "0..*" `Entrega`**: Asociación / Composición según el ciclo de vida del registro en el sistema.
