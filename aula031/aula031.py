'''
    Funções (def) em Python - *args **kwargs -
    Aula 31
'''

# def func(a1,a2,a3=None,a4=None):
#     print(a1,a2,a3)
#
# var = func()
# ===================================================================
def func (*args):
    args = list(args) # cast para transformar em lista
    print(args)
    print(len(args))

# var = func()
lista = [1,2,3,4,5]
n1, n2, *n = lista

func(1,2,3,4,5)

print(*lista, sep='-')    #sep = separador

#Argumentos com palavras-chave
def func2(**kwargs):
    print(kwargs)
    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('Idade não foi inserida')

func2(nome='Alan', sobrenome='Coimbra')


