import csv
from grafo import Grafo
import random
PORCENTAJE = 0.09

def cercanos (grafo,origen):
    """
    Funcion bfs que devuelve una lista con tuplas de vertices y su dis
    tancia al origen, cuyo primero elemento es el vertice, y el segundo
    es la distancia que este se encuentra al vertice origen.
    
    POST:Devulve una lista.Si devuelve una lista vacia, o el origen no
    pertenece al grafo, o no exiten adyacentes que se conecten con dicho vertice.
    """
    visitados  =  {}
    cola  =  [origen]
    visitados[origen] = True
    resultado = []
    cont = 0
    while cola:
        v  =  cola.pop(0)
        resultado.append((v,cont))
        cont +=  1
        for w in grafo.get_adyacentes(v):
            if w not in visitados:
                visitados[w] = True
                cola.append(w)
    resultado.sort(key = lambda x : x[1])
    return resultado

def grafo_crear(nombre_archivo):
    """
    Crea un grafo de conexiones de actores a partir de un archivo de datos.

    PRE: Recibe el nombre de un archivo separado por comas que contenga de lineas:
        actor,pelicula,pelicula,pelicula
        que equivalen a: vertice,arista,arista,arista
    POST: Devuelve un grafo creado a partir de estos datos.
    """
    grafo  =  Grafo()
    with open(nombre_archivo,"r",newline='\n') as csvfile:
        actores_csv  =  csv.reader(csvfile)
        aristas = {}
        for linea in actores_csv:
            actor = linea[0]
            grafo.agregar_vertice(actor)
            for pelicula in linea[1:]:
                if pelicula in aristas:
                    aristas['{}'.format(pelicula)].append('{}'.format(actor))
                else:
                    aristas['{}'.format(pelicula)] = ['{}'.format(actor)]
    for pelicula in aristas.keys():
        actores  =  aristas[pelicula]
        while actores:
            aux  =  actores.pop(0)
            for actor in actores:
                grafo.agregar_arista(aux,actor,pelicula)
    return grafo

def camino(grafo, origen, llegada):
    """
    Devuelve el camino entre un actor de origen y uno de llegada.

    PRE: Recibe el grafo, un actor de origen y un actor de llegada.
    POST: Devuelve una lista ordenada de cadenas (peliculas) para llegar desde
    el origen hasta el final.
    """
    cola = [origen]
    visitados = {origen:True}
    padres = {origen:None}
    camino = []
    resultado = []

    while cola:
        v  =  cola.pop(0)
        for w in grafo.get_adyacentes(v):
            if w not in visitados:
                visitados[w] = True
                padres[w] = v
                cola.append(w)
                if w  ==  llegada:
                    break
    if llegada not in padres:
        return resultado
    h = llegada
    while h:
        camino.insert(0,h)
        h = padres.pop(h)
    actor_1  =  camino.pop(0)
   
    while camino:
        actor_2 = camino.pop(0)
        pelicula = grafo.get_arista(actor_1,actor_2)
        resultado.append((actor_1,actor_2,pelicula))
        actor_1  =  actor_2
    return resultado


def actores_a_distancia(grafo, origen, n):
    """
    Devuelve los actores a distancia n del recibido.

    PRE: Recibe el grafo, el actor de origen y el numero deseado.
    POST: Devuelve la lista de cadenas (actores) a n pasos del recibido.
    """    
    
    aux  =  cercanos(grafo,origen)
    resultado = []
    if aux:
        for i in range(n):
            resultado.append(aux[i][0])
    return resultado

def actores_a_mayor_distancia(grafo,origen,n):
    """
    Calcula los actores que se encuentran a una distancia mayor que n del
    origen ingresado.
    PRE: Recibe un grafo, origen y un entero n.
    POST: devuelve una lista de cadenas. Si esta vcai es porque no hay
    actores mas lejos que N
    """
    actores = cercanos(grafo,origen)
    if actores:
        for i,(actor,cercania) in enumerate(actores):
            if cercania < n:
                actores.pop(i)
    return actores
            

def popularidad(grafo, actor):
    """
    Calcula la popularidad del actor recibido.

    PRE: Recibe el grafo y un actor de origen
    POST: Devuelve un entero que simboliza la popularidad: todos los adyacentes
        de los adyacentes del actor, multiplicado por su cantidad de peliculas
    """

    lista  =  actores_a_distancia(grafo,actor,2)
    return len(lista)*len(grafo.get_vertices())

def random_walk(grafo,v,pasos,orden):
    if pasos  <=  0:
        return
    orden[v] +=  1
    pasos -=  1
    w = random.choice(grafo.get_adyacentes(v))
    random_walk(grafo,w ,pasos,orden)
        
def similares(grafo, origen, n):
    """
    Calcula los n actores mas similares al actor de origen y los devuelve en una
    lista ordenada de mayor similitud a menor.

    PRE: Recibe el grafo, el actor de origen, y el n deseado
    POST: Devuelve una lista de los n actores no adyacentes mas similares
    al pedido. La lista no debe contener al actor de origen.
    """
    orden  =  {}
    for v in grafo.get_vertices():
        orden[v] = 0

    random_walk(grafo,origen,len(grafo.get_vertices())*PORCENTAJE,orden)
    aux  =  []
    resultado = []
    orden.pop(origen)
    for key,value in orden.items():
        aux.append((key,value))
    aux.sort(key = lambda x: -x[1],reverse = True)
    for i in range(n):
        resultado.append(aux[i][0])
    return resultado
    
def estadisticas(grafo):
    return (len(grafo.get_aristas()),len(grafo.get_vertices()))

def promedio_kbn(grafo):
    promedio_kbn = 0
    for actor in grafo.get_vertices():
        promedio_kbn +=  len(camino(grafo,'Bacon Kevin',actor))
    promedio_kbn /= len(grafo.get_vertices())
    return promedio_kbn

def pertenece_actor(grafo, actor):
    return actor in grafo.get_vertices()

def bacon_number_actores(grafo):
    resultado = []
    for actor in grafo.get_vertices():
        path = camino(grafo, 'Bacon Kevin', actor)
        kbn=-1
        if path:
            kbn=len(path)
        resultado.append(kbn)
    return resultado