class Tema:  # gestion de observadores
    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self, codigo, accion):
        print("hola desde notificar")
        for observador in self.observadores:
            if accion == "alta":
                observador.alta(codigo)
            elif accion == "baja":
                observador.baja(codigo)
            elif accion == "modificacion":
                observador.modificacion(codigo)


class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


# print(observador_a.__dict__)
# print("---" * 25)
# print(Tema.__dict__)
