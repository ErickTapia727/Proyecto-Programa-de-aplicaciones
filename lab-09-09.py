"""
lab-09-09.py
-----------------
Ingenieria Civil en Computacion e Informatica - Programacion de Aplicaciones 2026-2
Prof. Rodolfo Canelón

Ejercicios de uso de datos con Parquet.

Descriptor de datos:
Alumno,Carrera,Arancel,Año_Ingreso,Periodo,Año,Semestre,Financiamiento,
Residencia,Sexo,Asistencia,Promedio_Notas,Trabaja,Desertar

Funcionalidades (implementadas con botones de Tkinter):
1) Mostrar los indices academicos de los estudiantes de ICCI, calcular el
   promedio y ordenarlos descendientemente.
2) Obtener los alumnos del semestre "Nivel 4" de la Carrera
   "Ingenieria Civil Informatica".
"""

import os
import tkinter as tk
from tkinter import messagebox, ttk

import numpy as np
import pandas as pd
import polars as pl

ARCHIVO_PARQUET = "datos_estudiantes.parquet"
CARRERA_ICCI = "Ingeniería Civil Informática"


def cargar_datos():
    """Carga el archivo parquet con pandas. Si no existe, se avisa al usuario."""
    if not os.path.exists(ARCHIVO_PARQUET):
        raise FileNotFoundError(
            f"No se encontró '{ARCHIVO_PARQUET}'. "
            "Ejecuta primero 'generar_datos.py' para crearlo."
        )
    return pd.read_parquet(ARCHIVO_PARQUET)


def obtener_indices_icci(df):
    """
    Filtra los estudiantes de ICCI, calcula el promedio de notas y
    los ordena de forma descendiente por Promedio_Notas.
    """
    icci = df[df["Carrera"] == CARRERA_ICCI].copy()
    promedio_general = np.mean(icci["Promedio_Notas"]) if len(icci) else 0.0
    icci_ordenado = icci.sort_values(by="Promedio_Notas", ascending=False)
    return icci_ordenado, promedio_general


def obtener_alumnos_nivel4_icci(df):
    """
    Utiliza polars para obtener los alumnos del semestre "Nivel 4" de la
    carrera Ingenieria Civil Informatica.
    """
    tabla = pl.from_pandas(df)
    filtrado = tabla.filter(
        (pl.col("Semestre") == "Nivel 4") & (pl.col("Carrera") == CARRERA_ICCI)
    )
    return filtrado.to_pandas()


class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicios de uso de datos con Parquet - ICCI")
        self.geometry("900x500")

        self.df = None
        self._cargar_dataframe_inicial()

        titulo = tk.Label(
            self,
            text="Programación de Aplicaciones - Ejercicios con Parquet",
            font=("Arial", 14, "bold"),
        )
        titulo.pack(pady=10)

        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=5)

        btn_indices = tk.Button(
            frame_botones,
            text="Índices académicos ICCI (ordenados desc.)",
            command=self.mostrar_indices_icci,
            width=45,
        )
        btn_indices.grid(row=0, column=0, padx=5, pady=5)

        btn_nivel4 = tk.Button(
            frame_botones,
            text='Alumnos "Nivel 4" - Ingeniería Civil Informática',
            command=self.mostrar_alumnos_nivel4,
            width=45,
        )
        btn_nivel4.grid(row=0, column=1, padx=5, pady=5)

        self.label_promedio = tk.Label(self, text="Promedio general ICCI: -", font=("Arial", 11))
        self.label_promedio.pack(pady=5)

        columnas = list(pd.read_parquet(ARCHIVO_PARQUET).columns) if os.path.exists(ARCHIVO_PARQUET) else []
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings")
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100, anchor="center")
        self.tabla.pack(expand=True, fill="both", padx=10, pady=10)

    def _cargar_dataframe_inicial(self):
        try:
            self.df = cargar_datos()
        except FileNotFoundError as error:
            self.df = None
            messagebox.showerror("Datos no encontrados", str(error))

    def _llenar_tabla(self, df):
        self.tabla.delete(*self.tabla.get_children())
        self.tabla["columns"] = list(df.columns)
        for col in df.columns:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100, anchor="center")
        for _, fila in df.iterrows():
            self.tabla.insert("", "end", values=list(fila))

    def mostrar_indices_icci(self):
        if self.df is None:
            messagebox.showerror("Error", "No hay datos cargados.")
            return
        icci_ordenado, promedio_general = obtener_indices_icci(self.df)
        if icci_ordenado.empty:
            messagebox.showinfo("Sin resultados", "No hay estudiantes de ICCI.")
            return
        self._llenar_tabla(icci_ordenado)
        self.label_promedio.config(
            text=f"Promedio general ICCI: {promedio_general:.2f}"
        )

    def mostrar_alumnos_nivel4(self):
        if self.df is None:
            messagebox.showerror("Error", "No hay datos cargados.")
            return
        alumnos_nivel4 = obtener_alumnos_nivel4_icci(self.df)
        if alumnos_nivel4.empty:
            messagebox.showinfo(
                "Sin resultados",
                'No hay alumnos de "Nivel 4" en Ingeniería Civil Informática.',
            )
            return
        self._llenar_tabla(alumnos_nivel4)
        self.label_promedio.config(text=f"Alumnos encontrados: {len(alumnos_nivel4)}")


if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
