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


FORSKJØVET_ALFABET = {
    'A': 'D', 
    'B': 'E', 
    'C': 'F',
    'D': 'G', 
    'E': 'H', 
    'F': 'I', 
    'G': 'J', 
    'H': 'K', 
    'I': 'L', 
    'J': 'M',
    'K': 'N', 
    'L': 'O', 
    'M': 'P', 
    'N': 'Q', 
    'O': 'R', 
    'P': 'S', 
    'Q': 'T', 
    'R': 'U', 
    'S': 'V', 
    'T': 'W',
    'U': 'X', 
    'V': 'Y', 
    'W': 'Z', 
    'X': 'Æ', 
    'Y': 'Ø', 
    'Z': 'Å', 
    'Æ': 'A', 
    'Ø': 'B', 
    'Å': 'C'
}


def dekrypter(filbane, forskyvning=3):
    tekst = ""
    with open(filbane, encoding="utf-8") as fil:
        tekst = fil.read()
        fil.close()
    (*tekst,) = tekst
    dekryptertTekst = ""
    for i in range(len(tekst)):
        if tekst[i].lower() in ALFABET:
            posisjon = ALFABET.index(tekst[i].lower())  -forskyvning
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



def kryptert(filbane):
    krypter_tekst = ""
    with open(filbane, encoding="utf-8") as fil:
        for tekst in fil:
            *tekst, = tekst
            for tegn in tekst:
                try:
                    krypter_tekst += FORSKJØVET_ALFABET[tegn.upper()]

                except:
                    krypter_tekst += tegn
    print(krypter_tekst)
    with open(filbane, "w", encoding="utf-8") as fil:
        fil.write(krypter_tekst)
        fil.flush()
        fil.close()


if __name__ == "__main__":
    # kryptert("hei.txt")
    dekrypter("hei.txt")
