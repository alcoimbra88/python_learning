'''
    Desempacotamento de listas com Python
'''

lista = ['Alan','Aline','Henrique','Lina','Omar']

n1,n2, *outra_lista , ultimo_da_lista= lista

print(n1,n2,outra_lista,ultimo_da_lista)