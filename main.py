from filFinner import *
from tekst_editor_code import *
import os 
import kultBiblotek2 as kB
from krypter import *

startFilbane = os.getcwd()


valg = kB.betterInput("str","Vil du velge en fil eller opprette en ny? (velge/ny) ","",forventet=["velge","ny"])

if valg=="velge":
    filbane = finnFil(startFilbane)
    valg = kB.betterInput("str","Vil du redigere filen, telle ord eller telle tegn? (redigere/ord/tegn/kryptere/dekryptere) ","",forventet=["redigere","ord","tegn","kryptere","dekryptere"])
    if valg=="redigere":
        tekst_editor(filbane)
    elif valg == "ord":
        tell_ord(filbane)
    elif valg=="tegn":
        tell_tegn(filbane)
    elif valg=="kryptere":
        kryptert(filbane)
    elif valg=="dekryptere":
        dekrypter(filbane)
else:
    opprettFil(startFilbane)
    



