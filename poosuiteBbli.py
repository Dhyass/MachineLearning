# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:51:56 2023

@author: NONZOOU
"""
### xecopoo1 suite avec : version 1.1
"""
1-Supprimer un livre : Ajoutez une méthode à la classe Bibliotheque pour 
supprimer un livre de la bibliothèque en utilisant son ISBN.

2-Modifier les informations d'un livre : Ajoutez une méthode pour permettre 
la modification des informations d'un livre existant, telles que le titre, l'auteur ou l'ISBN.

3-Rechercher et afficher tous les livres d'un auteur : 
    Ajoutez une méthode pour rechercher et afficher tous les livres d'un auteur donné dans la bibliothèque.

4-Menu interactif : Créez un menu interactif qui permet à 
l'utilisateur de choisir parmi différentes options, comme ajouter un livre, afficher la liste des livres, rechercher un livre, supprimer un livre, etc.

5-Sauvegarde et chargement des données : Ajoutez des méthodes pour sauvegarder 
les données de la bibliothèque dans un fichier et pour charger les données à partir du fichier. 
Cela permettrait de conserver les informations de la bibliothèque entre différentes exécutions du programme.
"""
import random

# Classe Livre
class Livre:
    def __init__(self, Titre, Auteur, ISBN):
        self.Titre = Titre
        self.Auteur = Auteur
        self.ISBN = ISBN

    def __str__(self):
        return f"Titre : {self.Titre}, Auteur : {self.Auteur}, ISBN : {self.ISBN}"

# Classe Bibliotheque
class Bibliotheque:
    def __init__(self, Nom):
        self.Nom = Nom
        self.LesLivres = []

    def AjouterLivres(self, livre):
        self.LesLivres.append(livre)

    def afficher_levres(self):
        if self.LesLivres:
            print(f"Les livres sont disponibles dans la bibliothèque : {self.Nom}")
            for livre in self.LesLivres:
                print(livre)
        else:
            print("La Bibliothèque est vide")

    def rechercher_livre_par_ISBN(self, ISBN):
        for livre in self.LesLivres:
            if livre.ISBN == ISBN:
                return str(livre)  # Correction : retourne les informations du livre trouvé
        return f"Le livre avec l'ISBN {ISBN} n'a pas été trouvé dans la bibliothèque"

    def supprimer_livre(self, ISBN):
        for livre in self.LesLivres:
            if livre.ISBN == ISBN:
                self.LesLivres.remove(livre)
                print(f"Le livre avec l'ISBN {ISBN} a été supprimé de la bibliothèque")
                return
        print(f"Aucun livre avec l'ISBN {ISBN} n'a été trouvé dans la bibliothèque")

    def modifier_livre(self, ISBN, Nouveau_Titre, Nouvel_Auteur, Nouvel_ISBN):
        for livre in self.LesLivres:
            if livre.ISBN == ISBN:
                livre.Titre = Nouveau_Titre
                livre.Auteur = Nouvel_Auteur
                livre.ISBN = Nouvel_ISBN
                print(f"Les informations du livre avec l'ISBN {ISBN} ont été mises à jour.")
                return  # Correction : ajouter un return pour sortir de la boucle
        print(f"Aucun livre avec l'ISBN {ISBN} n'a été trouvé dans la bibliothèque")

    def rechercher_livres_par_auteur(self, auteur):
        livres_auteur = []
        for livre in self.LesLivres:
            if livre.Auteur == auteur:
                livres_auteur.append(livre)

        if livres_auteur:
            print(f"Les livres de l'auteur {auteur} dans la bibliothèque {self.Nom} sont :")
            for livre in livres_auteur:
                print(livre)
        else:
            print(f"Aucun livre de l'auteur {auteur} n'a été trouvé dans la bibliothèque.")

# Fonction pour afficher le menu
def afficher_menu():
    print("\nMenu de la Bibliothèque")
    print("1. Ajouter un livre")
    print("2. Afficher la liste des livres")
    print("3. Rechercher un livre par ISBN")
    print("4. Supprimer un livre")
    print("5. Modifier les informations d'un livre")
    print("6. Rechercher les livres d'un auteur")
    print("7. Quitter")

# Créez une bibliothèque
bibliotheque = Bibliotheque("La Bibliothèque Nationale")

# Menu principal
while True:
    afficher_menu()
    choix = input("Choisissez une option (1/2/3/4/5/6/7) : ")

    if choix == "1":
        # Option : Ajouter un livre
        Titre = input("Entrer le titre de l'Oeuvre : ")
        Auteur = input("Entrer le nom de l'auteur : ")
        ISBN = input("Entrer l'ISBN du Livre : ")
        Livre_obj = Livre(Titre, Auteur, ISBN)
        bibliotheque.AjouterLivres(Livre_obj)
        print(f"Le livre {Titre} a été ajouté à la bibliothèque.")

    elif choix == "2":
        # Option : Afficher la liste des livres
        bibliotheque.afficher_levres()

    elif choix == "3":
        # Option : Rechercher un livre par ISBN
        livre_chercher = input("Entrer l'ISBN du livre que vous cherchez : ")
        result = bibliotheque.rechercher_livre_par_ISBN(livre_chercher)
        print(result)

    elif choix == "4":
        # Option : Supprimer un livre
        livre_chercher = input("Entrer l'ISBN du livre à supprimer : ")
        bibliotheque.supprimer_livre(livre_chercher)

    elif choix == "5":
        # Option : Modifier les informations d'un livre
        ISBN = input("Entrer l'ISBN du livre que vous voulez modifier : ")
        Nouveau_Titre = input("Entrer le nouveau titre de l'oeuvre : ")
        Nouvel_Auteur = input("Entrer le nouveau nom de l'auteur : ")
        Nouvel_ISBN = input("Entrer le nouveau ISBN du livre : ")
        bibliotheque.modifier_livre(ISBN, Nouveau_Titre, Nouvel_Auteur, Nouvel_ISBN)

    elif choix == "6":
        # Option : Rechercher les livres d'un auteur
        auteur = input("Entrez le nom de l'auteur : ")
        bibliotheque.rechercher_livres_par_auteur(auteur)

    elif choix == "7":
        # Option : Quitter le programme
        print("Merci d'avoir utilisé la bibliothèque. Au revoir !")
        break

    else:
        print("Option invalide. Veuillez choisir une option valide (1/2/3/4/5/6/7).")


    
        