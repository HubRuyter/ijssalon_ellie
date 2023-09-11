#2
def print_aanbieding():
    prijzen = {
        "aardbeien" : 3,
        "vanille" : 4,
        "chocolade" : 5
    }

    #3
    aanbieding = prijzen ["aardbeien"] * 0.8
    #4
    reclame_tekst = f"Vandaag in de aanbieding: aardbeien-ijs, 1 liter - slechts € {aanbieding}"
    #5
    reclame_tekst2 = reclame_tekst [:65]
    #6
    reclame_tekst3 =  reclame_tekst2.upper()
    #7
    reclame_tekst4 = reclame_tekst3.split()
    #8
    for el in reclame_tekst4:
            print (el)
    #9
    for el in reclame_tekst4:
            print (el.lower())
    #10
    for el in reclame_tekst4:
        if len(el) > 4:
            print(el.upper())
    else:
            print(el.lower())

print_aanbieding()