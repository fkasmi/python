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


stuff={"rope":1,"torch":6,"gold coin":42,"dagger":1,"arrow":12}

def displayInventory(inventory):
    print("Inventory:")
    item_total=0
    for k,v in inventory.items():
        print(k + " " + str(v))
        item_total=int(v)+item_total
    print("Total number of items: " + str(item_total))
    
displayInventory(stuff)

print("***"*5)
print(cle_dans_dico(spam,'color'))
print("***"*5)
print(init_dico(spam,'poids',555))


stuff={"rope":1,"torch":6,"gold coin":42,"dagger":1,"arrow":12}
dragon=['gold coin','dagger','gold coin','gold coin','ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total=0
    for k,v in inventory.items():
        print(k + " " + str(v))
        item_total=int(v)+item_total
    print("Total number of items: " + str(item_total))
    
#displayInventory(stuff)

def addToInventory(inventory,addedItems):
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i]=inventory[i]+1
    return inventory

updatedstuff=addToInventory(stuff,dragon)
displayInventory(updatedstuff)
