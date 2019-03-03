import pprint
import copy
import pyperclip
"""
sudo apt-get install python3-pip  
sudo pip3 install --upgrade pip
sudo pip3 install setuptools
sudo pip3 install pyperclip
"""


# la partie dictionaire

'''
afficher_valeur_dico(d)
afficher_cle_dico(d)
afficher_item_dico(d)
valeur_dans_dico(d,valeur)
cle_dans_dico(d,cle)
init_dico(d,cle,valeur)
supprime_valeur_dico(d,cle)

spam ={'color':'red','age':42}

exemples :

spam ={'color':'red','age':42}
afficher_valeur_dico(spam)
print("***"*5)
afficher_cle_dico(spam)
print("***"*5)
afficher_item_dico(spam)
print("***"*5)
print(valeur_dans_dico(spam,42))
print("***"*5)
print(cle_dans_dico(spam,'color'))
print("***"*5)
print(init_dico(spam,'poids',555))


'''

def afficher_valeur_dico(d):
	for v in d.values():
		print(v)

def afficher_cle_dico(d):
	for v in d.keys():
		print(v)

def afficher_item_dico(d):
	for v in d.items():
		print(v)
		
def valeur_dans_dico(d,valeur):
	return valeur in d.values()		

def cle_dans_dico(d,cle):
	return cle in d.keys()
	
def init_dico(d,cle,valeur):
	d.setdefault(cle,valeur)
	return d

def supprime_valeur_dico(d,cle):
	return del d[cle]	

### la partie liste

def longueur_liste(l):
	return len(l)
	
def sous_liste(l,a,b):
	return l[a:b]	

def remplacer_valeur(l,a,valeur):
	l[a]=valeur
	return l
	
def concatener_liste(l1,l2):
	return l1+l2	
	
def repliquer_liste(l,valeur):
	return l*valeur	
	
def effacer_liste_valeur(l,valeur):
	del l[valeur]
	return l	

def retrouver_position_liste(l,valeur):
	return l.index(valeur)

def ajouter_fin_liste(l,valeur):
	l.append(valeur)	
	return l	
	
def insertion_liste(l,position,valeur):
	l.insert(position,valeur)	
	return l	
	
def trier_liste(l):
	l.sort()			
	return l
	
def trier_liste_inverse(l):
	l.sort(reverse=True)			
	return l

def trier_liste_caractere(l):
	l.sort(key=str.lower)			
	return l		

def copier_liste(l1,l2):
	l2=copy.copy(l1)
	return l2
	
def copier_liste_v2(l1,l2):
	#copie de liste de listes
	l2=copy.deepcopy(l1)
	return l2
	
def vider_liste(l):
	l.clear()
	return l
	
def etendre_liste(l,valeur):
	l.extend(valeur)
	return l
	
def supprimer_fin_liste(l):
	l.pop()
	return l
	
def occurence_liste(l,valeur):
	return l.count(valeur)				
	
def string_en_liste(s,symbole):
		return s.split(symbole)
		
def liste_en_string(l,symbole):
		return symbole.join(l)
		
		

def effacer_liste_toute_valeur(l,valeur):
	while valeur in l:
		l.remove(valeur)
	return l

'''
exemples
l=[1,2,3,4]
m=[5,7,9,4,4,5]
n=['a','Z','b','C']
t=[]
#on affiche la longueur de l
print(longueur_liste(l))
#on affiche un extract de l
print(sous_liste(l,1,3))
#on affiche la nouvelle valeur
print(remplacer_valeur(l,1,9))
#on affiche la concatenation
print(concatener_liste(l,m))
#on affiche la replication
print(repliquer_liste(l,5))
#on affiche la suppression de la valeur
print(effacer_liste_valeur(l,1))
#on affiche la suppression de toutes les valeurs
print("****"*5)
print(effacer_liste_toute_valeur(m,5))

#on affiche la position de la valeur
print(retrouver_position_liste(l,4))

#on affiche l'ajout en fin de liste de la valeur
print(ajouter_fin_liste(l,44))

#on affiche l'insertion de la valeur
print(insertion_liste(l,1,74))

#on affiche la liste triee
print(trier_liste(l))

#on affiche la liste triee inverse
print(trier_liste_inverse(l))


#on affiche la liste triee inverse
print(trier_liste_caractere(n))

#on affiche la liste copiee
print(copier_liste_v2(n,t))


st='f a r i d'
lt=[]
print(string_en_liste(st,' '))
print(liste_en_string(n,'%'))
print(m)
print(occurence_liste(m,4))
vider_liste(m)
print(etendre_liste(l,n))
print(supprimer_fin_liste(etendre_liste(l,n)))
'''

# la partie string

def MAJ(s):
	return s.upper()
	
def MIN(s):
	return s.lower()
	
def IS_MIN(s):
	return s.islower()		

def IS_MAJ(s):
	return s.isupper()

def IS_LETTER(s): # seulement des lettres
	return s.isalpha()

def IS_MIX(s): # mix
	return s.isalnum()

def IS_DECIMAL(s): # seulement chiffres
	return s.isdecimal()	
	
def IS_SPACE(s): # seulement espace
	return s.isspace()
	
def IS_TITLE(s): # seulement si 1er car majuscule suivi min
	return s.istitle()		

def IS_BEGIN_WITH(s,word): # mot commence par word ?
	return s.startswith(word)		

def IS_END_WITH(s,word): # mot finit par word ?
	return s.endswith(word)		

def string_en_liste(s,symbole):
		return s.split(symbole)
		
def liste_en_string(l,symbole):
		return symbole.join(l)

def justifie_gauche(s,valeur,symbole):
	return s.rjust(valeur,symbole)		

def justifie_droite(s,valeur,symbole):
	return s.ljust(valeur,symbole)	

def justifie_centre(s,valeur,symbole):
	return s.center(valeur,symbole)	

def supprime_espace(s):
	return s.strip()

def supprime_espace_gauche(s):
	return s.lstrip()	

def supprime_espace_droit(s):
	return s.rstrip()	

'''
ex
mot='coucou cA va'	
print(MAJ(mot))
print(MIN(mot))
print(IS_MAJ(mot))
print(IS_MIN(mot))
print(IS_LETTER(mot))
print(IS_MIX(mot))
print(IS_DECIMAL(mot))
print('***'*5)
print(IS_END_WITH(mot,'va'))
print('***'*5)

print(justifie_gauche(mot,15,'-'))
print('***'*5)
print(justifie_gauche(mot,25,'+'))
print('***'*5)
print(justifie_centre(mot,35,'%'))



print(pyperclip.paste())
'''


