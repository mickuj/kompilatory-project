def skaner(tekst, token, pozycja):
    if token.isdigit():
        start = pozycja
        while pozycja < len(tekst) and tekst[pozycja].isdigit():
            pozycja += 1
        return ("liczba", tekst[start:pozycja], start, pozycja)

    if token.isalpha() or token == "_":
        start = pozycja
        while pozycja < len(tekst) and (tekst[pozycja].isalnum() or tekst[pozycja] == "_"):
            pozycja += 1
        return ("id", tekst[start:pozycja], start, pozycja)

    if token == "+":
        return ("dodawanie", token, pozycja, pozycja+1)

    if token == "-":
        return ("odejmowanie", token, pozycja, pozycja+1)

    if token == "*":
        return ("mnożenie", token, pozycja, pozycja+1)

    if token == "/":
        return ("dzielenie", token, pozycja, pozycja+1)

    if token == "(":
        return ("lewy nawias", token, pozycja, pozycja+1)

    if token == ")":
        return ("prawy nawias", token, pozycja, pozycja+1)

    else:
        return ("błąd", token, pozycja, pozycja+1)

def main():
    tekst = input("Wpisz wyrażenie do analizy: ")
    pozycja = 0
    dlugosc = len(tekst)
    
    while pozycja < dlugosc:
        znak = tekst[pozycja]
        if znak.isspace():
            pozycja += 1
            continue
        
        kod, wartosc, start, koniec = skaner(tekst, znak, pozycja)
        
        if kod != "błąd":
            print(kod, wartosc, start)
            
        pozycja = koniec

if __name__ == "__main__":
    main()
