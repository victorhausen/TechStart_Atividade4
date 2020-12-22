
class Markeplace:
    name:str
    description:str

    def __init__(self, name, description):
        self.name = name
        self.description = description

class Cateogorie:
    name:str
    description:str

    def __init__(self, name, description):
        self.name = name
        self.description = description

class Subcategorie(Categorie):
    name:str
    description:str
    parent_categorie_id:str 

    def __init__(self, name, description):
        self.parent_categorie_id = parent_categorie_id 
        super().__init__(name, description)