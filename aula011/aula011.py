'''
Chegagem de tipo
'''

num1 = input('Digite um numero: ')
num2 = input('Digite um numero: ')

#isnumeric isdigit isdecimal


if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('Digite somente numeros')