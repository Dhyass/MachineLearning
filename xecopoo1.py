# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 13:08:32 2023

@author: NONZOOU
"""
"""
    Exercice : Gestion d'une bibliothèque

Imaginez que vous devez créer un système de gestion de bibliothèque en utilisant la POO. Vous devez créer deux classes : une classe "Livre" pour représenter les livres et une classe "Bibliotheque" pour gérer les livres dans la bibliothèque. Voici quelques étapes à suivre :

Créez une classe "Livre" avec les attributs suivants :

Titre
Auteur
ISBN (numéro d'identification unique)
Ajoutez un constructeur à la classe "Livre" pour initialiser ces attributs.

Créez une classe "Bibliotheque" avec les attributs suivants :

Nom de la bibliothèque
Liste des livres disponibles (une liste d'objets "Livre")
Ajoutez un constructeur à la classe "Bibliotheque" pour initialiser le nom de la bibliothèque et une liste vide de livres.

Ajoutez une méthode à la classe "Bibliotheque" pour ajouter un livre à la bibliothèque.

Ajoutez une méthode à la classe "Bibliotheque" pour afficher la liste des livres disponibles dans la bibliothèque.

Ajoutez une méthode à la classe "Bibliotheque" pour rechercher un livre par son ISBN et afficher ses détails.

Créez quelques objets "Livre" et ajoutez-les à votre bibliothèque. Ensuite, testez les méthodes de la classe "Bibliotheque" pour ajouter, afficher et rechercher des livres.
"""

class Livre:
    def __init__(self, Titre, Auteur,ISBN):
        self.Titre= Titre
        self.Auteur= Auteur
        self.ISBN= ISBN
        
    def __str__(self):
        return f"Titre : {self.Titre} : Auteur :{self.Auteur} : ISBN : {self.ISBN}"
        
class Bibliotheque :
    def __init__(self, Nom):
        self.Nom = Nom
        self.LesLivres= []
        ### méthode pour ajouter un livre 
    def AjouterLivres(self, livre) :
        self.LesLivres.append(livre)
        
        ### methode pour afficher un livre
    def afficher_levres(self):
        if self.LesLivres :
            print(f"Les livres sont disponibles dans la bibliothèque : {self.Nom}")
            for livre in self.LesLivres:
                print(livre)
        else:
            print("La Bibliothèque est vide")
    ### methode pour chercher un livre avec isbn
    def rechercher_livre_par_ISBN(self, ISBN):
        for livre in self.LesLivres:
            if livre.ISBN == ISBN:
                return livre
        return None
        
# Créez des livres et une bibliothèque
Livre1 =Livre("Les Seigneur des Anneaux", "J.R.R. Tolkien", "978-2-234-12345-6")
Livre2=Livre("Harry Potter à l'école des Sorciers", "J.K. Rowling","978-2-345-67890-1")
Livre3 = Livre("1984", "George Orwell", "978-0-452-28423-4")
Livre4 = Livre("End Of Days", "Sylvia Browne", "978-0-452-28423-7")

bibliotheque = Bibliotheque("La Bibliothèque Nationale")

# Ajoutez des livres à la bibliothèque
bibliotheque.AjouterLivres(Livre1)
bibliotheque.AjouterLivres(Livre2)
bibliotheque.AjouterLivres(Livre3)
bibliotheque.AjouterLivres(Livre4)

bibliotheque.afficher_levres()

# Recherchez un livre par ISBN
isbn_recherche = "978-2-345-67890-8"
livre_recherche = bibliotheque.rechercher_livre_par_ISBN(isbn_recherche)
if livre_recherche:
    print(f"\nLivre trouvé : {livre_recherche}")
else:
    print("\nLivre non trouvé.")

### Supprimer un livre
### modifier les informations d'un livre (nom auteur, titre, isbn)
### rechercher et afficher tous les livres d'un auteur dans la bibliothèque
### un choix d'options 