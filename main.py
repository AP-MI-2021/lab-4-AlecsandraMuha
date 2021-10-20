def citireLista():
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l
def nrnegative_nenule(l):
    '''
    afiseaza nr nenule negative din lista l
    :param l: lista data
    :return: nr negative nenule
    '''
    rezultat = []
    for x in l:
        if  x < 0 and x != 0:
            rezultat.append(x)
    return rezultat
def test_nrnegative_nenule():
    assert nrnegative_nenule([5,-1,6]) == [-1]
    assert nrnegative_nenule([]) == []
    assert nrnegative_nenule([-1,-1,-1]) == [-1,-1,-1]
def celmaimicnumarcucifraegala(l,c):
    '''
    afiseaza cel mai mic numar cu ultima cifra egala cu o cifra data
    :param l: lista de nr. intregi
    :param c: cifra citita de la tastatura
    :return:in variabila min cel mai mic numar cu ultima cifra egala cu o cifra data sau None daca nu exista
    '''
    min = None
    for x in l:
        if x % 10 == c and (min is None or x < min):
            min = x
    return min
def test_celmaimicnumarcucifraegala():
    assert celmaimicnumarcucifraegala([1, 6, 34, 68, 40, 48, 20], 8) == 48
    assert celmaimicnumarcucifraegala([1, 6, 34], 8) == None
    assert celmaimicnumarcucifraegala([1, 6, 34, 68, 40, 48, 28], 8) == 28
def is_prime(n):
    '''
    verificam daca un numar este prim sau nu
    :param n: numarul pe care il verificam daca este prim sau nu
    :return: True daca numarul este prim sau False in caz contrar
    '''
    if n<2:
        return False
    for d in range(2, int(n ** (1 / 2)) + 1):
        if n % d == 0:
            return False
    return True
def is_superprime(n):
    '''
    verificam daca un numar este superprim sau nu
    :return:True daca numarul este superprim sau False in caz contrar
    '''

    n = [int(i) for i in str(n)]
    nr = 0
    for i in n:
        nr = nr * 10 + i
        if is_prime(nr) == False:
            return False
    return True
def listais_superprime(l):
    '''
    verificam daca un numarele din lista sunt superprime sau nu
    :return:numerele din lista superprime
    '''
    rezul = []
    for x in l:
        if is_superprime(x) == True:
            rezul.append(x)
    return rezul
def test_listais_superprime():
    assert listais_superprime([239,17,22]) == [239]
    assert listais_superprime([ 17, 22]) == []
    assert listais_superprime([239]) == [239]
def cmmdc(m,n):
    '''
    calculeaza cmmdc al celor doua numere
    :param m: nr intreg
    :param n: nr intreg
    :return: cmmdl al numerelor
    '''
    while m!= n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return m

def printMenu():
    print("1. Citire lista")
    print("2. Afisarea tuturor nr. negaive nenule din lista.")
    print("3. Afisarea celui mai mic nr. care are ultima cifra egala cu o cifra de la tastatura .")
    print("4. Afișarea tuturor numerelor din listă care sunt superprime.")
    print("5. Afișarea listei obținute din lista inițială"
          " în care numerele pozitive și nenule au fost înlocuite cu"
        "CMMDC-ul lor și numerele negative au cifrele în ordine inversă.")
    print("6.Iesire")
def main():
    test_nrnegative_nenule()
    test_listais_superprime()
    test_celmaimicnumarcucifraegala()
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(nrnegative_nenule(l))
        elif optiune == "3":
            c = int(input("Dati un nr.: "))
            min = celmaimicnumarcucifraegala(l, c)
            if min is None:
                print("Nu exista")
            else:
                print(min)
        elif optiune == "4":
            print(listais_superprime(l))
        elif optiune == "5":
            pass
        elif optiune == "6":
	        break
        else:
            print("Optiune gresita! Alege alta optiune!")

if __name__ == '__main__':
    test_celmaimicnumarcucifraegala()
    test_listais_superprime()
    test_nrnegative_nenule()


main()