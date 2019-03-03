import pyperclip

"""
sudo apt-get install python3-pip  
sudo pip3 install --upgrade pip
sudo pip3 install setuptools
sudo pip3 install pyperclip
"""

print(r'That\'s it man ! what\'s up.')
print(''' Salut 
Comment
ca
	va ?''')

"""
	TTTT
"""
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
