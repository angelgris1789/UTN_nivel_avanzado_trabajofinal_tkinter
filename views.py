import tkinter as tk
from tkinter import Frame, ttk
from typing import Text
from models import Model


class View:
    def __init__(self, master, controller):
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.viewPanel = ViewPanel(master, controller)


class ViewPanel:
    def __init__(self, root, controller):
        self.controller = controller
        # controller.rellenar()
        self.framePanel = tk.Frame(root)
        self.framePanel.pack()
        self.btn_ingreso = tk.Button(self.framePanel, text="Ingresar")
        # self.btn_ingreso.grid(column=0, row=0)
        self.lbl_codigo = tk.Label(self.framePanel, text="CODIGO")
        self.lbl_codigo.grid(column=0, row=0)
        self.ent_codigo = tk.Entry(self.framePanel)
        self.ent_codigo.grid(column=0, row=1)
        self.lbl_desc = tk.Label(self.framePanel, text="Descriptcion")
        self.lbl_desc.grid(column=1, row=0)
        self.ent_desc = tk.Entry(self.framePanel)
        self.ent_desc.grid(column=1, row=1)
        self.lbl_ubic = tk.Label(self.framePanel, text="Deposito")
        self.lbl_ubic.grid(column=2, row=0)
        self.ent_ubic = tk.Entry(self.framePanel)
        self.ent_ubic.grid(column=2, row=1)
        self.lbl_cant = tk.Label(self.framePanel, text="Cantidad")
        self.lbl_cant.grid(column=3, row=0)
        self.ent_cant = tk.Entry(self.framePanel)
        self.ent_cant.grid(column=3, row=1)
        self.lbl_precio = tk.Label(self.framePanel, text="Precio")
        self.lbl_precio.grid(column=4, row=0)
        self.ent_precio = tk.Entry(self.framePanel)
        self.ent_precio.grid(column=4, row=1)
        self.btn_alta = tk.Button(
            self.framePanel,
            text="Alta",
            command=lambda: controller.alta(
                self.ent_codigo.get(),
                self.ent_desc.get(),
                self.ent_ubic.get(),
                self.ent_cant.get(),
                self.ent_precio.get(),
            ),
        )
        self.btn_alta.grid(column=0, row=3)

        self.btn_modificar = tk.Button(
            self.framePanel,
            text="Modificar",
            command=lambda: controller.modificar(
                self.ent_codigo.get(),
                self.ent_desc.get(),
                self.ent_ubic.get(),
                self.ent_cant.get(),
                self.ent_precio.get(),
            ),
        )
        self.btn_modificar.grid(column=1, row=3)

        self.btn_baja = tk.Button(
            self.framePanel,
            text="Eliminar",
            command=lambda: controller.baja(
                self.tvw_insumos.item(self.tvw_insumos.focus())
            ),
        )
        self.btn_baja.grid(column=2, row=3)

        self.btn_restablecer = tk.Button(
            self.framePanel, text="Restablecer", command=controller.restablecer
        )
        self.btn_restablecer.grid(column=3, row=3)
        self.tvw_insumos = ttk.Treeview(
            self.framePanel,
            columns=("codigoSAP", "descripcion", "ubicacion", "cantidad", "precio"),
        )
        self.tvw_insumos.heading("#0", text="CODIGO SAP")
        self.tvw_insumos.heading("#1", text="Descripcion")
        self.tvw_insumos.heading("#2", text="Deposito")
        self.tvw_insumos.heading("#3", text="Cantidad")
        self.tvw_insumos.heading("#4", text="Precio")

        self.tvw_insumos.grid(column=0, row=4, columnspan=5)
        self.controller.mostrar(
            self.tvw_insumos
        )  # trae todos los registros de la base por primera vez

        self.tvw_insumos.bind("<Button-1>", controller.cargar_form)
        self.lbl_error = tk.Label(self.framePanel, text="", font=20)

        self.lbl_error.grid(
            column=0,
            row=5,
        )
