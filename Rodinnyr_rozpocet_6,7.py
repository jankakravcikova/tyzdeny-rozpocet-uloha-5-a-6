from Rodinny_rozpocet_funkcia import dennaBilanciaVydavkov

tyzdenneObraty=[]
for i in range(7):
    tyzdenneObraty.append(dennaBilanciaVydavkov())
print(tyzdenneObraty)

tyzdennaBilancia=sum(tyzdenneObraty)
if tyzdennaBilancia<=0:
    print('Tento tyzden sme neusetrili, prave naopak. Zostatok je:', tyzdennaBilancia,'eur')
else:
    print('Tento tyzden sa nam podarilo usetrit:',tyzdennaBilancia,'eur')
