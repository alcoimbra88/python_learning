'''
    Operador Ternário em Python
'''
'''
logged_user = False
msg = 'Usuário Logado' if logged_user else 'Usuário precisa Logar'
'''

idade = input('Qual sua idade?')

if not idade.isnumeric():
    print('Digite apenas numeros')
else :
    idade = int(idade)
    e_maior = (idade >= 18)
    msg = 'Pode acessar' if e_maior else 'Não pode acessar'

print(msg)