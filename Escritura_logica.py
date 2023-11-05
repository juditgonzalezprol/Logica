import tkinter as tk
from tkinter import ttk

def agregar_simbolo(simbolo):
    entrada_proposicion.insert(tk.END, simbolo)

def borrar_proposicion():
    entrada_proposicion.delete(1.0, tk.END)

root = tk.Tk()
root.title("Editor de Lógica")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0)

etiqueta = ttk.Label(frame, text="Proposición Lógica:")
etiqueta.grid(row=0, column=0, columnspan=4)

entrada_proposicion = tk.Text(frame, width=30, height=2)
entrada_proposicion.grid(row=1, column=0, columnspan=4)

simbolos = ["∨", "∧", "¬", "→", "↔", "∃", "∀", "⊨", "p", "q", "r", "φ", "Γ"]
row = 2
column = 0

for simbolo in simbolos:
    boton = ttk.Button(frame, text=simbolo, command=lambda s=simbolo: agregar_simbolo(s))
    boton.grid(row=row, column=column)
    column += 1
    if column == 4:
        column = 0
        row += 1

boton_borrar = ttk.Button(frame, text="Borrar", command=borrar_proposicion)
boton_borrar.grid(row=row, column=column, columnspan=4)

root.mainloop()

