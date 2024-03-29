import kultBiblotek2 as kB
import filLeserBiblotek2 as fB

def tekst_editor(filbane):
    tekst = input(str("Skriv teksten du ønsker og legge til:"))
    ny_linje = kB.betterInput("str","Vil du ha ny linje? ","",forventet=["ja","nei","Ja","Nei"])
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




def opprettFil(filbane):
    filbane +="/"+kB.betterInput("str","Hva skal den nye filen hete? ","Dette var ikke rett")+".txt"
    tekst =kB.betterInput("str","Hva skal stå i filen? ","Dette var ikke rett")
    fB.skrivTilNyFil(filbane,tekst,safe=False)
        
def tell_tegn(filbane,vis=True):
    tekst = fB.lesHelFil(filbane)
    tekst = tekst.replace("\n","")
    tekst = tekst.replace("\t","")
    *tekst, = tekst
    if vis:
        print("antall tegn er: ",len(tekst))
    return len(tekst)


if __name__ == "__main__":
    # tekst_editor ("test.txt")
    tell_tegn ("test.txt")
    


