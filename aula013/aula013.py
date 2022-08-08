'''
Manipulanto Strings
* Strngs indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
'''

texto = 'Python S2'

# Positivos
print(texto[2])

# Negativos
print(texto[-1])

url = 'www.google.com.br/'

print(url[:-1])

nova_string = texto[2:6]
print(nova_string)

nova_string2 = texto[0:6:2]
print(nova_string2)