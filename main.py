import openpyxl

# PARTE 1: Crear diccionario y entrada de datos
# Crea un diccionario vacío llamado 'estudiantes'
# Usa un ciclo for para pedir 3 nombres y notas (convierte la nota a float)
# Guarda cada par nombre-nota en el diccionario
# --- Escribe tu código aquí ---
estudiantes = {}

for i in range(3):
    nombre = input("Nombre: ")
    nota = float(input("Nota: "))
    estudiantes[nombre] = nota

# PARTE 2: Crear archivo Excel
# Crea un nuevo libro de trabajo
libro = openpyxl.Workbook()
# Obtén la hoja activa
hoja = libro.active

# PARTE 3: Escribir encabezado
# Escribe "Nombres cortos (<=4 letras)" en A1
# --- Escribe tu código aquí ---
hoja["A1"] = "Nombres cortos (<=4 letras)"

# PARTE 4: Escribir nombres cortos con ciclo y condicional
fila = 2
# Usa un ciclo for para recorrer el diccionario
# Si el nombre tiene <= 4 letras, escríbelo en la columna A y aumenta 'fila'
# --- Escribe tu código aquí ---
for nombre in estudiantes:
    if len(nombre) <= 4:
        hoja[f"A{fila}"] = nombre
        fila += 1

# PARTE 5: Guardar archivo
# Guarda el archivo como "ejercicio4.xlsx"
# --- Escribe tu código aquí ---
libro.save("ejercicio4.xlsx")
print("¡Ejercicio 4 guardado en ejercicio4.xlsx!")