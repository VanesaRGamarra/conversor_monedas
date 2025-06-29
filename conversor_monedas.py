import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Ventana principal
ventana = ttk.Window(themename="superhero")
ventana.title('Conversor de Monedas')
ventana.geometry('800x400')
ventana.configure(bg="LightSteelBlue")
ventana.resizable(True, False)
ventana.iconbitmap("Logogrupo 6.ico")
# Diccionario con tasas de cambio simuladas
tasas_cambio = {
    "USD": 1190,
    "EUR": 1392,
    "GBP": 1568,
    "JPY": 10,
    "AUD": 776,
    "CAD": 886
}

# Función para convertir moneda
def convertir():
    try:
        cantidad = float(ingreso_cantidad.get())
        moneda = combo_convertir.get()

        if moneda in tasas_cambio:
            resultado = round(cantidad * tasas_cambio[moneda], 2)
            cambio_moneda.config(text=f"${resultado}")
        else:
            cambio_moneda.config(text="Seleccione moneda")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una cantidad válida.")

# Función para actualizar moneda
def actualizar_Monedas():
    try:
        clave = combo_actualizar.get()
        nuevo_valor = float(nuevo_precio.get())

        if clave in tasas_cambio:
            tasas_cambio[clave] = nuevo_valor
            mostrar_lista()
            mostrar_diccionario()
            messagebox.showinfo("Éxito", f"El valor de '{clave}' se ha actualizado a ${nuevo_valor}.")
        else:
            messagebox.showerror("Error", f"La moneda '{clave}' no existe.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una cantidad válida.")

# Mostrar lista de monedas
def mostrar_lista():
    lista.delete(0, tk.END)
    for clave, valor in tasas_cambio.items():
        lista.insert(tk.END, f"1 {clave} = ${valor}")

# Mostrar diccionario en texto en tab3
def mostrar_diccionario():
    texto_moneda = "\n".join([f"1 {k} = ${v}" for k, v in tasas_cambio.items()])
    etiqueta_diccionario.config(text=f"MONEDAS DISPONIBLES:\n{texto_moneda}")

# Crear pestañas
notebook = ttk.Notebook(ventana)
notebook.pack(fill='both', expand='yes')

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

notebook.add(tab1, text='Conversor de monedas')
notebook.add(tab2, text='Lista de monedas')
notebook.add(tab3, text="Editar monedas")

# ---------- TAB 1: Conversión ----------
tk.Label(tab1, text="CONVERSOR DE MONEDAS", font="Helvetica 20 bold",
         bg="LightSteelBlue", fg="DarkSlateGray", relief=tk.GROOVE,
         bd=0.5, padx=10, pady=10).pack(pady=20)

cuadro1 = tk.Frame(tab1, bg="LightSteelBlue")
cuadro1.pack(pady=10)

tk.Label(cuadro1, text="Cantidad:", font=('Helvetica', 16), bg="LightSteelBlue").grid(row=0, column=0, padx=10)
ingreso_cantidad = tk.Entry(cuadro1, font="Helvetica 16", justify="right", width=10)
ingreso_cantidad.grid(row=0, column=1)
ingreso_cantidad.insert(0, "1")

combo_convertir = ttk.Combobox(cuadro1, values=list(tasas_cambio.keys()), font="Helvetica 16", width=6, state="readonly")
combo_convertir.grid(row=0, column=2, padx=10)
combo_convertir.set("USD")

cuadro2 = tk.Frame(tab1, bg="LightSteelBlue")
cuadro2.pack(pady=10)

tk.Label(cuadro2, text="Convertido a Pesos ARS:", font=('Helvetica', 16), bg="LightSteelBlue").pack(side=tk.LEFT)
cambio_moneda = tk.Label(cuadro2, text="$0.00", font="Helvetica 18 bold", bg="white",
                         width=14, relief=tk.SUNKEN, anchor='e')
cambio_moneda.pack(side=tk.LEFT, padx=10)

tk.Button(tab1, text="Convertir", font="Helvetica 14", command=convertir).pack(pady=10)

# ---------- TAB 2: Lista ----------
tk.Button(tab2, text="Ver lista de monedas extranjeras", command=mostrar_lista).pack(pady=10)

marco_lista = tk.Frame(tab2)
marco_lista.pack(pady=10)

scrollbar = tk.Scrollbar(marco_lista)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista = tk.Listbox(marco_lista, yscrollcommand=scrollbar.set, width=40, font="Helvetica 12")
lista.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=lista.yview)

# ---------- TAB 3: Editar monedas ----------
tk.Label(tab3, text="ACTUALIZAR EL VALOR DE LAS MONEDAS", font="Helvetica 20 bold",
         bg="LightSteelBlue", fg="DarkSlateGray", relief=tk.GROOVE,
         bd=0.5, padx=10, pady=10).pack(pady=20)

etiqueta_diccionario = tk.Label(tab3, text="", wraplength=350, justify="left", bg="LightSteelBlue", font=("Helvetica", 12))
etiqueta_diccionario.pack(pady=10)
mostrar_diccionario()

cuadro3 = tk.Frame(tab3, bg="LightSteelBlue")
cuadro3.pack(pady=10)

tk.Label(cuadro3, text="Nuevo valor:", font=('Helvetica', 16), bg="LightSteelBlue").grid(row=0, column=0, padx=10)
nuevo_precio = tk.Entry(cuadro3, font="Helvetica 16", justify="right", width=10)
nuevo_precio.grid(row=0, column=1)

combo_actualizar = ttk.Combobox(cuadro3, values=list(tasas_cambio.keys()), font="Helvetica 16", width=6, state="readonly")
combo_actualizar.grid(row=0, column=2, padx=10)
combo_actualizar.set("USD")

tk.Button(tab3, text="Actualizar", font="Helvetica 14", command=actualizar_Monedas).pack(pady=10)

ventana.mainloop()

