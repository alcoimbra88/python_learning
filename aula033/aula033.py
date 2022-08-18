'''
    1 - Crie uma função1 que recebe uma funcao 2 como parametro e retorne o valor da funcao2
     executada

    2 - Crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2
    executada. Faça a funcao1 executar duas funcoes que recebam um numero diferente de argumentos
'''

#1

def func2():
     return '2'

def func1(funcao):
    return funcao()

executar = func1(func2)
print(executar)


#2

def mestre(funcao,*args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome,saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi,'Alan')
executando2 = mestre(saudacao,'Alan',saudacao='Bom Dia')
print(executando)
print(executando2)