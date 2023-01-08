from math import*
from random import*

# harjutus 1
#try:
#    nimi=input("Mis on sinu nimi? ")

#    if (nimi.upper == "JUKU"):
#        print("lähme kinno")
#    else:
#        print("Otsime Juku")
#        vanus=int(input("Kui vana sa oled? "))
#    if (vanus <=5):
#        print(f"{vanus} - tasuta")
#    elif(vanus <=14):
#        print(f"{vanus} - lastepilet")
#    elif(vanus <=64):
#        print(f"{vanus} - täispilet")
#    elif(vanus >=99 ):
#        print(f"{vanus} - sooduspilet")
#    elif(vanus >100 or vanus<0):
#        print(f"{vanus} - viga andmed")
#    else:
#        print("Küsime kui vana ta on?")
#except:
#    print("Vale andmed")

# harjutus 2
#nimi1=input("Mis on sinu nimi? ")
#nimi2=input("Mis on sinu nimi? ")
#if nimi1.isalpha() and nimi2.isalpha():
#	if nimi1.upper() == "MAKSIM" and nimi2.upper() == "OLEKSANDR":
#		print(f"{nimi1} ja {nimi2} - olete täna naabrid")
#	else:
#		print("Küsime kus on Maksim ja Oleksandr")
#else:
#	print("Vale nimi")

# harjutus 3

#try:
#	pikkus=float(input("Kui pikk on sein? "))
#	laius=float(input("Kui lai on sein? "))
#	if pikkus>0 and laius>0:
#		pindala=pikkus*laius
#		print(f"Pindala on : {pindala}")
#		vastus1=input("Kas teeme remondi? jah või ei? ")
#	if vastus1=="jah":
#		vastus2=float(input("Kui palju maksab ruutmeeter? "))
#	if vastus2<0:
#		print("Vastus on vale")
#	else:
#		põrand=vastus2*pindala
#		(f"remondi summa on: {põrand}")
#except:
#	print("Vale info")

# harjutus 4
#try:
#	hind=float(input("Mis on hind? "))
#	if hind>700:
#		hind=round(700*0.7,2)
#		print(f"hind soodusega on {hind}")
#	else:
#		print("Selle hinnale pole soodustust")
#except:
#	print("Hind peab olema numbris")

# harjutus 5
#try:
#    n=int(input("Mitu toa korteris? "))
#    for i in range(1,n+1,1):
#        temperatuur=float(input(f"{i}. toas temperatuur on? "))
#        if temperatuur>=18:
#            print(f"{temperatuur} on soe")
#        else:
#            print("Peab soojendama toa")
#except:
#    print("vale andme info")

# harjutus 6
#try:
#    s=k=l=0
#    kogus=randint(1,20)
#    print("kokku on",kogus,"inimest")
#    #for i in range(1,kogus+1,1):
#    while kogus>0:
#        kogus-=1
#        pikkus=randint(56,256)
#        if pikkus<=165:
#            print(f"{pikkus} on lühike suurus")
#            l+=1
#        elif pikkus<=185:
#            print(f"{pikkus} on keskmine suurus")
#            k+=1
#        else:
#            print(f"{pikkus} on suur suurus")
#            s+=1
#    print(f"lühike suurusega on {l}")
#    print(f"keskmine suurusega on {k}")
#    print(f"suure suurusega on {s}")
#except:
#    print("Vale andmetüüp")

# harjutus 7

#try:
#    pikkus=float(input("Milline on sinu pikkus? "))
#    sugu=input("Milline on sinu sugu? mees või naine? ")
#    if sugu=="mees":
#        if pikkus<=165 and sugu.lower()=="mees":
#            print(f"{pikkus} on lühike suurus")
#        elif pikkus<=185 and sugu.lower()=="mees":
#            print(f"{pikkus} on keskmine suurus")
#        else:
#            print(f"{pikkus} on suur suurus")
#    if sugu=="naine":
#        if pikkus<=160 and sugu.lower()=="naine":
#            print(f"{pikkus} on lühike suurus")
#        elif pikkus<=180 and sugu.lower()=="naine":
#            print(f"{pikkus} on keskmine suurus")
#        else:
#            print(f"{pikkus} on suur suurus")
#except:
#    print("Vale andmetüüp")

