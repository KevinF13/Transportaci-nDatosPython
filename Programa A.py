import tkinter as tk
from tkinter import messagebox
import pandas as pd

def guardar_como_csv():
    data = {
        'Campo1': [campo1.get()],
        'Campo2': [campo2.get()],
        'Campo3': [campo3.get()]
    }
    df = pd.DataFrame(data)
    df.to_csv('datos.csv', index=False)
    messagebox.showinfo("Éxito", "Datos guardados en datos.csv")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Programa A")

# Campos de entrada de texto
tk.Label(root, text="Nombre:").pack()
campo1 = tk.Entry(root)
campo1.pack()

tk.Label(root, text="Apellido:").pack()
campo2 = tk.Entry(root)
campo2.pack()

tk.Label(root, text="Edad:").pack()
campo3 = tk.Entry(root)
campo3.pack()

# Botón para guardar como CSV
boton_guardar = tk.Button(root, text="Guardar como CSV", command=guardar_como_csv)
boton_guardar.pack()

root.mainloop()
