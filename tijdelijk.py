from helper import decoreer


def print_aanbieding():
    prijzen = {
        "aardbeien": 3,
        "vanille": 4,
        "chocolade": 5
    }
    aanbieding = prijzen["aardbeien"] * 0.8

    reclame_tekst = f"Vandaag in de aanbieding: aardbeien-ijs, \
                    n1 liter - slechts € {aanbieding:.2}"

    reclame_tekst2 = reclame_tekst[:65]

    reclame_tekst3 = reclame_tekst2.upper()

    reclame_tekst4 = reclame_tekst3.split()
    print(reclame_tekst4)

    for el in reclame_tekst4:
        print(el)

    for el in reclame_tekst4:
        print(el.lower())

    for el in reclame_tekst4:
        if len(el) > 4:
            print(el.upper())
        else:
            print(el.lower())


decoreer("aanbieding")
print_aanbieding()
