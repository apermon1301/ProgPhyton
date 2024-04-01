import tkinter as tk
from tkinter import ttk
import sys

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.contador=0
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1= tk.Menu(menubar1)
        opciones1=tk.Menu(menubar1, tearoff=0)
        self.label1=ttk.Label(text="Nombre:")
        self.label1.grid(column=0, row=0)
        self.label2=ttk.Label(text="Nota:")
        self.label2.grid(column=0, row=1)
        self.nombre=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana1, width=10, textvariable=self.nombre)
        self.entry1.grid(column=1, row=0)
        self.nota=tk.StringVar()
        self.entry2=ttk.Entry(self.ventana1, width=10, textvariable=self.nota)
        self.entry2.grid(column=1, row=1)


        self.boton1=ttk.Button(self.ventana1, text="Insertar",command=self.insertar)
        self.boton1.grid(column=0, row=2)
        self.boton2=ttk.Button(self.ventana1, text="Eliminar",command=self.eliminar)
        self.boton2.grid(column=1,row=2)
        self.listbox1=tk.Listbox(self.ventana1)
        self.listbox1.grid(column=0, row=3, columnspan=2, sticky="we")
        self.ventana1.mainloop()
        def finalizar(self):
            sys.exit()

        def insertar(self):
            dato=self.dato1.get()+"-"+self.dato2.get()
            self.listbox1.insert(self.contador,dato)
            self.contador=self.contador+1
            
        def eliminar(self):
            if len(self.listbox1.curselection())!=0:
                item=self.listbox1.curselection()[0]
                self.listbox1.delete(item)
                self.contador=self.contador-1
                                            

aplicacion1=Aplicacion()
