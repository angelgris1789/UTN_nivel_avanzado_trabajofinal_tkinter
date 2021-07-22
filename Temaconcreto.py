import observer
import log


class TemaConcreto(observer.Tema):  # mi clase controller
    def __init__(self):
        pass

    def set_estado(self, value):
        self.estado = value
        self.notificar(value)

    def get_estado(self):
        return self.estado


tema1 = TemaConcreto()
observador_a = log.Log(tema1)
tema1.set_estado(0)
