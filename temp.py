# -*- coding: utf-8 -*-

f= lambda X, y: X**2 + y

print(f(8,7))

def e_potentiel(mass, hauteur, g=9.81):
    Ep = mass*hauteur*g
    print(Ep, "Joules")
    return Ep

print("bonjour")

rusltat=e_potentiel(80, 8, 9.81)

rusltat=e_potentiel(mass=70, hauteur=78, g=9.81)

###################################################################

def signe(t):
        
    if True :
        print(t, "Possitif")
    elif t==0 :
        print("nul")
    else :
        print(t, "negatif")
    


###################################################################

def mutiple(n,m):
    print("Table de multiplication", n)
    for i in range(m+1):
        print(i,"*",n, "=", i*n)

mutiple(3,24)
        
def fibo(n):
    print("suite de fibonacci")
    f=1
    k=2
    print(f)
    print(k)
    for i in range(n):
        c=f+k
        print(c)
        f=k
        k=c
      
fibo(20)

def fibonacci(n):
    # Initialiser les deux premiers termes de la suite
    fib_sequence = [1, 2]

    # Générer les termes suivants jusqu'à atteindre n termes
    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence[:n]

# Utilisation de la fonction pour générer les 10 premiers termes de la suite de Fibonacci
n = 10
result = fibonacci(n)
print(result)

def fibo(n):
    print("Suite de Fibonacci :")
    a, b = 1, 2  # Les deux premiers termes de la suite
    print(a)    # Afficher le premier terme
    print(b)    # Afficher le deuxième terme
    for _ in range(n - 2):  # Nous avons déjà affiché les deux premiers termes
        c = a + b
        print(c)  # Afficher le terme actuel
        a, b = b, c  # Mettre à jour les deux derniers termes

fibo(20)

#####################################################################

### listes ; mlodifiables

villes =["Paris", "Accra", 'Mango', 'Dakar']
pays=['Frace', "Ghana", 'Togo','Senegal']

P_c= [villes, pays]

####tulpes

fruits = ("bananes","avocats","manges","prune") #non modifiables

#####String, 

prenom = "KOKolabakouwaguigninakouwarakatamatoun"

## le pas Liste[debut:fin:pas] ## sequence

print(villes[1:3])# debiut=1; fin=3; pas=0

print(villes[::2]) # debu=0 fin= dernier, pas=2

### iverser la seqieuence

print(villes[::-1])##" de la fin au debut

print(villes[-1:2:-1])

villes.append('Bamako') ## ajouter a la fin

villes.insert(2, "Niamey") ## insere aà la deuxieme place

print(villes)

villes_2= ["Yaka","New York","Caire", "Rabat"]

villes.extend(villes_2) ## fussion de deux listes

print(villes)


print(len(villes))## la taill

villes.sort() ## ranger par ordre alphabetique

print(villes)

nombre=[10,50,10,110,89,2.5,78,63.5,79,0.1]
nombre.sort()
print(nombre)

print(nombre.count(10))##X compter le nombre qu'un element se repetet dans une liste


############### Verifier la presence d'un element

if "Londres" in villes:
    print("Oui, son indix est : ", villes.index("Londres"))
else:
    villes.insert(3, "Londres")
    villes.sort()
    print(villes)
    
for i in villes :
    print(villes.index(i), i) # avec index

### ou ## avec enumerate
for i, valeur in enumerate(villes): # index de l'element
    print(i, valeur)

### deux listes

for a, b in zip(villes, nombre):
    print(a, b)
    
def fibonacci(n):
    # Initialiser les deux premiers termes de la suite
    fib_sequence = [1, 2]

    # Générer les termes suivants jusqu'à atteindre n termes
    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence[:n]

    

