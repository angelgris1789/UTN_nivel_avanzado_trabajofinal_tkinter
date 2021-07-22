import tkinter as tk
from tkinter import ttk
from tkinter.constants import END
from val import validar
from mysql.connector.errors import DatabaseError
from models import Model
from views import View
import observer
import log


class Controller(observer.Tema):
    def __init__(self):
        observador1 = log.Log(self)
        self.root = tk.Tk()
        self.model = Model()
        self.view = View(self.root, self)
        self.root.title("Inventario SAP")
        self.root.geometry("1200x500")

        self.root.mainloop()

    def alta(self, *args, **kwargs):
        try:
            self.model = Model()
            if validar(args[0]) == True:
                self.model.agregar(self, args[0], args[1], args[2], args[3], args[4])
                self.mostrar(self.view.viewPanel.tvw_insumos)
            else:
                self.view.viewPanel.lbl_error.config(text="Los datos no son correctos")
        except DatabaseError:
            self.view.viewPanel.lbl_error.config(
                text="Se debe colocar codigo valido",
                bg="red",
                foreground="white",
            )
            self.view.viewPanel.lbl_error.config(text="Los datos no son correctos")
        self.notificar(args[0], "alta")

    def baja(self, codigosap):
        self.model = Model()
        self.model.borrar(codigosap["text"])
        self.mostrar(self.view.viewPanel.tvw_insumos)
        self.notificar(codigosap["text"], "baja")

    def modificar(self, *args, **kwargs):
        if validar(args[3]) == True:
            self.model = Model()
            self.model.modificar(self, args)
            self.mostrar(self.view.viewPanel.tvw_insumos)
        else:
            self.view.viewPanel.lbl_error.config(text="Los datos no son correctos")

        self.notificar(args[0], "modificacion")

    def mostrar(self, tree):
        self.model = Model()
        data = self.model.traer_datos(tree)
        for row in data:
            tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4]))

    def cargar_form(self, *args, **kwargs):
        tree = self.view.viewPanel
        self.datos = tree.tvw_insumos.item(tree.tvw_insumos.focus())
        self.lista = self.datos["values"]
        self.restablecer()
        try:
            if self.datos["text"] != "":
                tree.ent_codigo.insert(0, self.datos["text"])
                tree.ent_desc.insert(0, self.lista[0])
                tree.ent_ubic.insert(0, self.lista[1])
                tree.ent_cant.insert(0, self.lista[2])
                tree.ent_precio.insert(0, self.lista[3])
        except ():
            pass

    def restablecer(self):
        tree = self.view.viewPanel
        tree.ent_codigo.delete(0, END)
        tree.ent_desc.delete(0, END)
        tree.ent_ubic.delete(0, END)
        tree.ent_cant.delete(0, END)
        tree.ent_precio.delete(0, END)
