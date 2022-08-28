'''
    Dicionário
'''


'''
d1 = {'chave1':'valor da chave'}
d1['nova chave'] = 'valor da nova chave'
d2 = dict(chave1 = 'Valor da chave', chave2 = 'Valor da outra chave')
d3 = {
    'str' : 'valor',
    123: 'Outro valor',
    (1,2,3) : 'Tupla'
}

print(d1)
print(d1['chave1'])
print(d2)
print(d3)

d1.update({'nova_chave':'novo_valor'})
print(d1)

#============ Deletar chave e valor =====
del d3['str']
print(d3)

#=============== Checagem =================
d1['naoexiste'] = 'Agora existe'
if 'naoexiste' in d1:
    print('nao existe')

if d1.get('naoexiste') is not None:
    print('da certo tambem')


print(123 in d3)
print('Outro valor' in d3.values())

print(len(d3))

#========== Iteracao ===================
for k,v in d3.items():
    print(k,v)
'''

clientes = {
    'cliente1': {
        'nome':'Alan',
        'sobrenome':'Coimbra'
    },
    'cliente2':{
        'nome':'Aline',
        'sobrenome':'Coimbra'
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k} :')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t {dados_k} = {dados_v}')

#========= Copia do dicionario ==================

d1 = {'nome1':'Alan','nome2':'Aline','nome3':'Henrique'}

import copy               # Importa o modulo de copia
v = copy.deepcopy(d1)      # Cria uma copia dao d1
v['nome1'] = 'Teste'

print(d1)
print(v)

lista = [
    ['c1',1],
    ['c2',2],
    ['c3',3]
]

d1 = dict(lista)   # Converte Lista para Dicionario
print(d1)

d2 = {
    1:2,
    2:3,
    3:4
}

d2.pop(3)  # pop Deleta o item desejado
print(d2)

d1.update(d2)  # Concatenar com outro dicionario
print(d1)
