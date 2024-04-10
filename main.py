# -*- coding: utf-8 -*-
"""
Programmation multithreading (1h30)
	- accès au cours, à l'ordinateur et à internet
	- interdiction d'utiliser queue.Queue!
	- usage obligatoire de threads!
	- coefficient 2


	Problèmes à résoudre:
		C'est un jeu avec trois acteurs indépendant un arbitre "A" et
		2 joueurs ("J1" et "J2").
		- Le rôle de "A" :
			* il initie le jeu en lançant un nombre entre 10000 et 100000 à un joueur (au hasard)
			* il affiche le nom du gagnant
			* il met fin au jeu (stoppe les threads) lorsqu'un des joueurs a gagné
		- Le rôle de chaque joueur à réception du nombre N.
			* si c'est 1 le joueur a gagné, il l'annonce à l'arbitre
			* si N est pair, envoie N//2 à l'autre joueur
			* si N est impair, envoie (3N+1)//2 à l'autre joueur

		Chaque action devra être logguée via le module logging tel que fait dans diner_des_philosophes.py.


Vous me fournirez les documents suivants dans un zip nommé {NOM}_{Prenom}_CC2.zip:
	- un fichier python contenant votre code source aéré et documenté (commentaires)
	  il sera tenu compte des choix de nommages effectués.
	- le fichier de log que vous avez obtenu par exécution du programme
	- par mail à boulanger.philippe@yahoo.fr pour 19h dernier délai. tout dépassement sera pénalisant. 
	- le non-respect de la consigne entraînera une perte de points!

Barème:
	Convention nom (2)
	Code aéré (1)
	Structure du code (fonction/classe) (1)
	Respect consigne (1)
	Run sans erreur (2)
	Génère les bonnes sorties (2)
	Choix des outils (6)
	Efficacité (5)
    
Created on Mon Apr 2024

@author: Remy Hamed
"""

import random
from threading import Lock, Thread


class Queue:
    def __init__(self):
        self.__queue = []
        self.__lock = Lock()

    def push( self, data ):
        with self.__lock:
            self.__queue.append( data )

    def pop( self ):
        with self.__lock:
            if len(self.__queue) == 0:
                return None
            return self.__queue.pop( 0 )

    def __len__(self):
        with self.__lock:
            return len(self.__queue)

class Player(Thread):
	def __init__(self, name, queue):
		Thread.__init__(self)
		self.name = name
		self.queue = queue
    
	def run(self):
		while True:
			n = self.queue.pop()
			if n is None:
				break
			if n == 1:
				print(f"{self.name} wins")
				break
			if n % 2 == 0:
				self.queue.push(n // 2)
			else:
				self.queue.push((3 * n + 1) // 2)


class referee(Thread):
	def __init__(self, queue):
		Thread.__init__(self)
		self.queue = queue
		self._continue = True
	
	def init_game(self):
		n = random.randint(10000, 100000)
		print(f"Starting number: {n}")
		number_bundle = "j1" + ' ' + str(n)
		self.queue.push(number_bundle)
	
	def run(self):
		while self._continue:
			number_bundle = self.queue.pop()
			if number_bundle is None:
				break
			parts = number_bundle.split()
			player = parts[0]
			number = int(parts[1])
			if number == 1:
				print(f"{player} wins")
				self._continue = False
			else:
				Queue.push(number_bundle)


class player(Thread):
	def __init__(self, name, queue):
		Thread.__init__(self)
		self.name = name
		self.queue = queue
		self._continue = True

	def play(self):
			number_bundle = self.queue.pop()
			if number_bundle is None:
				return
			parts = number_bundle.split()
			player = parts[0]
			number = int(parts[1])
			if player == self.name:
				self.queue.push(number_bundle)
				return
			if number == 1:
				self.queue.push(number_bundle)
			if number % 2 == 0:
				self.queue.push(f"j1 {number // 2}")
			if number % 2 == 1:
				self.queue.push(f"j1 {3 * number + 1 // 2}")

	
	def run(self):
		while self._continue:
			self.play()

q = Queue()

r= referee(q)
r.init_game()

players = [ Player("j1", q),Player("j2", q)]

r.start()
[ p.start() for p in players]
[ p.join() for p in players]
r.join()





# Path: exam_false/main.p