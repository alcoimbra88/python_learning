'''
    Conjuntos em Python (Set)

    add (adiciona), update(atualiza), clear, discard
    union | (une)
    intersection & (todos os elementos presentes nos dois sets)
    difference - (elementos apenas no set da esquerda)
    symmetryc_difference ^ (elementos que estão nos dois sets, mas não em ambos)
'''

s1 ={1,2,3,4,5}

for v in s1:
    print(v)

# Criar set vario
s2 = set()
s2.add(1)
s2.add(2)
s2.add(3)
s2.add(4)
s2.discard(2) # Remove o elemento
s2.update('Alan') # Itera e adiciona cada letra
print(s2)


# Nao aceita elementos duplicados
s3 = {1,1,2,2,3,3}
print(s3)

# Cast de lista para set
l1 = [1,1,2,2,3,3,4,4]
print(l1)
l1 = set(l1)
print(l1)
l1 = list(l1)
print(l1)

# Uniao de Sets
s4 = {1,2,3,4,5}
s5 = {1,2,3,4,5,6,7}
s6 = s4 | s5
print(s6)

# Interseccao (Mostra os elementos presente nos Sets)
s7 = {1,2,3,4,5}
s8 = {1,2,3,4,5,6,7}
s9 = s7 & s8
print(s9)

# Difference (elementos que estao presentes no set da esquerda)
s10= {1,2,3,4,5,6,7}
s11= {1,2,3,4,5}
s12= s10 - s11
print(s12)

# Symmetric_difference (Elementos diferentes em ambos)
s13= {1,2,3,4,5,6}
s14= {1,2,3,4,5,7}
s15= s13 ^ s14
print(s15)
