#Bienvenue Jeune Padawan ! 
#Aujourd'hui ça part sur du Python 

"""
pour les commentaires
Tu peux aussi fonctionner comme ça
"""

print("Hello, World!")

print("La version actuelle de Python est :")
import sys

print(sys.version)

x = 27 #Déclarer des variables n'a jamais été aussi simple !
y = "Le chiffre porte-bonheur est :" #Simple ou double quote, les deux fonctionnent

print(y,x)

#Je souhaite modifier les deux variables connues

x = "La réponse à LA question de l'univers est :"
y = float(42)

print(x,y)

#Pour connaître le type de donnée d'une variable 

print(type(x))
print(type(y))

#Tous les noms possibles pour déclarer une variable

name = 'JB'
_name = 'JB'
name_1 = 'JB'
name1 = 'JB'
Name = 'JB2'

#ou autre façon de les déclarer si certaines sont égales

name = _name = name_1 = name1 = 'JB'
Name = 'JB2'

print(name,_name,name_1,name1,Name)

cucurbitacées = ["courge", "potiron", "citrouille", "potimarron"]
a, b, c, d = cucurbitacées

print("Les différents cucurbitacées sont :")
print('-',a)
print('-',b)
print('-',c)
print('-',d)


#utilisons maintenant une fonction 

x = "bleu"

def myfunc():
    print("toute",x)
    
myfunc()


a = "Nous allons maintenant essayer \nplusieurs possibilités d' \"introduire\" dans le texte\ndes mots\nainsi que des espaces."

print(a)

#Rajout de commentaire pour MAJ

