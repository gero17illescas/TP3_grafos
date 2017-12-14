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
        self.vertices[vertice] = {}
 
    def borrar_vertice(self, vertice):
        """
        Remueve el vertice del grafo, si no existe levanta KeyError
        """
        if vertice in self.vertices:
            for key in self.vertices.keys():
                self.vertices[key].pop(vertice,None)
            self.vertices.pop(vertice)
 
    def agregar_arista(self, vertice_1, vertice_2, nombre):
        """
        Agrega la arista en el vertice si este existe
        """
        if not self.aristas.get(nombre): #Nueva pelicula
            self.aristas[nombre] = []
        else:
            if vertice_1 not in self.aristas[nombre]:
                self.aristas[nombre].append(vertice_1)
            if vertice_2 and vertice_2 not in self.aristas[nombre]:
                self.aristas[nombre].append(vertice_2)
        if vertice_1 and vertice_2:
            self.vertices[vertice_2][vertice_1] = True
            self.vertices[vertice_1][vertice_2] = True

    def borrar_arista(self, arista):
        #Remueve la arista si esta en el grafo
        if arista in self.aristas:
            a=self.aristas.pop(arista)
            if a:
                (vertice_1,vertice_2)=a
                self.vertices[vertice_1].pop(arista)
                self.vertices[vertice_2].pop(arista)
 
    def get_aristas(self):
        #Devuelve la arista si esta en el grafo, caso contrario None
        return self.aristas

    def get_vertices(self):
        #Devuelve el vertice si esta en el grafo, caso contrario None
        return self.vertices

    def get_adyacentes(self, vertice):
        return list(self.vertices[vertice].keys())

    def son_adyacentes(self, vertice_1, vertice_2):
        try:
            for adyacente in self.get_adyacentes(vertice_1):
                if adyacente is vertice_2:
                    return True
            return False
        except KeyError:
            #Si el vertice no esta en el grafo
            return False
    
    def get_arista(self,v1,v2):
        return self.vertices[v1][v2]