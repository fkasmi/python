import pprint

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
