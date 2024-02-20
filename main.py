from filFinner import *
from tekst_editor_code import *
import os 
import kultBiblotek2 as kB

startFilbane = os.getcwd()


valg = kB.betterInput("str","Vil du velge en fil eller opprette en ny? (velge/ny) ","",forventet=["velge","ny"])

if valg=="velge":
    filbane = finnFil(startFilbane)
    valg = kB.betterInput("str","Vil du redigere filen, telle ord eller teller bokstaver? (redigere/ord/bokstaver) ","",forventet=["redigere","ord","bokstaver"])
    if valg=="redigere":
        tekst_editor(filbane)
    elif valg == "ord":
        pass # Legg kode her
    else:
        pass #legg kode her
else:
    opprettFil(startFilbane)
    



