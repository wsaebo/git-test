#Dette programmet leser inn og spør en person om man vil ha en brus. 
print ("Vil du ha en brus?" ) #Printer ut spørsmålet vil du ha en brus ? 
brus = input() #Tar i mot input fra brukeren
brus = str.upper(brus) #Konverterer strengen til uppcase slik at om brukeren taster nei, NEI, JA, jA osv så vil det fungere uansett :) 
if (brus=="JA"): #Om brus er lik ja så får du en brus 
    print("Her har du en brus")
elif (brus=="NEI") : #Om brus er lik nei så får du ikke brus og printer ut den er god 
    print ("Den er god")

else: 
    print("Det forstod jeg ikke") #printer ut det forstod jeg ikke om input er noe annet enn ja eller nei. 


