from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    totale_korting = prijs - korting * 4
    return f'Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {totale_korting} euro'

print (aanbieding_1('aardbei', 4, 0.10))   

def inkomsten_totaal(inkomsten, btw):
    totaal_inkomsten = sum(inkomsten)
    bedrag = round(totaal_inkomsten * btw)
    return f'Het totaal van alle inkomsten van deze week is {totaal_inkomsten} euro, waarover {bedrag} euro btw betaald dient te worden'

print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09))

def laag_en_hoog(mijn_lijst):
    return max(mijn_lijst), min(mijn_lijst)

print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

def gemiddelde(mijn_lijst):
    gemiddelde_inkomsten = sum(mijn_lijst) / len(mijn_lijst)
    return f'De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten} euro'

print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

print(meervoudig([10,5,3,2,1,2,9]))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer




     

    