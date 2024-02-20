import kultBiblotek2 as kB
import filLeserBiblotek2 as fB

def tekst_editor(filbane):
    tekst = input(str("Skriv teksten du ønsker og legge til:"))
    ny_linje = kB.betterInput("str","Vil du ha ny linje? ","",forventet=["ja","nei","Ja","Nei"])
    if ny_linje =="ja":
        tekst = "\n" + tekst
    with open (filbane, "a", encoding="utf-8") as fil:
        fil.write(tekst)



def opprettFil(filbane):
    filbane +="/"+kB.betterInput("str","Hva skal den nye filen hete? ","Dette var ikke rett")+".txt"
    tekst =kB.betterInput("str","Hva skal stå i filen? ","Dette var ikke rett")
    fB.skrivTilNyFil(filbane,tekst,safe=False)
        



if __name__ == "__main__":
    tekst_editor ("test.txt")
    


