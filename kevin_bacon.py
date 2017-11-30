import seis_grados

def camino_hasta_KB(dataset,actor):
	camino = interfaz(camino,'Kevin Bacon',actor)
	for (actor_1,actor_2,pelicula) in camino:
		print(actor_1+" actuó con "+actor_2+" en "+pelicula[0]+".")

def bacon_number(dataset,actor):
	camino = camino(dataset,'Kevin Bacon',actor)
	if not pertence_actor(actor):
		print("El actor ingresado o es incorrecto o no se encuentra en la base de datos.")
		return
	kbn=-1
	if camino:
		kbn=len(camino)
	print(actor+" tiene un Kevin Bacon Number igual a "+kbn+".")
	
def bacon_number_mayor_a_6(dataset,actor):
	actores = 
	Bacon Number mayor a 6

	Imprime la cantidad de actores (¿existirán?) a una distancia mayor a 6 pasos de Kevin Bacon. De no existir actores a más pasos que 6, se imprime un mensaje acorde. En este numero no influyen la cantidad de actores con un KBN infinito.

	bacon_number_mayor_a_6
	>>> Los actores con un KBN mayor a 6 son:
	>>> Con KBN igual a 6: N actores
	>>> Con KBN igual a 7: N actores
	>>> ...

	Bacon Number infinito

	Imprime la cantidad de actores (¿existirán?) con un KBN infinito. De no haber, se debe imprimir un mensaje acorde.

	bacon_number_infinito
	>>> Los actores con un Bacon Number infinito son N

	Bacon Number promedio

	Imprime el Kevin Bacon Number promedio. En este numero no influyen la cantidad de actores con un KBN infinito, pero si lo hace el KBN de Kevin Bacon.

	KBN_promedio
	>>> El Kevin Bacon Number promedio es N

   
def similares_a_KB(dataset,n):
	similares = interfaz(similares,n)
	print("Los % actores más similares KB son %",n,similares)
	
def popularidad_contra_KB(dataset,actor):
	kb=interfaz(popularidad, 'Kevin Bacon')
	ac=interfaz(popularidad, actor)
   
	print("% es un % de lo popular que es Kevin Bacon" % (actor,(ac*100/kb)))
	
def cantidad_actores(dataset):
	print("El dataset contiene % actores" % interfaz(estadisticas)[1])

def cantidad_peliculas(dataset):
	print("El dataset contiene % películas" % interfaz(estadisticas)[0])

def main()