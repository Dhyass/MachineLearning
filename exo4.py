# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:06:20 2023

@author: NONZOOU
"""

class Livre:
    def __init__(self, titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn

    def __str__(self):
        return f"Titre : {self.titre}, Auteur : {self.auteur}, ISBN : {self.isbn}"

class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.livres_disponibles = []

    def ajouter_livre(self, livre):
        self.livres_disponibles.append(livre)

    def afficher_livres(self):
        if self.livres_disponibles:
            print(f"Liste des livres disponibles dans la bibliothèque {self.nom}:")
            for livre in self.livres_disponibles:
                print(livre)
        else:
            print("La bibliothèque est vide.")

    def rechercher_livre_par_isbn(self, isbn):
        for livre in self.livres_disponibles:
            if livre.isbn == isbn:
                return livre
        return None

# Créez des livres et une bibliothèque
livre1 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", "978-2-234-12345-6")
livre2 = Livre("Harry Potter à l'école des sorciers", "J.K. Rowling", "978-2-345-67890-1")
livre3 = Livre("1984", "George Orwell", "978-0-452-28423-4")

bibliotheque = Bibliotheque("Bibliothèque Centrale")

# Ajoutez des livres à la bibliothèque
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)
bibliotheque.ajouter_livre(livre3)

# Affichez la liste des livres disponibles
bibliotheque.afficher_livres()

# Recherchez un livre par ISBN
isbn_recherche = "978-2-345-67890-1"
livre_recherche = bibliotheque.rechercher_livre_par_isbn(isbn_recherche)
if livre_recherche:
    print(f"\nLivre trouvé : {livre_recherche}")
else:
    print("\nLivre non trouvé.")

# Testez avec d'autres opérations si nécessaire
