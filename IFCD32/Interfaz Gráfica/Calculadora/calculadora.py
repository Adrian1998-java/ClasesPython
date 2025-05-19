import tkinter as tk
from modulo import operaciones as op

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

# Creamos los campos de entrada, y el combobox con las operaciones
texto1 = tk.Entry(ventana, width=20, font=("Arial", 16))
texto1.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
texto2 = tk.Entry(ventana, width=20, font=("Arial", 16))
texto2.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
texto_resultado = tk.Message(ventana, text="Resultado", font=("Arial", 16))
texto_resultado.grid(row=3, column=0, columnspan=4, padx=20, pady=10)

operaciones = ["+", "-", "*", "/"]
combo = tk.StringVar()
combo.set(operaciones[0])
combo_box = tk.OptionMenu(ventana, combo, *operaciones)
combo_box.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# Función para realizar la operación
def calcular():
    try:
        num1 = float(texto1.get())
        num2 = float(texto2.get())
        operacion = combo.get()
        if operacion == "+":
            resultado = op.suma(num1, num2)
        elif operacion == "-":
            resultado = op.resta(num1, num2)
        elif operacion == "*":
            resultado = op.multiplicacion(num1, num2)
        elif operacion == "/":
            resultado = op.division(num1, num2)
        else:
            resultado = "Operación no válida"
        texto_resultado.config(text=f"{resultado:.2f}")
    except ValueError:
        texto_resultado.config(text=f"{resultado:.2f}")
        
        
# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.grid(row=4, column=0, columnspan=4, padx=10, pady=10)
# Botón para limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=lambda: texto1.delete(0, tk.END))
boton_limpiar.grid(row=5, column=0, columnspan=4, padx=10, pady=10)
# Botón para salir
boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

ventana.mainloop()





