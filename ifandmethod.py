def get_number(message):
   message = message + " (kilépés: <Enter>): "
   get_text = input(message)
   if get_text == "":
      return None
   try:
      return float(get_text.replace(",", "."))
   except ValueError:
      return None
   
def get_integer(message):
   message = message + " (kilépés: <Enter>): "
   get_text = input(message)
   if get_text == "":
      return None
   try:
      return int(get_text)
   except ValueError:
      return None

def koszones():
   print("Szia! Örülök, hogy itt vagy!")


def kor_ellenorzes(eletkor):
   if eletkor < 18:
      return "Még nem vagy nagykorú."
   else:
      return "Nagykorú vagy."

def belepes():
   jelszo = input("Kérem a jelszót: ")
   if jelszo == "python123":
      return "Sikeres belépés."
   else:
      return "Hibás jelszó."

def paros_szam(szam):
   if szam % 2 == 0:
      return "A szám páros."
   else:
      return "A szám páratlan."

def pozitiv_szam(szam):
   if szam > 0:
      return "A szám pozitív."
   elif szam == 0:
      return "A szám nulla."
   else:
      return "A szám negatív."

def belepes_teljes():
   felhasznalo = input("Kérem a felhasználó nevét: ")
   jelszo = input("Kérem a jelszót: ")
   if felhasznalo == "admin" and jelszo == "python123":
      return f"Sikeres belépés, {felhasznalo}."
   elif felhasznalo == "admin" and jelszo != "python123":
      return "Hibás jelszó ."
   elif felhasznalo != "admin":
      return "Ismeretlen felhasználó."


#1. Bemelegítés a gyakorláshoz
bemelegites = get_number("Kérek egy számot")
if bemelegites is None:
   print("Nem adtál meg számot.")
elif bemelegites < 0:
   print("A megadott szám negatív.")
elif bemelegites == 0:
   print("A megadott szám nulla.")
else:
   print("A megadott szám: pozitív.")


#2. Szám bekérése egész számként, megvizsgálva, hogy páros vagy páratlan
paros_paratlen = get_integer("Kérek egy egész számot")
if paros_paratlen is None:
   print("Nem adtál meg egész számot.")
elif paros_paratlen % 2 == 0:
   print("A megadott szám páros.")
else:
   print("A megadott szám páratlan.")

#3. Osztályzat bekérése és kiértékelése
osztalyzat = get_integer("Kérek egy osztályzatot (1-5)")
if osztalyzat is None:
   print("Nem adtál meg osztályzatot.")
elif osztalyzat < 1 or osztalyzat > 5:
   print("Hibás osztályzat.")
else:
   print(f"{osztalyzat}: { {1: 'Elégtelen', 2: 'Elégséges', 3: 'Közepes', 4: 'Jó', 5: 'Jeles' }[osztalyzat] }")

#4. Metódus nélküli köszönés
koszones()

#5. Életkor-ellenőrző metódus
kor = get_integer("Kérem az életkorodat")
if kor is None:
   print("Nem adtál meg életkort.")
else:
   print(kor_ellenorzes(kor))

#6. Jelszó ellenőrzés
print(belepes())

#7. Páros szám viszgálata metódussal
paros_paratlan = get_integer("Kérek egy számot")
if paros_paratlan is None:
   print("Nem adtál meg számot.")
else:
   print(paros_szam(paros_paratlan))

#8. Pozitív szám vizsgálata paraméterrel
elojeles_szam = get_number("Kérek egy számot")
if elojeles_szam is None:
   print("Nem adtál meg számot.")
else:
   print(pozitiv_szam(elojeles_szam))

#9. Beléptetési rendszer metódussal
print(belepes_teljes())

#10. Jegy meghatározása paraméterrel
ertekeles = get_integer("Kérek egy %-os értékelést")
if ertekeles is None:
   print("Nem adtál meg értékelést.")
elif ertekeles < 0 or ertekeles > 100:
   print("Hibás értékelés.")
else:
   print(f"Az {ertekeles}% eredménye: {jegy(ertekeles)}")

