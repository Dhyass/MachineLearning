
############# dictionnaire

traduction_1= {
    "Haa":"Dog",
    "Piaou":"Cat",
    "Zouma":"Bird",
    "Kelimiye":"Chicken",
    "Soom":"Mouse",
    "poung":"Goat",
    "Heou":"Sheep",
    "Kpanga":"donkey",
    "Gbanng-No":"Horse"
    
    }

inventair={
    "Chien":400,
    "chat":'neant',
    "Chevre":600,
    
    }

assembre ={
    "dic_1": traduction_1,
    "dict_2":inventair
    
    }
import numpy as np
parametre= {
    "w1": np.random.randn(10,100),
    "w2": np.random.randn(1,100),
    "w3": np.random.randn(10,1000),
    "w4": np.random.randn(1,10),
    "w5": np.random.randn(20,100)
    }

print(traduction_1.values())
print(traduction_1.keys())
print(len(traduction_1))
###ajout d'lement dans le tble&u

traduction_1["Kpakpa"]="Duck"
print(traduction_1)

## verifier si un element es dans le deictionnaire

print(traduction_1.get("Kpakpaya"))

## creer un dictionnaire à partir d'unz lise
paysCapytale={
    }

villes =("Paris", "Accra", 'Mango', 'Dakar')
pays=['Frace', "Ghana", 'Togo','Senegal']

paysCapytale.fromkeys(villes)
print(paysCapytale)

villes = ("Paris", "Accra", 'Mango', 'Dakar')
pays = ['France', "Ghana", 'Togo', 'Senegal']

# Créer un dictionnaire à partir des listes
paysCapitale = dict(zip(villes, pays))

# Afficher le dictionnaire résultant
print(paysCapitale)

for i in paysCapytale.items():
    print(i)


#####################################################################
## list comprehnesion : inserer la boucle for

liste_1 = []

for i in range(14):
    liste_1.append(i**2)
    
print(liste_1)

#######une liste comprehension consite à inserer une boucle for à ol'interrieur de la boucle la liste elle meme

liste_2 = [i**3 for i in range(25)]
print(liste_2)