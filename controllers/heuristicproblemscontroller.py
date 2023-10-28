
class heuristicproblemsController():

    def __init__(self):
        print("controlador")


    def index(self):
        return self.repositorioAlmacenista.findAll()

    def create(self,infoAlmacenista):
        return "create"

    def show(self,id):
        return "show"

    def update(self, id, infoAlmacenista):
        return "update"

    def delete(self,id):
        return "delete"+id