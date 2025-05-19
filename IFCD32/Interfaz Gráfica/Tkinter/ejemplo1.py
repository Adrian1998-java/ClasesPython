import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Mini Editor de Texto")
ventana.geometry("600x400")

# Crear área de texto con scroll
texto = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, font=("Arial", 12))
texto.pack(expand=True, fill="both")

# Funciones de los menús
def nuevo_archivo():
    if messagebox.askyesno("Nuevo", "¿Deseas borrar el contenido actual?"):
        texto.delete("1.0", tk.END)

def abrir_archivo():
    archivo = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if archivo:
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
        texto.delete("1.0", tk.END)
        texto.insert(tk.END, contenido)

def guardar_archivo():
    archivo = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if archivo:
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(texto.get("1.0", tk.END))
        messagebox.showinfo("Guardar", "Archivo guardado con éxito.")

def salir():
    if messagebox.askokcancel("Salir", "¿Deseas salir del editor?"):
        ventana.destroy()

# Crear la barra de menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Menú Archivo
menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Nuevo", command=nuevo_archivo)
menu_archivo.add_command(label="Abrir...", command=abrir_archivo)
menu_archivo.add_command(label="Guardar", command=guardar_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

# Ejecutar la aplicación
ventana.mainloop()