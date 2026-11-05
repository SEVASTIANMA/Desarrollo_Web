# Propuesta de Proyecto Académico: Sistema de Gestión de Información (SGI)
**Programa de Formación:** Análisis y Desarrollo de Software (ADSO)  
**Formato:** Documentación de Proyecto / Guía Didáctica  

---

## 1. Definición del Tema

**Tema:** Diseño, desarrollo e implementación de un *Sistema Web de Gestión de Inventario y Ventas para Pequeños Comercios*.

El proyecto consiste en la creación de una aplicación web integral que automatice el registro de productos, el control de existencias en tiempo real, el procesamiento de ventas y la generación de reportes analíticos para optimizar la toma de decisiones en microempresas.

---

## 2. Formulación de Objetivos

### Objetivo General
Desarrollar un sistema web funcional de gestión de inventario y ventas mediante la aplicación de metodologías ágiles de desarrollo de software, lenguajes de programación modernos y bases de datos relacionales, para optimizar los procesos operacionales de pequeñas empresas.

### Objetivos Específicos
1. **Levantar y documentar** los requerimientos funcionales y no funcionales del sistema mediante técnicas de recolección de información.
2. **Diseñar la arquitectura del software**, incluyendo diagramas UML, modelo entidad-relación de la base de datos y prototipos de interfaz de usuario (UI/UX).
3. **Construir el sistema** implementando el *frontend* y el *backend* mediante el uso de buenas prácticas de programación, patrones de diseño y control de versiones.
4. **Ejecutar pruebas de software** (unitarias e integrales) para garantizar la calidad, seguridad y correcto funcionamiento de la aplicación antes de su despliegue.

---

## 3. Marco Teórico

### 3.1. Concepto Básico del Tema
El desarrollo de software enfocado en sistemas de información abarca el ciclo de vida completo de una aplicación: desde el análisis de necesidades hasta el mantenimiento del sistema. Se fundamenta en tres pilares principales:
* **Frontend:** La interfaz gráfica interactiva con la que el usuario final interactúa.
* **Backend:** La lógica de negocio y las API que procesan la información.
* **Base de Datos:** El sistema encargado de almacenar, recuperar y estructurar la información de manera persistente y segura.

### 3.2. Importancia del Tema
En la era digital, la automatización de procesos mediante software no es un lujo, sino una necesidad operativa. La falta de control en los inventarios genera pérdidas económicas y deficiencias en la atención al cliente. Un sistema de información centralizado reduce el error humano, optimiza el tiempo de respuesta y proporciona métricas clave para la sostenibilidad del negocio.

### 3.3. Relación con la Carrera (ADSO)
Este tema integra de manera holística las competencias fundamentales del programa ADSO:
* **Análisis:** Identificación de necesidades del cliente y modelado de requisitos (Historias de Usuario / Casos de Uso).
* **Diseño:** Estructuración de la arquitectura del sistema, diagramas de clases, datos y prototipado UI/UX.
* **Desarrollo:** Escritura de código limpio, consumo de API REST, manejo de frameworks y bases de datos SQL/NoSQL.
* **Calidad y Despliegue:** Implementación de pruebas, control de versiones con Git/GitHub y conceptos de integración continua.

---

## 4. Metodología

Para el desarrollo del proyecto se aplicará la metodología ágil **Scrum**, combinada con el enfoque de **Ciclo de Vida de Desarrollo de Software (SDLC)**.

| Fase | Descripción de Actividades |
| :--- | :--- |
| **1. Iniciación y Análisis** | Levantamiento de requisitos, creación del *Product Backlog* y definición de las Historias de Usuario. |
| **2. Diseño** | Modelado de la base de datos (MER/MR), arquitectura del sistema y diseño de *wireframes* (Figma). |
| **3. Desarrollo (Sprints)** | Programación iterativa en Sprints de 2 semanas (*Backend* + *Frontend* + Integración). |
| **4. Pruebas e Integración** | Realización de pruebas funcionales, corrección de *bugs* y refactorización de código. |
| **5. Cierre y Despliegue** | Despliegue en entorno de pruebas (*staging* / *cloud*) y entrega de documentación técnica. |

---

## 5. Organización de Actividades

```mermaid
gantt
    title Cronograma de Actividades - Proyecto ADSO
    dateFormat  YYYY-MM-DD
    section Fase 1: Análisis
    Historias de Usuario y Requisitos    :a1, 2026-11-01, 7d
    section Fase 2: Diseño
    Modelo de BD y Prototipos UI/UX      :a2, after a1, 10d
    section Fase 3: Desarrollo
    Desarrollo Backend (API REST)         :a3, after a2, 14d
    Desarrollo Frontend e Integración    :a4, after a3, 14d
    section Fase 4: Pruebas y Cierre
    Pruebas de Software y Documentación   :a5, after a4, 7d
    Presentación Final                   :a6, after a5, 3d