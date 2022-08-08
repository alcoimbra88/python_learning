# Aula sobre formatacao de Strings

nome = 'Alan'
idade = 32
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso/ (altura ** 2)

print(nome, 'tem', idade, 'anos de idade')
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')  # f no começo ja exibe do jeito que esta
print('{0} tem {1} anos de idade e seu imc é {2:.2f}'.format(nome, idade, imc))  # o primeiro parametro sera 0 etc
print('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))  # atribuido a var