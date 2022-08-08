"""
    Enumerate  - Enumerar elementos da lista # list
"""

lista = [['Alan', 'Aline', 'Henrique'],
         ['Maria', 'Joel', 'Luna'],
         ['Albin', 'Simone', 'Barbara'],
         ]

# print(lista[1][2])

# enumerada = list(enumerate(lista))

# print(enumerada[1][1][2])

for v1 in enumerate(lista):
    valor_enumerado, minha_lista = v1
    nome1 ,nome2 , nome3 = minha_lista
    print(nome1,nome2,nome3)