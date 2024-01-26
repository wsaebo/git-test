#Dette programmet skal sjekke hvilken dato som kommer først
print("Skriv inn første dato som et heltall\n")
dag1=int(input())
print("Skriv inn første måned som et heltall \n")
mnd1=int(input())
print("Skriv inn andre dato som et heltal \n")
dag2=int(input())
print("Skriv inn andre måned som et heltall \n")
mnd2=int(input())

if (dag1==dag2&mnd1==mnd2): #Sjekker om dato er samme 
    print("Samme dato") 
    
elif (dag1<=dag2&mnd1<=mnd2): #Sjekker om dag 1 og mnd 1 kommer først 
    print ("Riktig rekkefølge") 
elif (dag1>=dag2&mnd1>=mnd2): #Sjekker om dag 2 og mnd 2 kommer først 
    print("Feil rekkefølge")





