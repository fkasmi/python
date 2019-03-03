import copy

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
