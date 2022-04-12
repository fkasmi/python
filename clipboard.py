import sys,pyperclip

texte=pyperclip.paste()

lines=texte.split('\n')
for i in range(len(lines)):
   lines[i] = '*' + lines[i]

texte='\n'.join(lines)
pyperclip.copy(texte)
