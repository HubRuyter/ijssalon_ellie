from algemene_functies import mijn_functies_2


def aanbieding_1(smaak, prijs, korting):
    smaak = "aardbei"
    prijs = 4.00
    korting = 4.00 - 0.40

    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter), \nin de smaak {smaak} van € {prijs:.2f} voor € {korting:.2f}.")\



aanbieding_1(smaak="aardbei", prijs=4.00, korting=0.40)


def devider():
    print("================================================================")


devider()


BTW = 0.21


def inkomsten_totaal(inkomsten):
    inkomsten = sum([220 + 430 + 125 + 160 + 205 + 90 + 345])
    omzet = inkomsten * BTW
    print(f"Het totaal van alle inkomsten van deze week is €{inkomsten:.2f}, \nwaarover €{omzet:.2f} btw betaald dient te worden.")\



inkomsten_totaal(sum)


def devider():
    print("================================================================")


devider()

i = 0


def laag_en_hoog(mijn_lijst):
    for i in (mijn_lijst):
        if mijn_lijst[i] <= min_omzet:
            min_omzet = mijn_lijst[i]
        if mijn_lijst[i] >= max_omzet:
            max_omzet = mijn_lijst[i]
    return mijn_lijst


mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
print("Laagste bedrag is: €", (min(mijn_lijst)))
print("Hoogste bedrag is: €", (max(mijn_lijst)))


def devider():
    print("================================================================")


devider()


def gemiddelde(mijn_lijst):
    mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
    gemiddelde = sum(mijn_lijst) / len(mijn_lijst)
    print(f"De gemiddelde inkomsten deze week zijn: €{gemiddelde:.2f}")
    return mijn_lijst


gemiddelde(gemiddelde)


def devider():
    print("================================================================")


devider()


def meervoudig(invoer_lijst):
    a = max(invoer_lijst)
    b = min(invoer_lijst)
    print(a, b)
    return invoer_lijst


invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
meervoudig(invoer_lijst)


def devider():
    print("================================================================")


devider()

# Deze opdracht lukt mij van geen kant!


def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functies_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
