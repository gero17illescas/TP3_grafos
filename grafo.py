class Grafo(object):
    """
    Representacion de un grafo
    """
    def __init__(self):
        self.vertices = {}
        self.aristas = {}
 
    def agregar_vertice(self, vertice):
        """
        Agrega un vertice al grafo
        """
        self.vertices[vertice] = []
 
    def borrar_vertice(self, vertice):
        """
        Remueve el vertice del grafo, si no existe levanta KeyError
        """
        try:
            for key in self.vertices.keys():
                self.vertices[key].pop(vertice)
            self.vertices.pop(vertice)
        except KeyError:
            #Si el vertice no esta en el grafo
            pass
 
    def agregar_arista(self, vertice_1, vertice_2,nombre):
        """
        Agrega la arista en el vertice si este existe
        """
        try:
            self.vertices[vertice_1].append(nombre)
            self.vertices[vertice_2].append(nombre)
            self.aristas[nombre]= (vertice_1,vertice_2)
        except KeyError:
            #Si el vertice no esta en el grafo
            pass
 
    def borrar_arista(self, arista):
        #Remueve la arista si esta en el grafo
        try:
            a=self.aristas.pop(arista)
            if a:
                (vertice_1,vertice_2)=a
                self.vertices[vertice_1].pop(arista)
                self.vertices[vertice_2].pop(arista)
            
        except KeyError:
            #Si el vertice no esta en el grafo
            pass
 
    def get_aristas(self):
        #Devuelve la arista si esta en el grafo, caso contrario None
        try:
            return self.aristas
        except KeyError:
            pass
    def get_vertices(self):
        #Devuelve el vertice si esta en el grafo, caso contrario None
        try:
            return self.vertices
        except KeyError:
            pass

    def get_adyacentes(self,vertice):
            
        try:
            lista = []
            for arista in self.vertices[vertice]:
                (vertice_1,vertice_2)=self.aristas[arista]
                if vertice_1 is vertice:
                    lista.append(vertice_2)
                else:
                    lista.append(vertice_1)
            return lista
        except KeyError:
            #Si el vertice no esta en el grafo
            pass

    def son_adyacentes(self,vertice_1,vertice_2):
        try:
            for adyacente in get_adyacentes(vertice_1):
                if adyacente is vertice_2:
                    return True
            return False
        except KeyError:
            #Si el vertice no esta en el grafo
            return False

