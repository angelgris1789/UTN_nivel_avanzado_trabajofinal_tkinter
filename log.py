import datetime

from observer import Observador


class Log(Observador):
    def __init__(self, obj):
        self.observador1 = obj
        self.observador1.agregar(self)

    def alta(self, codigo):

        log = open("log.txt", "a")
        log.write(
            str(datetime.datetime.now()) + " Alta del codigo: " + str(codigo) + "\r"
        )
        log.close()

    def modificacion(self, codigo):
        log = open("log.txt", "a")
        log.write(
            str(datetime.datetime.now())
            + " Modificacion del codigo: "
            + str(codigo)
            + "\r"
        )
        log.close()

    def baja(self, codigo):
        log = open("log.txt", "a")
        log.write(
            str(datetime.datetime.now())
            + " Eliminacion del codigo: "
            + str(codigo)
            + "\r"
        )
        log.close()


# if __name__ == "__main__":

# observador_b = ConcreteObserverB(tema1)

# objeto = Log()
# objeto.alta("80950")

# objeto.modificacion("80950")
# objeto.baja("80939")
