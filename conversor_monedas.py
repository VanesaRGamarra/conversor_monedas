import tkinter as tk
from tkinter import ttk, Frame, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Ventana principal

ventana = ttk.Window(themename="superhero")
ventana.title('Conversor de Monedas')
ventana.geometry('800x400')
ventana.configure(bg="LightSteelBlue")
ventana.resizable(True, False)
ventana.iconbitmap("Logogrupo 6.ico")

# Pestañas
notebook = ttk.Notebook(ventana)
notebook.pack(fill='both',expand='yes')

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text='Conversor de monedas')
notebook.add(tab2, text='Lista de monedas')


# Diccionario con tasas de cambio simuladas (valores de ejemplo)
tasas_cambio = {
    "USD": 1190,
    "EUR": 1392,
    "GBP": 1568,
    "JPY": 10,
    "AUD": 776,
    "CAD": 886
}


ventana.mainloop()
