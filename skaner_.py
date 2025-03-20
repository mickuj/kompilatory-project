def skaner(tekst):
    pozycja = 0
    dlugosc = len(tekst)

    while pozycja < dlugosc:
        znak = tekst[pozycja]
        if znak.isspace():
            pozycja += 1
            continue

        if znak.isdigit():
            start = pozycja
            while pozycja < dlugosc and tekst[pozycja].isdigit():
                pozycja += 1
            yield ("liczba", tekst[start:pozycja], start)
            continue

        if znak.isalpha() or znak == "_":
            start = pozycja
            while pozycja < dlugosc and (tekst[pozycja].isalnum() or tekst[pozycja] == "_"):
                pozycja += 1
            yield ("id", tekst[start:pozycja], start)
            continue

        if znak in "+":
            yield ("dodawanie", znak, pozycja)
            pozycja += 1
            continue

        if znak in "-":
            yield ("odejmowanie", znak, pozycja)
            pozycja += 1
            continue

        if znak in "*":
            yield ("mnożenie", znak, pozycja)
            pozycja += 1
            continue

        if znak in "/":
            yield ("dzielenie", znak, pozycja)
            pozycja += 1
            continue

        if znak in "(":
            yield ("lewy nawias", znak, pozycja)
            pozycja += 1
            continue

        if znak in ")":
            yield ("prawy nawias", znak, pozycja)
            pozycja += 1
            continue

        else:
            yield ("błąd", znak, pozycja)
            pozycja += 1

tekst = input("Wpisz wyrażenie do analizy: ")
wynik = skaner(tekst)

for tokeny in wynik:
    print(tokeny)