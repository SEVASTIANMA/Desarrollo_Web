from abc import ABC, abstractmethod


# ==========================================
# 1. ABSTRACCIÓN: Clase Abstracta de Base
# ==========================================
class Empleado(ABC):
    """
    Clase abstracta que define la plantilla conceptual para cualquier empleado.
    No se pueden crear instancias directas de esta clase (Abstracción Pura).
    """

    def __init__(self, identificacion: str, nombre: str, salario_base: float):
        self.identificacion = identificacion
        self.nombre = nombre
        
        # ENCAPSULAMIENTO: Atributo privado utilizando doble guion bajo (__salario_base)
        # Esto impide que sea modificado directamente desde fuera de la clase.
        if salario_base < 0:
            raise ValueError("El salario base no puede ser un valor negativo.")
        self.__salario_base = salario_base

    # ENCAPSULAMIENTO: Métodos Getter y Setter para controlar el acceso al atributo privado
    @property
    def salario_base(self) -> float:
        """Getter para obtener el salario base de forma controlada."""
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, nuevo_salario: float):
        """Setter con validación de negocio para modificar el salario base."""
        if nuevo_salario < 0:
            raise ValueError("El nuevo salario base no puede negativo.")
        self.__salario_base = nuevo_salario

    # POLIMORFISMO: Método abstracto que obliga a todas las clases hijas a
    # proveer su propia implementación del cálculo de ingresos netos.
    @abstractmethod
    def calcular_ingresos_netos(self) -> float:
        """Calcula el salario final mensual neto del empleado."""
        pass

    def obtener_resumen(self) -> str:
        """Método concreto heredable que devuelve los datos básicos del empleado."""
        return f"ID: {self.identificacion} | Nombre: {self.nombre}"


# ==========================================
# 2. HERENCIA: Creación de Subclases
# ==========================================
class EmpleadoDesarrollador(Empleado):
    """Clase especializada para programadores. Hereda de la clase Empleado."""

    def __init__(self, identificacion: str, nombre: str, salario_base: float, lenguaje_experto: str):
        # Invocación al constructor de la superclase para inicializar atributos comunes
        super().__init__(identificacion, nombre, salario_base)
        # Atributo específico de la clase hija
        self.lenguaje_experto = lenguaje_experto

    # POLIMORFISMO: Sobrescritura (Overriding) del método abstracto del padre
    def calcular_ingresos_netos(self) -> float:
        """
        Los desarrolladores reciben un bono adicional del 15% sobre su salario base 
        por especialización técnica en desarrollo de software.
        """
        bono_tecnico = self.salario_base * 0.15
        return self.salario_base + bono_tecnico

    # Extensión del comportamiento: Sobrescritura de un método concreto
    def obtener_resumen(self) -> str:
        resumen_padre = super().obtener_resumen()
        return f"{resumen_padre} | Rol: Desarrollador ({self.lenguaje_experto})"


class EmpleadoGerente(Empleado):
    """Clase especializada para cargos gerenciales. Hereda de Empleado."""

    def __init__(self, identificacion: str, nombre: str, salario_base: float, bono_gestion: float):
        super().__init__(identificacion, nombre, salario_base)
        self.bono_gestion = bono_gestion

    # POLIMORFISMO: Sobrescritura (Overriding) adaptada a las reglas del Gerente
    def calcular_ingresos_netos(self) -> float:
        """Los gerentes suman un bono fijo de gestión administrativa a su salario."""
        return self.salario_base + self.bono_gestion

    def obtener_resumen(self) -> str:
        resumen_padre = super().obtener_resumen()
        return f"{resumen_padre} | Rol: Gerente Administrativo"


# ==========================================
# 3. GESTIÓN Y DEMOSTRACIÓN DEL POLIMORFISMO
# ==========================================
class SistemaNomina:
    """Clase controladora encargada de procesar un conjunto de objetos Empleado."""

    def __init__(self):
        # Almacenará objetos que compartan la interfaz común de Empleado
        self.lista_empleados = []

    def registrar_empleado(self, nuevo_empleado: Empleado):
        """Añade un empleado al sistema."""
        self.lista_empleados.append(nuevo_empleado)

    def procesar_nomina_total(self):
        """
        DEMOSTRACIÓN DE POLIMORFISMO EN ACCIÓN:
        Itera sobre una lista heterogénea de objetos (Desarrolladores, Gerentes)
        y llama al método calcular_ingresos_netos(). Cada objeto responde de manera
        autónoma ejecutando su propia lógica interna sin que la nómina sepa su tipo exacto.
        """
        print("--- PROCESAMIENTO DE NÓMINA EMPRESARIAL ---")
        costo_total_empresa = 0.0

        for emp in self.lista_empleados:
            ingresos_totales = emp.calcular_ingresos_netos()
            costo_total_empresa += ingresos_totales
            
            # Impresión de datos utilizando el comportamiento polimórfico
            print(emp.obtener_resumen())
            print(f" > Salario Base: ${emp.salario_base:.2f}")
            print(f" > Liquidación Neta Mensual: ${ingresos_totales:.2f}")
            print("-" * 50)

        print(f"COSTO TOTAL DE NÓMINA MENSUAL: ${costo_total_empresa:.2f}")


# ==========================================
# 4. EJECUCIÓN DEL PROGRAMA (PUNTO DE ENTRADA)
# ==========================================
if __name__ == "__main__":
    # Inicialización del sistema de nómina
    nomina_corporativa = SistemaNomina()

    # Creación de instancias de objetos (Instanciación de Clases Hijas)
    desarrollador_1 = EmpleadoDesarrollador("DEV-01", "Ana Martínez", 3500.00, "Python & Go")
    desarrollador_2 = EmpleadoDesarrollador("DEV-02", "Carlos Ruiz", 3200.00, "Rust")
    gerente_general = EmpleadoGerente("MGR-01", "Elena Gómez", 5000.00, 1200.00)

    # Registro de los objetos en el controlador
    nomina_corporativa.registrar_empleado(desarrollador_1)
    nomina_corporativa.registrar_empleado(desarrollador_2)
    nomina_corporativa.registrar_empleado(gerente_general)

    # Ejecución de la lógica polimórfica
    nomina_corporativa.processar_nomina_total()

    # Demostración del funcionamiento del Encapsulamiento
    print("\n--- PRUEBA DE CONTROL DE ENCAPSULAMIENTO ---")
    try:
        # Intentar modificar el salario con un valor inválido mediante el Setter
        desarrollador_1.salario_base = -1500.00
    except ValueError as error:
        print(f"Captura correcta del error de encapsulamiento: {error}")
