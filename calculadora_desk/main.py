import tkinter as tk
from tkinter import messagebox, font, DoubleVar, StringVar
from functools import partial
import re
import sys

# Funciones
def validar_input(caracter):
    valido = True
    try:
        # Cuando le paso un resultado (varios caracteres)
        float(caracter)
        valido = True
    except ValueError:
        # Ingresos de teclado o botones
        if not caracter in '-.1234567890':
            valido = False
        else: 
            if len(ingreso.get()) > 0 and caracter == '-':
                valido = False
            elif len(ingreso.get()) > 0 \
                and ingreso.get().count('.') == 1 \
                and caracter == '.':
                valido = False
    return valido

def apagar():
    resp = messagebox.askokcancel(title="Pregunta", message="¿Desea salir?")
    if resp:
        sys.exit()

def borrar_todo():
    numero_1.set(0)
    numero_2.set(0)
    op_func.set('')
    ingreso.delete(0, tk.END)
    operacion.config(text="")

def borrar_ultimo():
    ingresos = ingreso.get()
    ingreso.delete(0, tk.END)
    ingreso.insert(0, ingresos[0:-1])
    
def operar(op="="):
    if operacion.cget('text') != '' and ingreso.get() != '':
        numero_2.set(float(ingreso.get()))
        etiqueta = operacion.cget('text') + str(numero_2.get()) + op
        ingreso.delete(0, tk.END)
        if op_func.get() == '+':
            resultado = numero_1.get() + numero_2.get()
        elif op_func.get() == '-':
            resultado = numero_1.get() - numero_2.get()
        elif op_func.get() == '*':
            resultado = round(numero_1.get() * numero_2.get(),2)
        elif op_func.get() == '/':
            try:
                resultado = round(numero_1.get() / numero_2.get(),2)
            except ZeroDivisionError:
                etiqueta = "Error"
                resultado = 0
        op_func.set(op)    
        numero_1.set(resultado)
            
        if op == '=' and etiqueta != 'Error':
            etiqueta = ''
            ingreso.delete(0, tk.END)
            ingreso.insert(tk.INSERT, str(resultado))
            
    else:        
        numero_1.set(float(ingreso.get()))                
        op_func.set(op)
        ingreso.delete(0, tk.END)
        etiqueta = str(numero_1.get()) + op
    
    operacion.config(text=etiqueta)

# Ventana Principal
ventana = tk.Tk()

# Ubicación de la ventana cuando se ejecuta la app
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()
ventana.geometry(f'+{int(screen_width/3)}+{int(screen_height/3)}')

# Registro función para validar sólo ingresos numéricos
validacion = ventana.register(validar_input)

# Etiqueta con operación
operacion = tk.Label(ventana,
                     width=30,
                     font=font.Font(family="Arial", size=12), 
                     justify=tk.RIGHT,
                     bg='lavender')
operacion.grid(row=0, columnspan=4)

# Variables globales para control de las operaciones
numero_1 = DoubleVar(value=0)
numero_2 = DoubleVar(value=0)
op_func = StringVar(value='')

# Input 
ingreso = tk.Entry(ventana,
                   validate="key", 
                   validatecommand=(validacion, '%S'),
                   font=font.Font(family="Arial", size=15), 
                   justify=tk.RIGHT)
ingreso.grid(row=1, columnspan=5, pady=5, padx=2, sticky="EW")

# Botones
borrar = tk.Button(text='C', 
                   width=5, 
                   font=font.Font(family="Arial", size=15), 
                   command=borrar_todo) 
borrar_dig = tk.Button(text='<<', 
                       width=5, 
                       font=font.Font(family="Arial", size=15),
                       command=borrar_ultimo) 
boton_off = tk.Button(text='Off', 
                      width=5, 
                      font=font.Font(family="Arial", size=15), 
                      bg="indianRed1",
                      command=apagar) 

borrar.grid(row=2, column=0, pady=3, padx=1)
borrar_dig.grid(row=2, column=2, pady=3, padx=1)
boton_off.grid(row=2, column=3, pady=3, padx=1)

def escribir(num):
    ingreso.insert(tk.END, num)
    
def convetir_negativo():
    negativo = -float(ingreso.get())
    ingreso.delete(0, tk.END)
    ingreso.insert(0, str(negativo))
    
numeros = [
    tk.Button(
        text=x, 
        width=5, 
        font=font.Font(family="Arial", size=15),
        command=partial(escribir, x)
        ) 
    for x in range(1, 10)
    ]

operaciones = [
    tk.Button(
        text=x, 
        width=5, 
        font=font.Font(family="Arial", size=15),
        command=partial(operar, x)
        ) 
    for x in ('+', '-', '*', '/')
    ]

fila = 3
for k in (8, 5, 2):
        numeros[k].grid(row=fila, column=0, pady=3, padx=1)
        numeros[k-1].grid(row=fila, column=1, pady=3, padx=1)
        numeros[k-2].grid(row=fila, column=2, pady=3, padx=1)
        fila += 1
        
for i in range(4):
    operaciones[i].grid(row=i+3, column=3, pady=3, padx=1)

cero = tk.Button(text=0, width=5, 
                 font=font.Font(family="Arial", size=15), 
                 command=partial(escribir, 0))
cero.grid(row=6, column=0, pady=3, padx=1)

punto = tk.Button(text='.', 
                  width=5, 
                  font=font.Font(family="Arial", size=15), 
                  command=partial(escribir, '.'))
punto.grid(row=6, column=1, pady=3, padx=1)

calcular = tk.Button(ventana,
                     text='=', 
                     width=5, 
                     font=font.Font(family="Arial", size=15), 
                     command=partial(operar, '='))
calcular.bind("<Return>", operar)
calcular.grid(row=6, column=2, pady=3, padx=1)

negativo = tk.Button(text='±', 
                     width=5, 
                     font=font.Font(family="Arial", size=15), 
                     command=partial(convetir_negativo))
negativo.grid(row=2, column=1, pady=3, padx=1)

def acerca_de():
    messagebox.showinfo(message='Calculadora desarrollada\npara "Acreditación de saberes"')

barra_menu = tk.Menu()
info = tk.Menu(barra_menu, tearoff=0)
info.add_command(label="Información", command=acerca_de)
barra_menu.add_cascade(label="Acerca de...", menu=info)

ventana.title("Calculadora")
ventana.config(menu=barra_menu)
ventana.mainloop()