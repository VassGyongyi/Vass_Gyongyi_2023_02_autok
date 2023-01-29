
def bekeres():
    nev = input('Autó  neve:')
    ev = int(input('Gyártási dátum: '))
    print('I/A:')

    if ev == 2023:
        print(f'\tEz az {nev} friss gyártás.')
    elif ev < 2000:
        print(f'\tEz az {nev} öreg autó.')
    else:
        print(f'\tEz az {nev} átlagos korú.')