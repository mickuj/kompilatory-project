tokeny_kolory = {
    "komentarze": "grey; font-style: italic;",
    "napisy": "green",
    "liczby": "brown",
    "słowa_kluczowe": "blue; font-weight: bold;",
    "operatory": "purple",
    "identyfikatory": "black",
    "nawiasy": "yellow",
    "interpunkcyjne": "orange",
    "błąd": "red",
}

slowa_kluczowe = ["jeśli", "inaczej", "dopóki", "dla", "definiuj", "zwróć", "wypisz", "i", "lub", "nie", "prawda", "fałsz"]

def skaner(tekst, pozycja):
    start = pozycja
    token = tekst[pozycja]

    if token.isdigit():
        while pozycja < len(tekst) and tekst[pozycja].isdigit():
            pozycja += 1
        if pozycja < len(tekst) and tekst[pozycja] == '.':
            pozycja += 1
            while pozycja < len(tekst) and tekst[pozycja].isdigit():
                pozycja += 1
        return ("liczby", tekst[start:pozycja], start, pozycja)

    if token.isalpha() or token == "_":
        while pozycja < len(tekst) and (tekst[pozycja].isalnum() or tekst[pozycja] == "_"):
            pozycja += 1
        value = tekst[start:pozycja]
        if value in slowa_kluczowe:
            return ("słowa_kluczowe", value, start, pozycja)
        return ("identyfikatory", value, start, pozycja)

    if token == '"':
        pozycja += 1
        while pozycja < len(tekst) and tekst[pozycja] != '"':
            pozycja += 1
        pozycja += 1
        return ("napisy", tekst[start:pozycja], start, pozycja)

    if token == '#':
        while pozycja < len(tekst) and tekst[pozycja] != '\n':
            pozycja += 1
        return ("komentarze", tekst[start:pozycja], start, pozycja)

    if token in "+-*/=><":
        pozycja += 1
        return ("operatory", tekst[start:pozycja], start, pozycja)

    if token == "(" or token == ")":
        pozycja += 1
        return ("nawiasy", tekst[start:pozycja], start, pozycja)

    if token in ",;!?.:{}[\]'\"<>%&^":
        pozycja += 1
        return ("interpunkcyjne", token, start, pozycja)

    if token.isspace():
        while pozycja < len(tekst) and tekst[pozycja].isspace():
            pozycja += 1
        return ("biale", tekst[start:pozycja], start, pozycja)

    return ("błąd", token, start, start + 1)

def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            return plik.read()
    except FileNotFoundError:
        print("Błąd: Nie znaleziono pliku.")
        return None

def main():
    nazwa_pliku = input("Podaj nazwę pliku do analizy: ")
    tekst = wczytaj_plik(nazwa_pliku)
    
    if tekst is not None:
        pozycja = 0
        dlugosc = len(tekst)

        with open("wynik.html", "w", encoding="utf-8") as plik:
            plik.write('<html><body><pre>')
            
            while pozycja < dlugosc:
                znak = tekst[pozycja]
                
                kod, wartosc, start, koniec = skaner(tekst, pozycja)
              
                if kod == "biale":
                    plik.write(wartosc)
                else:
                    color = tokeny_kolory.get(kod, "white")
                    plik.write(f'<span style="color:{color};">{wartosc}</span>')
                
                pozycja = koniec
            plik.write('</pre></body></html>')

        print("Zapisano plik HTML jako 'wynik.html'")

if __name__ == "__main__":
    main()
