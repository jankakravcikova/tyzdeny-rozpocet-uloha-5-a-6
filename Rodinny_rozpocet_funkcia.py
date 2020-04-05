#Program na evidenciu bilancie rodinnych financii
#autor: Jana Kravcikova
#verzia: 1.1

from random import randint
def dennaBilanciaVydavkov():
    denneOperaciePocet= randint(0,100)
    denneOperacieSumy=[]
    for i in range (denneOperaciePocet):
                       denneOperacieSumy.append(randint(-1000,1000))
    celkovaBilancia=sum(denneOperacieSumy)
    return celkovaBilancia
   

