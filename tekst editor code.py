filbane = "testen_min.txt"

tekst = input(str("Skriv teksten du ønsker og legge til:"))

ny_linje = input(str("Vil du begynne på en ny linje?"))
if ny_linje =="ja":
    tekst = "\n" + tekst

with open (filbane, "a", encoding="utf-8") as fil:
    fil.write(tekst)


