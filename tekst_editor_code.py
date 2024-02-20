import kultBiblotek2 as kB
def tekst_editor(filbane):
    tekst = input(str("Skriv teksten du ønsker og legge til:"))
    ny_linje = input(str("Vil du begynne på en ny linje?"))
    if ny_linje =="ja":
        tekst = "\n" + tekst
    with open (filbane, "a", encoding="utf-8") as fil:
        fil.write(tekst)
        fil.flush()
        fil.close()


def tell_ord(filbane):
    antall = 0
    with open(filbane,"r",encoding="utf-8") as fil:
        
        for linje in fil:
            ord_i_linje = linje.split()
            antall += len(ord_i_linje)
    print("Antall ord:", antall)


if __name__ == "__main__":
    tekst_editor ("test.txt")
    tell_ord ("test.txt")
