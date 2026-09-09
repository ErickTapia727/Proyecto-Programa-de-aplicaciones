# Proyecto-Programa-de-aplicaciones

## Ejercicios de uso de datos con Parquet (ICCI)

Programa en Python que usa Tkinter, pandas, numpy, polars y matplotlib para
trabajar con datos de estudiantes almacenados en formato Parquet.

### Cómo ejecutar el programa

1. Clona o descarga este repositorio, de modo que tengas los archivos
   `requirements.txt`, `generar_datos.py` y `lab-09-09.py` en la misma carpeta.

2. Abre una terminal en esa carpeta.

3. Asegúrate de tener Python 3 instalado, con Tkinter incluido:
   - En Windows/Mac, el instalador oficial de [python.org](https://www.python.org/) ya incluye Tkinter.
   - En Linux puede ser necesario instalarlo aparte:
     ```
     sudo apt install python3-tk
     ```

4. Instala las librerías necesarias:
   ```
   pip install -r requirements.txt
   ```

5. Genera los datos de ejemplo (crea el archivo `datos_estudiantes.parquet`):
   ```
   python generar_datos.py
   ```

6. Ejecuta el programa principal, que abrirá la ventana de Tkinter con los botones:
   ```
   python lab-09-09.py
   ```

**Notas:**
- El programa debe ejecutarse en un equipo con entorno de escritorio, ya que Tkinter necesita una interfaz gráfica para mostrar la ventana.
- En Windows el comando puede ser `python` o `py`; en Mac/Linux normalmente es `python3`.
- Ejecuta siempre `generar_datos.py` antes que `lab-09-09.py`, ya que este último necesita el archivo `datos_estudiantes.parquet` generado en el paso anterior.