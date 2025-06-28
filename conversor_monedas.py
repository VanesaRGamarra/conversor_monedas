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



ventana.mainloop()