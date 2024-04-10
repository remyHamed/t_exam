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