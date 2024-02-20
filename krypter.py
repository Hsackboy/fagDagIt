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
    'X': 'Å', 
    'Y': 'Æ', 
    'Z': 'Ø', 
    'Å': 'B', 
    'Æ': 'C', 
    'Ø': 'D'
}

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


if __name__ == "__main__":
    kryptert("test.txt")