# harjutus 8

#try:
#    piim=input("Kas te soovite osta piima? jah või ei? ")
#    sai=input("Kas te soovite osta saia? jah või ei? ")
#    leib=input("Kas te soovite osta leiba? jah või ei? ")
#    piimahind=1
#    saiahind=1
#    leibahind=1.5
#    if piim.lower()=="jah":
#        print(f"piima eest: {piimahind} euro")
#    if sai.lower()=="jah":
#        print(f"saia eest: {saiahind} euro")
#    if leib.lower()=="jah":
#        print(f"leiba eest: {leibahind} euro")
#    if piim.lower()=="jah" and sai.lower()=="jah":
#        print(f"piima ja saia eest peate maksma: {piimahind+saiahind} euro")
#    if piim.lower()=="jah" and leib.lower()=="jah":
#        print(f"piima ja leiba eest peate maksma: {piimahind+leibahind} euro")
#    if sai.lower()=="jah" and leib.lower()=="jah":
#        print(f"saia ja leiba eest peate maksma: {saiahind+leibahind} euro")
#    if piim.lower()=="ei" and sai.lower()=="ei" and leib.lower()=="ei":
#        print("ostke midagi!")
#except:
#    print("Vale andmetüüp")

# harjutus 9

#try:
#    while True:
#        külg=int(input("Palju külge on kehas? "))
#        if külg == 4:
#            print(f"{külg} - tegemist on ruuduga või ristkülik")
#            a=float(input("Kui suur on esimene külg? "))
#            b=float(input("Kui suur on teine külg? "))
#        if a==b:
#            print("Tegemist on ruuduga ")
#            break
#        else:
#            print(f"{külg} küljega - pole ruut ega ristkülik")
#except:
#    print("Vale andmetüüp")

# harjutus 10
#try:
#    while True:
#        a=float(input("Anna esimene arv "))
#        b=float(input("Anna teine arv "))
#        c=str(input("Mis tehet soovid? + - * / "))
#        way = c
#        if way == "+":
#            print((a+b))
#            break
#        elif way == "-":
#            print((a-b))
#            break
#        elif way == "*":
#            print((a*b))
#            break
#        elif way == "/":
#            print(a/b)
#            break
#except:
#    print("Vale andmetüüp")

# harjutus 11
#try:
#    while True:
#        vanus=int(input("Kui vana sa oled? "))
#        if vanus%5 ==0:
#            print("Sul on juubel")
#            break
#        elif vanus<0:
#            print("Küsin uuesti, kui vana sa oled? ")
#        else:
#            print("Sul pole juubelit")
            
#except:
#    print("Vale andmetüüp")

# harjutus 12
#try:
#    toode=0
#    while toode<=10:
#        toode=float(input("Palju maksab toode? "))
#        if toode<=0:
#            print("toode on tasuta")
#            break
#        elif toode<=10:
#            toodesoodushind=round(toode*0.9,2)
#            print(f"toode maksab allhinnaga {toodesoodushind} ")
#            break
#        elif toode>10:
#            toodesoodushind=round(toode*0.8,2)
#            print(f"toode maksab allhinnaga {toodesoodushind} ")
#            break
#        else:
#            print("palju maksab toode?")
#except:
#    print("Vale andmetüüp")

# harjutus 13
#try:
#    while True:
#        vanus=int(input("Kui vana sa oled? "))
#        sugu=(input("Mis on sinu sugu? mees või naine? "))
#        if vanus<=18 and vanus>=16 and sugu.lower()=="mees":
#            print("sulle on lubatud meie liituda")
#            break
#        elif vanus<16 and vanus>18 and sugu.lower()=="mees":
#            print("te ei saa meiega liituda")
#            break
#        elif sugu.lower()=="naine":
#            print("te ei saa meiega liituda")
#            break
#        else:
#            print("te ei saa meiega liituda")
#except:
#    print("Vale andmetüüp")