import re

tokeny = {
    "komentarze": r"#.*",
    "napisy": r'"[^"\n]*"',
    "liczby": r"\b\d+(\.\d+)?\b",
    "słowa_kluczowe": r"\b(jeśli|inaczej|dopóki|dla|definiuj|zwróć|wypisz|i|lub|nie|prawda|fałsz)\b",
    "operatory": r"(\+|-|\*|\/|=|>|<|>=|<=|==|!=)"
}

style = {
    "słowa_kluczowe": "color: blue; font-weight: bold;",
    "operatory": "color: purple;",
    "liczby": "color: red;",
    "napisy": "color: green;",
    "komentarze": "color: grey; font-style: italic;"
}

duzy_regex = "|".join(
    f"(?P<{name}>{pattern})" for name, pattern in tokeny.items()
)

def koloruj(linia):
    wynik = ""
    koniec_poprzedniego = 0
    for dopas in re.finditer(duzy_regex, linia):
        start, koniec = dopas.span()
        wynik += linia[koniec_poprzedniego:start]
        koniec_poprzedniego = koniec
        for nazwa in tokeny:
            if dopas.group(nazwa):
                wynik += f'<span style="{style[nazwa]}">{dopas.group(0)}</span>'
                break
    wynik += linia[koniec_poprzedniego:]
    return wynik

def do_html(plik_we, plik_wyj):
    with open(plik_we, "r", encoding="utf-8") as f:
        linie = f.readlines()

    kod_html = '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>polski python - kolor</title>
</head>
<body>
<pre>\n'''

    for linia in linie:
        kod_html += koloruj(linia)

    kod_html += '</pre>\n</body>\n</html>'

    with open(plik_wyj, "w", encoding="utf-8") as f:
        f.write(kod_html)

do_html("kod.txt", "wynik.html")
