'''
Formatando valores com modificadores - Aula 5

:s - Texto (Strings)
:d - Inteiros (Int)
:f - numeros de ponto flutuante (float)
:.(NUMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
'''

num1 = 10
num2 = 222
num3 = 10.5
nome = 'Alan'
nome_formatado = '{:$>50}'.format(nome)
nome_formatado2 = '{n:0<10} {n1:0^10} {n2:0<10}'.format(n=nome, n1=num1,n2=num2)
nome_formatado3 = nome.ljust(20, '#')
nome_formatado4 = nome.rjust(20, '#')
nome_formatado5 = nome.lower()  # tudo minusculoa
nome_formatado7 = nome.upper()  # tudo maiusculo
nome_formatado8 = nome.title()  # primeiras letras maiusculas

divisao = num1 / num2

print(f'{num1:0>10}')
print(f'{num2:0^10}')
print(f'{num3:.3f}')
print(f'{nome:#<50}')
print(f'{nome:#^50}')
print(f'{nome:#>50}')
print(f'{nome_formatado}')
print(f'{nome_formatado2}')
print(f'{nome_formatado3}')
print(f'{nome_formatado4}')

