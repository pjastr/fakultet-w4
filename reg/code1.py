
import re

def zamien_polskie_znaki(napis):
    polskie_do_lacinskich = {
        "ą": "a", "ć": "c", "ę": "e", "ł": "l", "ń": "n", "ó": "o", "ś": "s", "ź": "z", "ż": "z",
        "Ą": "A", "Ć": "C", "Ę": "E", "Ł": "L", "Ń": "N", "Ó": "O", "Ś": "S", "Ź": "Z", "Ż": "Z"
    }

    def zamien_znak(znak):
        return polskie_do_lacinskich.get(znak.group())

    wzorzec = r"[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]"
    napis_zamieniony = re.sub(wzorzec, zamien_znak, napis)
    return napis_zamieniony


tekst = "Zażółć gęślą jaźń, ąęśćńź żółć"
tekst_zamieniony = zamien_polskie_znaki(tekst)
print(tekst_zamieniony)