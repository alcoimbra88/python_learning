'''
Listas em Python
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
'''

# lista = ['A','L','A','N']

# print(lista)
# print(lista[0:3]) #  Do indice 0 ao 2 (3 primeiros itens)
# print(lista[::2]) # Pula de 2 em 2 (omitiu o inicio, omitiu o fim e step 2)
# print(lista[::-1]) # Invertido

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
l4 = [7,8,9]
l3.extend(l4) # adiciona l4 em l3
l5 = 10
l3.append(l5) # inclui o valor de l5 no final de l3
l6 = 11
l3.insert(0,l6) # insere o valor de l6 onde for o indice
l3.pop() # retira o ultimo elemento da lista
del(l3[3:5]) #  Exclui os valores do indice 3 ao 5
l7 = list(range(1,10,2))  #  range de 1 a 10.  Pulando de 2 em 2

print(l1)
print(l2)
print(l4)
print(l5)
print(l6)
print(l3)
print(max(l3))  # maior valor da lista
print(min(l3))  # menor valor da lista
print(l7)


