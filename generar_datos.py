"""
generar_datos.py
-----------------
Ingenieria Civil en Computacion e Informatica - Programacion de Aplicaciones
Genera un archivo Parquet de ejemplo con el descriptor solicitado:

Alumno,Carrera,Arancel,Año_Ingreso,Periodo,Año,Semestre,Financiamiento,
Residencia,Sexo,Asistencia,Promedio_Notas,Trabaja,Desertar

Ejecutar una sola vez para crear datos_estudiantes.parquet antes de usar
lab-09-09.py
"""

import numpy as np
import pandas as pd

np.random.seed(42)

CARRERAS = [
    "Ingeniería Civil Informática",
    "Ingeniería Civil Industrial",
    "Ingeniería Civil Eléctrica",
    "Ingeniería Comercial",
]

SEMESTRES = ["Nivel 1", "Nivel 2", "Nivel 3", "Nivel 4", "Nivel 5", "Nivel 6"]
FINANCIAMIENTO = ["Beca", "Credito", "Particular"]
RESIDENCIA = ["Urbana", "Rural"]
SEXO = ["Masculino", "Femenino"]

N = 200

data = {
    "Alumno": [f"Alumno_{i:03d}" for i in range(1, N + 1)],
    "Carrera": np.random.choice(CARRERAS, N),
    "Arancel": np.random.randint(1_200_000, 3_500_000, N),
    "Año_Ingreso": np.random.randint(2018, 2026, N),
    "Periodo": np.random.choice([1, 2], N),
    "Año": np.random.randint(2022, 2027, N),
    "Semestre": np.random.choice(SEMESTRES, N),
    "Financiamiento": np.random.choice(FINANCIAMIENTO, N),
    "Residencia": np.random.choice(RESIDENCIA, N),
    "Sexo": np.random.choice(SEXO, N),
    "Asistencia": np.round(np.random.uniform(50, 100, N), 1),
    "Promedio_Notas": np.round(np.random.uniform(3.0, 7.0, N), 1),
    "Trabaja": np.random.choice(["Si", "No"], N),
    "Desertar": np.random.choice(["Si", "No"], N, p=[0.15, 0.85]),
}

df = pd.DataFrame(data)
df.to_parquet("datos_estudiantes.parquet", index=False)
print("Archivo 'datos_estudiantes.parquet' generado con", len(df), "registros.")
