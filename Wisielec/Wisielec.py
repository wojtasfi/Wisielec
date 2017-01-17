from random import randint
slowa =['flower', 'wood', 'town','map','dog', 'cat', 'sweater','mouse', 'lolipop']
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
    
print("Wisielec.")
print("The word has been chosen. It has %d %s.\n"
"%s\nAllowed mistakes: %d." % (dl_slowa,odmiana,"_ " * len(slowo),proby))


while proby >0 and odgadniete_litery < len(slowo):
    zgadles=""

    pytaj = "tak"
    
    
    while pytaj == "tak":
        litera = input("Guess the letter (%s):" % str(proby))
        
        if litera in litery:
            print("You have alresy guessed thie letter")
            continue
        
        if litera.isalpha():
            pytaj = "nie"
        
    litery.append(litera)
    
    
    for znak in slowo:
        if znak == litera:
            odgadniete_litery +=1
            zgadles =1
    
    if zgadles ==1:
        print("You guessed this letter. Summary: %d." % odgadniete_litery)
    else:
        print("Sorry you did not guess the letter.")
    
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
    print("You lost :( The word is: '%s'." % slowo)
else:
    print("You won!!!")