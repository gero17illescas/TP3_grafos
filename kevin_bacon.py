# coding=utf-8
from seis_grados import *
import sys
def camino_hasta_KB(dataset, actor):
    """
    Imprime el camino más corto con el cual se llega desde cualquier 
    actor hasta Kevin Bacon.
    """
    path = camino(dataset, 'Bacon Kevin', actor)
    for (actor_1, actor_2, pelicula) in path:
        print("{} actuó con {} en {}.".format(actor_1,actor_2,pelicula))

def bacon_number(dataset, actor):
    """
    Imprime el Kevin Bacon Number del actor recibido. 
    """
    path = camino(dataset, 'Bacon Kevin', actor)
    if not pertenece_actor(dataset, actor):
        print("El actor ingresado o es incorrecto o no se encuentra en la base de datos.")
        return
    kbn=-1
    if path:
        kbn=len(path)
    print("{} tiene un Kevin Bacon Number igual a {}.".format(actor,kbn))
    
def bacon_number_mayor_a_6(dataset):
    """
    Imprime la cantidad de actores (¿existirán?) a una distancia mayor
    a 6 pasos de Kevin Bacon. De no existir actores a más pasos que 6,
    se imprime un mensaje acorde. En este numero no influyen la cantidad
    de actores con un KBN infinito.
    """
    actores = actores_a_mayor_distancia(dataset, 'Bacon Kevin', 6)
    if not actores:
        print("No existen actores cuyo KBN sea mayor a 6")
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
    promedio = promedio_kbn(dataset)
    print("El Kevin Bacon Number promedio es %", promedio)

def similares_a_KB(dataset, n):
    print("Los % actores más similares KB son %", n, similares(dataset, 'Kevin Bacon', n))
    
def popularidad_contra_KB(dataset, actor):
    ac=popularidad(dataset,  actor)
    print("{} es un {} de lo popular que es Kevin Bacon".format(actor, ac))
    
def cantidad_actores(dataset):
    print("El dataset contiene {} actores".format(estadisticas(dataset)[1]))

def cantidad_peliculas(dataset):
    print("El dataset contiene {} peliculas".format(estadisticas(dataset)[0]))

    
def main():
    """Funcion principal"""
   
  
    file = sys.argv[1]
    dataset = grafo_crear(file)
    print("Cargado.\n")
    
    funciones = ['camino_hasta_KB', 'bacon_number', 'bacon_number_mayor_a_6', 
    'KBN_promedio', 'cantidad_actores', 'cantidad_peliculas','popularidad_contra_KB']
    entrada= input().split(" ")
    while entrada:
        while entrada == "" or entrada[0] not in funciones:
            entrada = input("No valido.Vuelva a ingresar.\n")
        comando = entrada[0]
        actor = " ".join(entrada[1:])
        if comando == 'camino_hasta_KB':
            camino_hasta_KB(dataset,actor)
        if comando == 'bacon_number':
            bacon_number(dataset,actor)
        if comando == 'bacon_number_mayor_a_6':
            bacon_number_mayor_a_6(dataset)
        if comando == 'similares_a_KB':
            if actor.isdigit():
                similares_a_KB(dataset, entrada[1])
        if comando == 'popularidad_contra_KB':
            popularidad_contra_KB(dataset, actor)
        if comando == 'bacon_number_infinito':
            bacon_number_infinito(dataset)
        if comando == 'KBN_promedio':
            KBN_promedio(dataset)
        if comando == 'cantidad_actores':
            cantidad_actores(dataset)
        if comando == 'cantidad_peliculas':
            cantidad_peliculas(dataset)
        entrada= input().split(" ")

main()