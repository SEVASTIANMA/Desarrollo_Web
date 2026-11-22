# Investigación de Biología Computacional y Proyecto de Ciencia: Simulación Híbrida Epidemiológica y Evolutiva (BioSim-SEIRV)

## Parte 1: Investigación Científica

### 1. Introducción
La **biología computacional** integra el análisis de datos, el modelado matemático y la simulación por computadora para comprender sistemas biológicos complejos. Uno de sus campos más relevantes es la **epidemiología matemática**, la cual estudia cómo se propagan las enfermedades infecciosas dentro de una población y cómo intervienen factores biológicos, ambientales y sociales.

Históricamente, los modelos compartimentales han sido la piedra angular de esta disciplina. Estos dividen a una población en estados epidemiológicos distintos y utilizan ecuaciones diferenciales o simulaciones estocásticas para predecir la evolución de un brote.

### 2. Fundamentos Biológicos y Matemáticos

#### A. El Modelo Compartimental SEIRV
A diferencia del modelo clásico SIR (Susceptible-Infectado-Recuperado), los sistemas biológicos reales requieren mayor precisión:
1. **Susceptibles ($S$):** Individuos sanos sin inmunidad que pueden contraer el patógeno.
2. **Expuestos ($E$):** Individuos infectados que se encuentran en el **período de incubación** (portan el patógeno pero aún no son altamente contagiosos).
3. **Infectados ($I$):** Individuos activos que presentan síntomas y transmiten la enfermedad.
4. **Recuperados ($R$):** Individuos que superaron la infección y adquirieron inmunidad temporal o permanente.
5. **Vacunados ($V$):** Individuos inmunizados artificialmente antes de contraer el patógeno.

#### B. Parámetros Biológicos Clave
* **Tasa de transmisión ($\beta$):** Probabilidad de contagio por contacto multiplicada por la tasa de contactos diarios.
* **Tasa de incubación ($\sigma$):** Inverso del período de latencia ($1 / \text{días de incubación}$).
* **Tasa de recuperación ($\gamma$):** Inverso del período infeccioso ($1 / \text{días de enfermedad}$).
* **Pérdida de inmunidad ($\omega$):** Tasa a la cual los recuperados o vacunados vuelven a ser susceptibles (deriva antigénica o caída de anticuerpos).
* **Número Reproductivo Básico ($R_0$):** Número promedio de casos secundarios producidos por un solo individuo infectado en una población totalmente susceptible:
  $$R_0 = \frac{\beta}{\gamma}$$
  * Si $R_0 > 1$, la epidemia se expande exponencialmente.
  * Si $R_0 < 1$, el brote se extingue.

#### C. Evolución Genética y Mutación del Patógeno
En la biología real, los virus y bacterias no son estáticos. Durante la replicación, ocurren errores en la polimerasa que generan **mutaciones**. Si una mutación confiere mayor afinidad por los receptores celulares o evasión inmunitaria, la selección natural favorece esa variante, alterando dinámicamente los valores de $\beta$ y $\omega$ a lo largo del tiempo.

### 3. Hipótesis del Proyecto Científico
> *"Si se introduce una tasa de mutación estocástica en un patógeno dentro de una población con vacunación parcial, se observarán oleadas epidémicas recurrentes (comportamiento endémico) en lugar de una única curva de extinción, debido a la evasión inmunitaria y al aumento progresivo de la transmisibilidad."*

---

## Parte 2: Código Fuente del Proyecto (`biosim_seirv.py`)

Guarda el siguiente código en un archivo llamado `biosim_seirv.py` y ejecútalo con `python biosim_seirv.py`. Utiliza únicamente librerías estándar de Python 3.

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
PROYECTO DE CIENCIA COMPUTACIONAL: BIOSIM-SEIRV v2.5
Título: Simulación Híbrida (Ecuaciones Diferenciales + Agentes Espaciales)
        de Dinámica Epidemiológica, Inmunidad y Evolución Viral.
Autor: Investigación de Biología Computacional
Lenguaje: Python 3
Descripción:
    Este programa modela la propagación de un patógeno en una población
    biológica utilizando dos enfoques complementarios:
    1. Modelo Determinista SEIRV resuelto mediante Runge-Kutta de 4to Orden (RK4).
    2. Modelo Estocástico Basado en Agentes (ABM) con mutación genética de cepas,
       movilidad espacial, cuarentena dinámica y memoria inmunológica.
