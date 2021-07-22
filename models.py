import mysql.connector

db = mysql.connector.connect(
    host="190.228.29.62",
    user="cursopython",
    passwd="hqAHvbHk5LN3",
    database="inventariopython",
)


class Model:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="190.228.29.62",
            user="cursopython",
            passwd="hqAHvbHk5LN3",
            database="inventariopython",
        )

    def traer_datos(self, tree):
        self.cur = self.db.cursor()
        sql = "SELECT * FROM inventario_test"
        # sql = "SELECT * FROM inventariosap"
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def agregar(self, *args, **kwargs):

        self.cur = self.db.cursor()
        self.sql = "INSERT INTO inventario_test () VALUES (%s,%s,%s,%s,%s)"
        self.datos = (args[1], args[2], args[3], args[4], args[5])
        self.cur.execute(self.sql, self.datos)
        self.db.commit()

    def borrar(self, *args, **kwargs):
        self.cur = self.db.cursor()
        self.sql = "DELETE FROM inventario_test WHERE codigosap = %s" % args[0]

        self.cur.execute(self.sql)

        self.db.commit()

    def modificar(self, *args, **kwargs):
        self.lista = args[1]
        # print(self.lista)
        self.cur = self.db.cursor()
        self.sql = "UPDATE inventario_test SET descripcion = %s, ubicacion = %s, cantidad = %s, costounitario=%s WHERE codigosap = %s"
        self.datos = (
            self.lista[1],
            self.lista[2],
            self.lista[3],
            self.lista[4],
            self.lista[0],
        )
        self.cur.execute(self.sql, self.datos)
        self.db.commit()
