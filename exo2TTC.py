# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:42:15 2023

@author: NONZOOU
"""
"""
    Une boucle while : entrez un prix HT (entrez o pour terminer) et affichez sa valeur TTC.
    
    Indication : 
   Le TTC, ou "Toutes Taxes Comprises", est le montant total à payer pour un produit ou un service, 
   y compris toutes les taxes applicables. Pour calculer le TTC à partir du TH, 
   ou "Taux de Taxe sur la Valeur Ajoutée" (TVA), vous pouvez utiliser la formule suivante :

TTC = HT + (HT * (TH / 100))

où :
- TTC est le montant total toutes taxes comprises.
- HT est le montant hors taxe, c'est-à-dire le prix du produit ou du service avant l'ajout de la TVA.
- TH est le taux de la TVA en pourcentage.

Voici un exemple :

Supposons que vous avez un produit dont le prix HT est de 100 euros et que le taux de TVA est de 20 %.

TTC = 100 + (100 * (20 / 100))
TTC = 100 + (100 * 0,20)
TTC = 100 + 20
TTC = 120 euros

Le montant total toutes taxes comprises pour ce produit est de 120 euros.

Cette formule vous permet de calculer le TTC à partir du prix HT et du taux de TVA.
"""
import classcercle 

def calculTTH(prix, taux):
    if prix < 0 or taux < 0:
        print("Erreur : le prix et la TVA doivent être positifs")
        return None
    else:
        prixttc = prix + (prix * taux / 100)
        return prixttc

print("Ce programme calcule le montant total pour un produit ou un service")

sortir = "C"
while sortir not in ("O", "o"):
    prix = float(input("Entrez le prix de l'article ou du service : "))
    tva = float(input("Entrez la TVA : "))
    TTC = round(calculTTH(prix, tva), 2)

    if TTC is not None:
        print(f"Le total à payer est : {TTC} Euros")

    sortir = input("O pour quitter, C pour continuer : ")
    
mon_cercle1 = classcercle.cercle_python("Cercle1")
mon_cercle1.parametrescercle(rayon=2.0, couleur='blue', epaisseur=2.0)

mon_cercle2 = classcercle.cercle_python("Cercle2")
mon_cercle2.parametrescercle(rayon=4.0, couleur='red', epaisseur=2.0)

mon_cercle1.dessiner_cercle()
mon_cercle2.dessiner_cercle()



    