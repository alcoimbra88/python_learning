'''
    Dicionário
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