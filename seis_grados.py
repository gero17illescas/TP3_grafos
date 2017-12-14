import csv
from grafo import Grafo
import random
PORCENTAJE = 0.6


def cercanos(grafo, origen):
    """
    Funcion bfs que devuelve una lista con tuplas de vertices y su dis
    tancia al origen, cuyo primero elemento es el vertice, y el segundo
    es la distancia que este se encuentra al vertice origen.
    
    POST:Devulve una lista.Si devuelve una lista vacia, o el origen no
    pertenece al grafo, o no exiten adyacentes que se conecten con dicho vertice.
    """
    visitados = {origen: True}
    cont = 0
    cola = [(cont, origen)]
    resultado = [(origen, cont)]
    while cola:
        (cont, v) = cola.pop(0)
        resultado.append((v, cont))
        for w in grafo.get_adyacentes(v):
            if w not in visitados:
                visitados[w] = True
                cola.append((cont+1, w))
                
    resultado.sort(key=lambda x: x[1])
    return resultado


def grafo_crear(nombre_archivo):
    """
    Crea un grafo de conexiones de actores a partir de un archivo de datos.

    PRE: Recibe el nombre de un archivo separado por comas que contenga de lineas:
        actor,pelicula,pelicula,pelicula
        que equivalen a: vertice,arista,arista,arista
    POST: Devuelve un grafo creado a partir de estos datos.
    """
    grafo = Grafo()
    aristas = grafo.get_aristas()
    with open(nombre_archivo, "r", encoding='utf-8', newline='\n') as csvfile:
        actores_csv = csv.reader(csvfile)
        for linea in actores_csv:
            actor = linea[0]
            grafo.agregar_vertice(actor)
            for pelicula in linea[1:]:
                actores = aristas.get(pelicula)
                if actores:
                    for aux in actores:
                        grafo.agregar_arista(actor, aux, pelicula)
                else:
                    aristas[pelicula] = [actor]

    return grafo


def camino(grafo, origen, llegada):
    """
    Devuelve el camino entre un actor de origen y uno de llegada.

    PRE: Recibe el grafo, un actor de origen y un actor de llegada.
    POST: Devuelve una lista ordenada de cadenas (peliculas) para llegar desde
    el origen hasta el final.
    """
    if not (pertenece_actor(grafo, origen) and pertenece_actor(grafo, llegada)):
        return False

    cola = [origen]
    visitados = {origen: True}
    padres = {origen: None}
    caminos = []
    resultado = []

    while cola:
        v = cola.pop(0)
        for w in grafo.get_adyacentes(v):
            if w not in visitados:
                visitados[w] = True
                padres[w] = v
                cola.append(w)
                if w == llegada:
                    break

    if llegada not in padres:
        return resultado

    h = llegada
    while h:
        caminos.insert(0, h)
        h = padres.pop(h)

    actor_1 = caminos.pop(0)
    while caminos:
        actor_2 = caminos.pop(0)
        pelicula = grafo.get_arista(actor_1, actor_2)
        resultado.append((actor_1, actor_2, pelicula))
        actor_1 = actor_2

    return resultado


def actores_a_distancia(grafo, origen, n):
    """
    Devuelve los actores a distancia n del recibido.

    PRE: Recibe el grafo, el actor de origen y el numero deseado.
    POST: Devuelve la lista de cadenas (actores) a n pasos del recibido.
    """    
    if not pertenece_actor(grafo, origen) or n < 0:
        return False
    aux = cercanos(grafo, origen)
    resultado = []
    if aux:
        aux.pop(0)
        i = 0
        while aux[i][1] <= n:
            if aux[i][1] == n:
                resultado.append(aux[i][0])
            i += 1
    
    return resultado


def actores_a_mayor_distancia(grafo, origen, n):
    """
    Calcula los actores que se encuentran a una distancia mayor que n del
    origen ingresado.
    PRE: Recibe un grafo, origen y un entero n.
    POST: devuelve una lista de cadenas. Si esta vcai es porque no hay
    actores mas lejos que N
    """
    if not pertenece_actor(grafo, origen) or n < 0:
        return False
    actores = cercanos(grafo, origen)
    if actores:
        for i, (actor, cercania) in enumerate(actores):
            if cercania <= n:
                actores.pop(i)
    return actores
            

def popularidad(grafo, actor):
    """
    Calcula la popularidad del actor recibido.

    PRE: Recibe el grafo y un actor de origen
    POST: Devuelve un entero que simboliza la popularidad: todos los adyacentes
        de los adyacentes del actor, multiplicado por su cantidad de peliculas
    """
    if not pertenece_actor(grafo, actor):
        return False
    lista = actores_a_distancia(grafo, actor, 2)
    cont = 0
    for pelicula in grafo.get_aristas():
        for tupla in grafo.aristas[pelicula]:
            if actor in tupla:
                cont += 1

    return len(lista)*cont


def random_walk(grafo, origen, pasos, orden):
    """
    Recibe un diccionario orden y de acuerdo a un camino aleatorio guarda
    en el dict la cantidad de veces que pasa por cada vertice.
    """
    if not pertenece_actor(grafo, origen) or pasos < 0:
        return False
    cola = [origen]
    while cola:
        v = cola.pop(0)
        if pasos <= 0:
            return
        orden[v] += 1
        pasos -= 1
        w = random.choice(grafo.get_adyacentes(v))
        cola.append(w)


def similares(grafo, origen, n):
    """
    Calcula los n actores mas similares al actor de origen y los devuelve en una
    lista ordenada de mayor similitud a menor.

    PRE: Recibe el grafo, el actor de origen, y el n deseado
    POST: Devuelve una lista de los n actores no adyacentes mas similares
    al pedido. La lista no debe contener al actor de origen.
    """
    if not pertenece_actor(grafo, origen) or n < 0:
            return False
    orden = {}
    for v in grafo.get_vertices():
        orden[v] = 0

    random_walk(grafo, origen, len(grafo.get_vertices())*PORCENTAJE, orden)
    aux = []
    resultado = []
    orden.pop(origen)
    for key, value in orden.items():
        aux.append((key, value))
    aux.sort(key=lambda x: x[1], reverse=True)
    for i in range(n):
        resultado.append(aux[i][0])
    return resultado


def estadisticas(grafo):
    """
    Devuelve una tupla en la que la primer componente es la cantida de
    aristas que tiene el grafo, y la segunda la cantidad e vertices.
    """
    return len(grafo.get_aristas()), len(grafo.get_vertices())


def promedio_kbn(grafo):
    promedios_kbn = 0
    cant_actores = len(grafo.get_vertices())
    for actor in grafo.get_vertices():
        aux = len(camino(grafo, 'Bacon Kevin', actor))
        if aux:
            promedios_kbn += aux
        else:
            cant_actores -= 1
    promedios_kbn /= cant_actores
    return promedios_kbn


def pertenece_actor(grafo, actor):
    """
    Devuleve un bool segun si el actor esta en el grafo o no
    """
    return grafo.vertices.get(actor)


def bacon_number_actores(grafo):
    resultado = []
    for actor in grafo.get_vertices():
        path = camino(grafo, 'Bacon Kevin', actor)
        kbn =-1
        if path:
            kbn = len(path)
        resultado.append(kbn)
    return resultado
