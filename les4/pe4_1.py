cijferICOR = 6
cijferCSN = 6
cijferPROG = 6
totaal = (cijferICOR + cijferCSN + cijferPROG)
beloning = (totaal* 10)
gemiddelde = (totaal / 3)
line1 ='Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren mij een beloning van ' + str(beloning) + ' euro op.'
print(line1)