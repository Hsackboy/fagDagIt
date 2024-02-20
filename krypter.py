ALFABET = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "æ",
    "ø",
    "å",
]


def dekrypter(filbane, forskyvning=3):
    tekst = ""
    with open(filbane, encoding="utf-8") as fil:
        tekst = fil.read()
        fil.close()
    (*tekst,) = tekst
    dekryptertTekst = ""
    for i in range(len(tekst)):
        if tekst[i].lower() in ALFABET:
            posisjon = ALFABET.index(tekst[i].lower()) - forskyvning
            if posisjon >= len(ALFABET):
                posisjon += -len(ALFABET)
            dekryptertTekst += ALFABET[posisjon]
        else:
            dekryptertTekst += tekst[i]

    print(dekryptertTekst)

    with open(filbane, "w", encoding="utf-8") as fil:
        fil.write(dekryptertTekst)
        fil.flush()
        fil.close()


if __name__ == "__main__":
    dekrypter("test20.txt", 3)
