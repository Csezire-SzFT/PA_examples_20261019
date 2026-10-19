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


def kor_ellenorzes():
   eletkor = get_integer("Kérem az életkorodat")
   if eletkor is None:
      print("Nem adtál meg életkort!")
   else:
      if eletkor < 18:
         print("Még nem vagy nagykorú.")
      else:
         print("Nagykorú vagy.")

def belepes():
   jelszo = input("Kérem a jelszót: ")
   if jelszo == "python123":
      return "Sikeres belépés!"
   else:
      return "Hibás jelszó!"

def paros_vizsgalat():
   paros_paratlan = get_integer("Kérek egy számot")
   if paros_paratlan is None:
      print("Nem adtál meg számot.")
   else:
      if paros_paratlan % 2 == 0:
         print("A szám páros.")
      else:
         print("A szám páratlan.")

def vizsgal(szam):
   if szam > 0:
      return "Pozitív."
   elif szam == 0:
      return "Nulla."
   else:
      return "Negatív."

def belepes_teljes():
   felhasznalo = input("Kérem a felhasználó nevét: ")
   jelszo = input("Kérem a jelszót: ")
   if felhasznalo == "admin" and jelszo == "python":
      return "Sikeres belépés!"
   elif felhasznalo == "admin" and jelszo != "python":
      return "Hibás jelszó!"
   elif felhasznalo != "admin":
      return "Ismeretlen felhasználó!"

def jegy(szazalek):
   if szazalek < 40:
      return "elégtelen"
   elif szazalek < 55:
      return "elégséges"
   elif szazalek < 70:
      return "közepes"
   elif szazalek < 85:
      return "jó"
   else:
      return "jeles"



#1. Bemelegítés a gyakorláshoz
bemelegites = get_number("Kérek egy számot")
if bemelegites is None:
   print("Nem adtál meg számot.")
elif bemelegites < 0:
   print("Negatív szám.")
elif bemelegites == 0:
   print("Nulla.")
else:
   print("Pozitív szám.")


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
   print("Hibás osztályzat!")
else:
   print(f"{osztalyzat}: { {1: 'elégtelen', 2: 'elégséges', 3: 'közepes', 4: 'jó', 5: 'jeles' }[osztalyzat] }")

#4. Metódus nélküli köszönés
koszones()

#5. Életkor-ellenőrző metódus
kor_ellenorzes()

#6. Jelszó ellenőrzés
print(belepes())

#7. Páros szám viszgálata metódussal
paros_vizsgalat()

#8. Pozitív szám vizsgálata paraméterrel
elojeles_szam = get_number("Kérek egy számot")
if elojeles_szam is None:
   print("Nem adtál meg számot.")
else:
   print(vizsgal(elojeles_szam))

#9. Beléptetési rendszer metódussal
print(belepes_teljes())

#10. Jegy meghatározása paraméterrel
ertekeles = get_number("Kérek egy %-os értékelést")
if ertekeles is None:
   print("Nem adtál meg értékelést.")
elif ertekeles < 0 or ertekeles > 100:
   print("Hibás százalék!")
else:
   print(f"Az {ertekeles}% eredménye: {jegy(ertekeles)}")

#11/1. Beléptetés első változat
eletkor = get_integer("Kérem az életkorodat")
if eletkor is None:
   print("Nem adtál meg életkort.")
else:
   kártya = get_integer("Van belépőkártyád? (1 = igen, más = nem)")
   if kártya is None:
      print("Nem adtál meg választ.")
   elif eletkor >= 18:
      if kártya == 1:
         print("Beléphetsz.")
      else:
         print("Nincs belépőkártyád.")

#11/2. Beléptetés második változat
eletkor = get_integer("Kérem az életkorodat")
if eletkor is None:
   print("Nem adtál meg életkort.")
else:
   kártya = get_integer("Van belépőkártyád? (1 = igen, más = nem)")
   if kártya is None:
      print("Nem adtál meg választ.")
   elif eletkor >= 18:
      if kártya == 1:
         print("Beléphetsz.")
   else: 
      print("Túl fiatal vagy a belépéshez.")

#11/3. Beléptetés harmadik változat
eletkor = get_integer("Kérem az életkorodat")
if eletkor is None:
   print("Nem adtál meg életkort.")
else:
   kártya = get_integer("Van belépőkártyád? (1 = igen, más = nem)")
   if kártya is None:
      print("Nem adtál meg választ.")
   elif eletkor >= 18:
      if kártya == 1:
         print("Beléphetsz.")
      else:
         print("Nincs belépőkártyád.")
   else:
      print("Túl fiatal vagy.")