print ("Vil du ha en brus?" )
brus = input()
brus = str.upper(brus) #Konverterer strengen til uppcase slik at om brukeren taster nei, NEI, JA, jA osv så vil det fungere uansett :) 
if (brus=="JA"): 
    print("Her har du en brus")
elif (brus=="NEI") : 
    print ("Ingen brus i dag")

else: 
    print("Det forstod jeg ikke")


