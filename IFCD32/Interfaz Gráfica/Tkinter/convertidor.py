import tkinter as tk
from tkinter import ttk, messagebox

# Función para realizar la conversión
def convertir():
    try:
        valor = float(entrada_valor.get())
        tipo = variable_tipo.get()
        unidad = combo_unidad.get()

        if tipo == "Temperatura":
            if unidad == "Celsius a Fahrenheit":
                resultado = valor * 9/5 + 32
            elif unidad == "Fahrenheit a Celsius":
                resultado = (valor - 32) * 5/9
        elif tipo == "Longitud":
            if unidad == "Metros a Pies":
                resultado = valor * 3.28084
            elif unidad == "Pies a Metros":
                resultado = valor / 3.28084
        elif tipo == "Peso":
            if unidad == "Kilogramos a Libras":
                resultado = valor * 2.20462
            elif unidad == "Libras a Kilogramos":
                resultado = valor / 2.20462
        else:
            resultado = "Unidad no válida"

        etiqueta_resultado.config(text=f"Resultado: {resultado:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número válido.")

# Actualizar las opciones según el tipo seleccionado
def actualizar_unidades():
    tipo = variable_tipo.get()
    unidades = []
    if tipo == "Temperatura":
        unidades = ["Celsius a Fahrenheit", "Fahrenheit a Celsius"]
    elif tipo == "Longitud":
        unidades = ["Metros a Pies", "Pies a Metros"]
    elif tipo == "Peso":
        unidades = ["Kilogramos a Libras", "Libras a Kilogramos"]
    combo_unidad['values'] = unidades
    combo_unidad.current(0)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Unidades")
ventana.geometry("400x250")
ventana.resizable(False, False)

# Marco principal
frame = tk.Frame(ventana, padx=10, pady=10)
frame.pack(fill="both", expand=True)

# Entrada de valor
tk.Label(frame, text="Valor a convertir:").grid(row=0, column=0, sticky="e")
entrada_valor = tk.Entry(frame)
entrada_valor.grid(row=0, column=1)

# Tipo de conversión
tk.Label(frame, text="Tipo de unidad:").grid(row=1, column=0, sticky="e")
variable_tipo = tk.StringVar(value="Temperatura")

opciones_tipo = ["Temperatura", "Longitud", "Peso"]
fila_tipo = 2
for i, opcion in enumerate(opciones_tipo):
    tk.Radiobutton(frame, text=opcion, variable=variable_tipo, value=opcion, command=actualizar_unidades).grid(row=fila_tipo, column=i, pady=5)

# Selección de unidad específica
tk.Label(frame, text="Conversión:").grid(row=4, column=0, sticky="e")
combo_unidad = ttk.Combobox(frame, state="readonly")
combo_unidad.grid(row=4, column=1, pady=5)

# Botón de conversión
boton_convertir = tk.Button(frame, text="Convertir", command=convertir)
boton_convertir.grid(row=5, column=0, columnspan=3, pady=10)

# Etiqueta de resultado
etiqueta_resultado = tk.Label(frame, text="Resultado: ")
etiqueta_resultado.grid(row=6, column=0, columnspan=3)

# Inicializar unidades
actualizar_unidades()

# Ejecutar la aplicación
ventana.mainloop()
