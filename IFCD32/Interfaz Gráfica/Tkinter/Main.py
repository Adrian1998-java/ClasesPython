import tkinter as tk  # Importar Tkinter

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera app")
ventana.geometry("300x150")  # Tamaño: ancho x alto

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="¡Hola, Tkinter!", font=("Arial", 14))
etiqueta.pack(pady=10)  # Mostrar la etiqueta con un poco de espacio vertical

# Función que se ejecuta al hacer clic
def al_hacer_clic():
    etiqueta.config(text="¡Has hecho clic!")

# Botón con una función asociada
boton = tk.Button(ventana, text="Haz clic", command=al_hacer_clic)
boton.pack()

# Iniciar el programa (bucle de eventos)
ventana.mainloop()