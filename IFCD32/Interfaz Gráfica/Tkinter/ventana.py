import tkinter as tk

root = tk.Tk()
root.title("Formulario")
root.geometry("300x150")

tk.Label(root, text="Nombre:").grid(row=0, column=0, sticky="e")
tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text="Edad:").grid(row=1, column=0, sticky="e")
tk.Entry(root).grid(row=1, column=1)

tk.Button(root, text="Enviar").grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()