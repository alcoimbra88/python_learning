'''
Tipos de dados
str - string
int - inteiro
float - numero real / ponto flutuante
bool - booleano / lógico
'''

print('Alan',type('Alan'))  # classe type retorna o tipo do valor, no caso, string (str)
print(123,type(123))  # Aqui, inteiro (int)
print(1.3,type(1.3))  # Aqui, float (float)
print(10==10,type(10==10))  # Aqui, boolean (bool)
print(bool([]))

# Type casting (convertando tipo)
print('Alan', type('Alan'), bool('Alan'))  # Mudou o tipo para boolean (bool()), é possivel com outros tipos (str(), int(), etc)