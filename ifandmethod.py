def get_number(message):
   message = message + "(kilépés: <Enter>):"
   get_text = input(message)
   if get_text == "":
      return None
   try:
      return float(get_text.replace(",", "."))
   except ValueError:
      return None
   
def get_integer(message):
   message = message + "(kilépés: <Enter>):"
   get_text = input(message)
   if get_text == "":
      return None
   try:
      return int(get_text)
   except ValueError:
      return None

#Bemelegítés a gyakorláshoz
bemelegites = get_number("Kérek egy számot")
if bemelegites is None:
   print("Nem adtál meg számot.")
elif bemelegites < 0:
   print("A megadott szám negatív.")
elif bemelegites == 0:
   print("A megadott szám nulla.")
else:
   print("A megadott szám: pozitív.")


# Szám bekérése egész számként
egesz_szam = get_integer("Kérek egy egész számot")
