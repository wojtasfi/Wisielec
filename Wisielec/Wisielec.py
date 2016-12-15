from random import randint
slowa =['kwiatek', 'tartak', 'drzewo','mapa','pies', 'kot', 'sweter','myszka', 'lizak']
rand_number = randint(0,len(slowa)-1)
slowo = slowa[rand_number]
proby = 5
litery =[]
odgadniete_litery=0

dl_slowa = len(slowo)

if dl_slowa ==1:
    odmiana ="znak"
elif dl_slowa >=2 and dl_slowa < 5:
    odmiana ="znaki"
elif dl_slowa >=5:
    odmiana ="znaków"
    
print("Witamy w grze Wisielec.")
print("Słowo zostało wylosowane. Posiada ono %d %s.\n"
"%s\nMożesz pomylić się %d razy." % (dl_slowa,odmiana,"_ " * len(slowo),proby))


while proby >0 and odgadniete_litery < len(slowo):
    zgadles=""

    pytaj = "tak"
    
    
    while pytaj == "tak":
        litera = input("Zgadnij literkę (prób %s):" % str(proby))
        
        if litera in litery:
            print("Już zgadłeś/aś tą literę.")
            continue
        
        if litera.isalpha():
            pytaj = "nie"
        
    litery.append(litera)
    
    
    for znak in slowo:
        if znak == litera:
            odgadniete_litery +=1
            zgadles =1
    
    if zgadles ==1:
        print("Odgadłeś kolejną literę. Łącznie: %d." % odgadniete_litery)
    else:
        print("Nie odgadłeś literki.")
    
    #drukowanie odgadniętych liter
    print()
    for znak in slowo:
        if znak in litery:
            print(znak + " ",end="")
        else:
            print("_ ",end="")
    print()
    
    
    print()
    
    
    if zgadles != 1:
        proby -= 1
    
if proby == 0:
    print("Przegrałeś :( Wyslosowane słowo to '%s'." % slowo)
else:
    print("Wygrałeś!!!")