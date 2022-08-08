'''
While em Python
utilizado para realizar ações enquanto uma condição for verdadeiro
Requisitos: Entender condições e operadores
Contadores
Acumuladores
Else
'''

'''
x = 0
while x < 10:
    if x == 3:
        x= x+1
        continue

    print(x)
    x = x + 1

print("Acabou !")
==========================================
x = 0
y = 0
while x < 3:
    y = 0
    while y < 2:
        print (f'x: {x}, y: {y}')
        y = y+1

    x = x +1
'''

contador = 0
acumulador = ""

while contador < 10:
    if contador > 5:
        break # Não executa o else tb
    print(contador)
    contador += 1
    acumulador = acumulador + "A"
else:
    print("Acabou")

print(acumulador)