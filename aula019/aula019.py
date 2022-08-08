'''
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis
'''

string = "Uma frase aleatoria qualquer, ne ? E agora outra frase tosca, ne nao ? "
lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
print(lista_2)
frase = ''

# for valor in lista_1:
#     print(f'{valor} {lista_1.count(valor)}')

palavra = ''
contagem = 0

# for valor in lista_1:
#     qtd_vezes = lista_1.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print( f'A palavra que mais apareceu foi {palavra}')

# for valor in lista_2:
#     print(valor.strip())

string = 'O Brasil é penta'
lista = string.split(' ')
# string2 = ','.join(lista)
#
# print(string)
# print(lista)
# print(string2)

for indice, valor in enumerate(lista):
    print(indice, valor)
