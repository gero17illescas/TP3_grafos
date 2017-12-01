# coding=utf-8
from seis_grados import *
import sys
def camino_hasta_KB(dataset, actor):
    """
    Imprime el camino más corto con el cual se llega desde cualquier 
    actor hasta Kevin Bacon.
    """
    path = camino(dataset, 'Kevin Bacon', actor)
    for (actor_1, actor_2, pelicula) in path:
        print(actor_1+" actuó con "+actor_2+" en "+pelicula[0]+".")

def bacon_number(dataset, actor):
    """
    Imprime el Kevin Bacon Number del actor recibido. 
    """
    path = camino(dataset, 'Kevin Bacon', actor)
    if not pertenece_actor(dataset, actor):
        print("El actor ingresado o es incorrecto o no se encuentra en la base de datos.")
        return
    kbn=-1
    if path:
        kbn=len(path)
    print(actor+" tiene un Kevin Bacon Number igual a "+str(kbn)+".")
    
def bacon_number_mayor_a_6(dataset,  actor):
    """
    Imprime la cantidad de actores (¿existirán?) a una distancia mayor
    a 6 pasos de Kevin Bacon. De no existir actores a más pasos que 6,
    se imprime un mensaje acorde. En este numero no influyen la cantidad
    de actores con un KBN infinito.
    """
    actores = actores_a_mayor_distancia(dataset, actor, 6)
    if not actores:
        print("No existen actores cuyo KBN a % sea mayor a 6", actor)
        return
    else:
        aux = {}
        for actor, cercania in actores:
            if cercania in aux:
                    aux[cercania].append(actor)
            else:
                    aux[cercania]=0
        for cercania in aux:
            print("Con KBN igual a %: %", cercania, aux[cercania])

def bacon_number_infinito(dataset):
    """
    Imprime la cantidad de actores con un KBN infinito. De no haber,  se
    debe imprimir un mensaje acorde.
    """
    raise ValueError

def KBN_promedio(dataset):
    """
    Imprime el Kevin Bacon Number promedio de todos los actores en
    la base de datos.

    PRE: Recibe el dataset.
    """
    promedio = estadisticas(dataset)[2]
    print("El Kevin Bacon Number promedio es %", promedio)

def similares_a_KB(dataset, n):
    print("Los % actores más similares KB son %", n, similares(dataset, 'Kevin Bacon', n))
    
def popularidad_contra_KB(dataset, actor):
    kb=popularidad(dataset,  'Kevin Bacon')
    ac=popularidad(dataset,  actor)
   
    print("% es un % de lo popular que es Kevin Bacon" % (actor, (ac*100/kb)))
    
def cantidad_actores(dataset):
    print("El dataset contiene % actores" % estadisticas(dataset)[1])

def cantidad_peliculas(dataset):

    
def main():
    """Funcion principal"""
   
  
    file = sys.argv[1]
    dataset = grafo_crear(file)
    print("Cargado.\n")
    for acotres in dataset.get_vertices():
        print(acotres)
    for pelicula in dataset.get_aristas():
        print(pelicula)
    entrada= input().split(" ")
    funciones = ['camino_hasta_KB', 'bacon_number', 'bacon_number_mayor_a_6', 
    'similares_a_KB', 'popularidad_contra_KB', 'bacon_number_infinito', 
    'KBN_promedio', 'cantidad_actores', 'cantidad_peliculas']
    while entrada == "" or entrada[0] not in funciones:
        entrada = input("No valido.Vuelva a ingresar.\n")
    
    if entrada[0] == 'camino_hasta_KB':
        camino_hasta_KB(dataset,'Reeves Keanu')
    if entrada[0] == 'bacon_number':
        bacon_number(dataset, entrada[1])
    if entrada[0] == 'bacon_number_mayor_a_6':
        bacon_number_mayor_a_6(dataset, entrada[1])
    if entrada[0] == 'similares_a_KB':
        if entrada[1].isdigit():
            similares_a_KB(dataset, entrada[1])
    if entrada[0] == 'popularidad_contra_KB':
        popularidad_contra_KB(dataset, entrada[1])
    if entrada[0] == 'bacon_number_infinito':
        bacon_number_infinito(dataset)
    if entrada[0] == 'KBN_promedio':
        KBN_promedio(dataset)
    if entrada[0] == 'cantidad_actores':
        cantidad_actores(dataset)
    if entrada[0] == 'cantidad_peliculas':
        cantidad_peliculas(dataset)

main()