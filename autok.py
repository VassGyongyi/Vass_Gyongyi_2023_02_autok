from Auto import Auto

auto_lista= []
def feldolgoz():
    f = open('auto.txt', 'r', encoding='utf-8')
    f.readline().strip()
    sorok = f.readlines()
    f.close()
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("$")
        #print(sor)
        auto_lista.append(Auto(sor))

        i += 1
    #print(auto_lista)

def flotta():
    print('III/Flotta:')
    print(f'\tAutók száma: {len(auto_lista)}')

def legfiatalabb():
    i = 0
    min = auto_lista[0].datum
    index = 0
    while i <len(auto_lista):
        if auto_lista[i].datum > min:
            min = auto_lista[i].datum
            index = i
        i += 1
    print('III/Legfiatalabb')
    print(f'\tA legfiatalabb autó: {auto_lista[index].nev}({auto_lista[index].datum})')