================================================================================
"""

import math
import random
import statistics
import json
import csv
import os
import time
from datetime import datetime
from typing import List, Dict, Tuple, Optional


# ==============================================================================
# SECCIÓN 1: CONFIGURACIÓN Y PARÁMETROS BIOLÓGICOS GLOBALES
# ==============================================================================

class ParametrosBiologicos:
    """
    Almacena las constantes y tasas biológicas que rigen el comportamiento
    del patógeno y la respuesta inmunológica del huésped.
    """
    def __init__(
        self,
        poblacion_total: int = 1000,
        infectados_iniciales: int = 5,
        vacunados_iniciales: int = 150,
        tasa_transmision_base: float = 0.35,
        dias_incubacion: float = 5.0,
        dias_infeccion: float = 10.0,
        dias_inmunidad: float = 90.0,
        tasa_mortalidad: float = 0.015,
        eficacia_vacuna: float = 0.85,
        tasa_mutacion: float = 0.008,
        radio_contagio: float = 2.5,
        dias_simulacion: int = 180
    ):
        self.poblacion_total = poblacion_total
        self.infectados_iniciales = infectados_iniciales
        self.vacunados_iniciales = vacunados_iniciales
        self.beta = tasa_transmision_base
        self.sigma = 1.0 / dias_incubacion if dias_incubacion > 0 else 1.0
        self.gamma = 1.0 / dias_infeccion if dias_infeccion > 0 else 1.0
        self.omega = 1.0 / dias_inmunidad if dias_inmunidad > 0 else 0.0
        self.mu = tasa_mortalidad
        self.eficacia_vacuna = eficacia_vacuna
        self.tasa_mutacion = tasa_mutacion
        self.radio_contagio = radio_contagio
        self.dias_simulacion = dias_simulacion

    def calcular_r0_teorico(self) -> float:
        """Calcula el Número Reproductivo Básico (R0 = beta / gamma)."""
        if self.gamma == 0:
            return float('inf')
        return self.beta / self.gamma

    def calcular_umbral_inmunidad_rebano(self) -> float:
        """Calcula el porcentaje de población inmune necesario para detener el brote."""
        r0 = self.calcular_r0_teorico()
        if r0 <= 1.0:
            return 0.0
        return (1.0 - (1.0 / r0)) * 100.0

    def validar_parametros(self) -> bool:
        """Verifica que los parámetros biológicos sean coherentes."""
        if self.poblacion_total <= 0:
            raise ValueError("La población total debe ser mayor que cero.")
        if self.infectados_iniciales + self.vacunados_iniciales > self.poblacion_total:
            raise ValueError("Infectados + Vacunados iniciales superan la población.")
        if not (0.0 <= self.eficacia_vacuna <= 1.0):
            raise ValueError("La eficacia de la vacuna debe estar entre 0 y 1.")
        if not (0.0 <= self.tasa_mortalidad <= 1.0):
            raise ValueError("La tasa de mortalidad debe estar entre 0 y 1.")
        return True

    def to_dict(self) -> Dict:
        """Exporta los parámetros a un diccionario serializable."""
        return {
            "poblacion_total": self.poblacion_total,
            "infectados_iniciales": self.infectados_iniciales,
            "vacunados_iniciales": self.vacunados_iniciales,
            "beta_transmision": round(self.beta, 4),
            "sigma_incubacion": round(self.sigma, 4),
            "gamma_recuperacion": round(self.gamma, 4),
            "omega_perdida_inmunidad": round(self.omega, 4),
            "tasa_mortalidad": self.mu,
            "eficacia_vacuna": self.eficacia_vacuna,
            "tasa_mutacion": self.tasa_mutacion,
            "R0_teorico": round(self.calcular_r0_teorico(), 3),
            "umbral_inmunidad_rebano_pct": round(self.calcular_umbral_inmunidad_rebano(), 2)
        }


# ==============================================================================
# SECCIÓN 2: MODELO DETERMINISTA (ECUACIONES DIFERENCIALES - RUNGE-KUTTA 4)
# ==============================================================================

class ModeloDeterministaSEIRV:
    """
    Resuelve el sistema de Ecuaciones Diferenciales Ordinarias (EDO) para el
    modelo SEIRV utilizando el método numérico de Runge-Kutta de 4to orden.
    """
    def __init__(self, params: ParametrosBiologicos):
        self.params = params
        self.historial: List[Dict[str, float]] = []

    def _derivadas(self, estado: Tuple[float, float, float, float, float, float]) -> Tuple[float, ...]:
        """
        Calcula las tasas de cambio instantáneas (dS/dt, dE/dt, dI/dt, dR/dt, dV/dt, dD/dt).
        """
        S, E, I, R, V, D = estado
        N_vivos = S + E + I + R + V
        if N_vivos <= 0:
            return (0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

        p = self.params
        fuerza_infeccion = p.beta * I / N_vivos
        fuerza_infeccion_vac = p.beta * (1.0 - p.eficacia_vacuna) * I / N_vivos

        dS = -fuerza_infeccion * S + p.omega * R + (p.omega * 0.5) * V
        dE = fuerza_infeccion * S + fuerza_infeccion_vac * V - p.sigma * E
        dI = p.sigma * E - p.gamma * I - (p.mu * p.gamma) * I
        dR = p.gamma * I - p.omega * R
        dV = -fuerza_infeccion_vac * V - (p.omega * 0.5) * V
        dD = (p.mu * p.gamma) * I

        return (dS, dE, dI, dR, dV, dD)

    def _paso_rk4(self, estado: Tuple[float, ...], dt: float) -> Tuple[float, ...]:
        """Ejecuta un paso de integración numérica Runge-Kutta de cuarto orden."""
        k1 = self._derivadas(estado)

        estado_k2 = tuple(estado[i] + 0.5 * dt * k1[i] for i in range(6))
        k2 = self._derivadas(estado_k2)

        estado_k3 = tuple(estado[i] + 0.5 * dt * k2[i] for i in range(6))
        k3 = self._derivadas(estado_k3)

        estado_k4 = tuple(estado[i] + dt * k3[i] for i in range(6))
