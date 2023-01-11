import os
import tkinter as tk

with open("0.utf", "r") as f:
    lineas = f.readlines()

window = tk.Tk()
window.title("Editor de archivo")

lista = tk.StringVar(window)
lista.set(lineas)

filteredLines = []

for i in range(7073, len(lineas)):
    if "langen^" in lineas[i] or "langen!" in lineas[i]:
        filteredLines.append(str(i) + '===' + lineas[i])

marco = tk.Frame(window)
marco.pack()

editor = tk.Text(marco, width=300, height=25, padx=3, pady=3)
editor.pack(side=tk.LEFT)

editor.delete("1.0", tk.END)
for linea in filteredLines:
    editor.insert(tk.END, linea)


def guardar_cambios():
    i = 2.0
    total_changes = 0

    while i <= len(filteredLines):
        line = editor.get(str(i - 1.0), str(i))
        index, line = line.split('===')
        j = int(index)
        if lineas[j] != line:
            lineas[j] = line
            total_changes += 1
        i += 1.0
        print(f"Total Changes: {total_changes}")
    with open("0.utf", "w") as f:
        # Escribir las líneas en el archivo
        f.writelines(lineas)


# Crear un botón para guardar los cambios
boton = tk.Button(window, text="Guardar cambios", command=guardar_cambios)
boton.pack()

# Iniciar el bucle de eventos de Tkinter
window.mainloop()
