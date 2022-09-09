f = open('hasla.txt')
a = open("wynik4a.txt", "w")
b = open("wynik4b.txt", "w")
c = open("wynic4c.txt", "w")
parzyste = 0
nieparzyste = 0
ascii = []

# a) ile haseł ma parzystą, a ile nieparzystą ilość znaków?
# b) utwórz zestawienie haseł (po jednym w wierszu), które są palindromami
# c) zestawienie haseł (po jednym w wierszu) zawierających w sobie dwa kolejne znaki, których suma kodów ASCII wynosi 220

def kod(h):
    for i in range(0, len(h)-1):
        if ord(h[i]) + ord(h[i+1]) == 220:
            return True
    return False

for i in f:
    haslo = i.strip()

    if len(haslo)%2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

    if haslo == haslo[::-1]:
        b.write(haslo)
        b.write('\n')

    if kod(haslo):
        c.write(str(haslo))
        c.write('\n')

a.write('Ilość haseł parzystych:')
a.write('\n')
a.write(str(parzyste))
a.write('\n')
a.write('Ilość haseł nieparzystych:')
a.write('\n')
a.write(str(nieparzyste))

a.close()
b.close()
c.close()
f.close()