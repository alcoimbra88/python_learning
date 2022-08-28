'''
    Perguntas e respostas com dicionarios
'''

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2 ?',
        'respostas': {
                'a':'1',
                'b':'4',
                'c':'5',
        },
        'resposta_certa':'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 * 2 ?',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6',
        },
        'resposta_certa': 'c'
    }
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}:{pv["pergunta"]}')
    print()
    print('Escolha a opção correta: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}] : {rv}')

    print()
    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('RESPOSTA CORRETA !')
        respostas_certas += 1
        print()
    else:
        print('Resposta Errada')
        print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas de {qtd_perguntas} perguntas')
print(f'Você acertou {porcentagem_acerto}% das perguntas')