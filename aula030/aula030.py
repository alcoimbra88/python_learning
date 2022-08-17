'''
    1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome

    2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.

    3 - Crie uma função que receba 2 números. O primeiro é uma valor e o segundo um percentual (ex: 10%).
        Retorne (return) o valor do primeiro número somado do aumento do percentual do mesmo.

    4 - Fizz Buzz - Se o parâmetro da função for divisivel por 2, retorne fizz, se o parâmetro da função for divisivel
        por 5 retorne buzz. Se o parâmetro da função for divisivel por 5 e por 3 retorna FizzBuzz, caso contrário,
        retorne o número enviado
'''

#1
def saudacao(saud, nome):
    print(saud, nome)

saudacao('Ola','Alan')

#2
def soma(n1, n2, n3):
    print(n1+n2+n3)

soma(2,3,5)

#3
def calculaPerc (numero,perc):
    perc = perc / 100
    diferenca = numero * perc
    print(numero + diferenca)

calculaPerc(200,36)

#4
def FizzBuzz(numero):
    if (numero % 3 == 0) and (numero % 5 == 0):
        print('FizzBuzz')
    else:
        if numero % 3 == 0:
            print('Fizz')
        elif numero % 5 == 0:
            print('Buzz')
        else:
            print(numero)

FizzBuzz(15)
