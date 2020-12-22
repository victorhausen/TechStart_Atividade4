import random
import pandas as pd
import sqlite3

class Controller:
    __instance = None
    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = {
            "marketplaces": [],
            "categories": [],
        }
        return cls.__instance

    def read_marketplaces(self):
        rows = []
        try:
            conn = sqlite3.connect('database/database.sqlite')
            cur = conn.cursor()
            cur.execute("SELECT * FROM marketplace;")
            rows = cur.fetchall()
        except:
            return('deu erro')
        finally:
            conn.close()

        df = pd.DataFrame(rows)
        return "bananinha"

    def read_categories(self):
        rows = []
        try:
            conn = sqlite3.connect('database/database.sqlite')
            cur = conn.cursor()
            cur.execute("SELECT * FROM categories;")
            rows = cur.fetchall()
        except:
            pass
        finally:
            conn.close()
        return rows

    #################3333
    def create_marketplace(self, marketplace):
        try:
            for categoria_id in produto.categorias:
                assert(categoria_id in [categoria.id for categoria in self.__instance['categorias']])
            self.__instance['produtos'].append(produto)
        except:
            print("Essa categoria mãe não existe.\nRegistro Cancelado")

    def create_categoria(self, categoria):
        try:
            assert(categoria.mae_id in [categoria.id for categoria in self.__instance['categorias']])
            self.__instance['categorias'].append(categoria)
        except:
            print("Essa categoria mãe não existe.\nRegistro Cancelado")

    def generate_id(self):
        id = str(random.sample(range(1000), 1)[0])
        for i in 3-len(id):
            id = "0" + id

        if id in self.get_used_ids():
            id = self.generate_id()

        return id