class Arista(object):
	def __init__(self,nombre,vertice_1,vertice_2,peso=None):
		self.nombre = nombre
		self.vertice_1 = vertice_1
		self.vertice_2 = vertice_2        
		self.peso = peso

class Grafo(object):
	def __init__(self):
		self.vertice = {}
		self.aristas = {}
 
	def agregar_vertice(self, vertice):
		#Agrega un vertice al grafo
		self.vertice[vertice] = []
 
	def borrar_vertice(self, vertice):
		#Remueve el vertice del grafo, si no existe levanta KeyErro
		try:
			self.vertice.pop(vertice)
		except KeyError:
			#Si el vertice no esta en el grafo
			pass
 
	def agregar_arista(self, vertice_1, vertice_2,nombre,peso=None):
		#Agrega la arista en el vertice si este existe
		try:
			a = Arista(nombre,vertice_1,vertice_2,peso)
			self.vertice[vertice_1]= nombre
			self.vertice[vertice_2]= nombre
			self.aristas[nombre]= a
		except KeyError:
			#Si el vertice no esta en el grafo
			pass
 
	def borrar_arista(self, arista):
		#Remueve la arista si esta en el grafo
		try:
			a = self.aristas[arista]
			self.vertice[a.vertice_1].pop(a.nombre)
			self.vertice[a.vertice_2].pop(a.nombre)
			self.aristas.pop(arista)
		except KeyError:
			#Si el vertice no esta en el grafo
			pass
 
	def get_arista(self, arista):
		#Devuelve la arista si esta en el grafo, caso contrario None
		try:
			return self.aristas[arista]
		except KeyError:
			pass
	def get_vertice(self, vertice):
		#Devuelve el vertice si esta en el grafo, caso contrario None
		try:
			return self.vertice[vertice]
		except KeyError:
			pass

	def get_adyacentes(self,vertice):
		#Devulve una dict de nombres de aristas, si el vertice esta en 
		#el grafo. None en caso contrario
		try:
			return self.vertice[vertice]
		except KeyError:
			#Si el vertice no esta en el grafo
			pass

	def son_adyacentes(self,vertice_1,vertice_2):
		try:
			for a in self.vertice[vertice_1]
				if a.vertice_2==vertice_2
					return True
		except KeyError:
			#Si el vertice no esta en el grafo
			return False


def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes: 
	min_node = None
	for node in nodes:
	  if node in visited:
		if min_node is None:
		  min_node = node
		elif visited[node] < visited[min_node]:
		  min_node = node

	if min_node is None:
	  break

	nodes.remove(min_node)
	current_weight = visited[min_node]

	for edge in graph.edges[min_node]:
	  weight = current_weight + graph.distance[(min_node, edge)]
	  if edge not in visited or weight < visited[edge]:
		visited[edge] = weight
		path[edge] = min_node

return visited, path