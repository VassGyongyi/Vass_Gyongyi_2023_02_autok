import random

lista = []

def veletlen():
    i = 0
    while i < 5:
        vel = random.randint(1,90)
        lista.append(vel)
        i += 1
    print(lista)

def konzol_kiir_elso():
    i = 0
    kimenet = " "
    while i < len(lista):
        if i == len(lista)-1:
            kimenet += str(lista[i])
        else:
            kimenet += str(lista[i]) + ";"
        i += 1
    print('II/A, B, C:')
    print(f'\t{kimenet}')

def egyjegyuek_szama():
    i = 0
    db = 0
    while i < len(lista):
        if lista[i] < 10:
            db += 1
        i += 1
    return db
def konzol_kiir():
    print('II/D, E:')
    print(f'\tAz egyjegyűek száma : {egyjegyuek_szama()}')

def file_kiir():
    f = open('szamok.txt', 'w', encoding='utf8')
    f.write(f'{egyjegyuek_szama()}')
    f.close()
