from random import shuffle #öll importinn sem ég þarf
import random
import signal, time   
import sys

loop = "1" #gefið koða fyrir 

while loop == "1": #Loopan ef loopið verður 1 þá spilast leikurinn
    spilastokkur = [] #list nafnið af spilastokknum

    with open('stokkur.txt','r',encoding='iso-8859-1') as stokkur: #þegar það er að lesa txt file-ið stokkur 
        for line in stokkur: #hvernig er verið að lesa hvern lista inn í lista á txt file-inu og svo sett listann í spilastokkinn
            spilastokkur.append(eval(line)) 

    shuffle(spilastokkur)        # stokkar spilinn


    spilamadur = spilastokkur[0:3] #skipt stokknum helming og helming
    tolvan = spilastokkur[3:6]
    stadap = 3
    stadat = 3

    while (spilamadur !=0 or tolvan != 0): #ef tolvan eða spilamaður er ekki með 0 þá heldur leikurinn áfram að spilast
        vinningsbunki = [] #bunkinn ef það skyldi koma jafntefli

        #þegar spilamaðurinn á leik og ef annað þeirra er ekki með spil til að spila þá kemur útkomann af vinningshafa
        if not spilamadur: #Ef spilamaðurinn er ekki með neitt inn í lista þá prentar þetta út
            print("Þvi miður kláraðiru spilinn")
            print("Tölvan vann leikinn!")
            break
        if not tolvan: #Ef tölvan er ekki með neitt in í lista þá prentar þetta út
            print("Tölvan kláraði öll spilinn!")
            print("Þú vannst leikinn, til hamingju!")
            break
        
        '''
        print("+++++++++++++++++++")
        print(spilamadur)
        print("+++++++++++++++++++")
        print(tolvan)                     #Til þess að sjá hver heldur á hvaða spil einnig hvaða spil eru haldinn í jafnteflis búnkann
        print("+++++++++++++++++++")      #Mátt kveikja á þvi en þetta er bara auka
        print(vinningsbunki)
        print("+++++++++++++++++++")
        '''
        print("")
        print("")
        print ("Þú dróst!")
        print ("Veldu flokk") #Hérna er valmöguleikarnir þegar spilarinn á að velja flokk
        print ("|| Nafn  = ",spilamadur[0][0])
        print ("|1| Þyngd í kílóum  = ",spilamadur[0][1])
        print ("|2| Mjólkurlagni dætra  = ",spilamadur[0][2])
        print ("|3| Einkunn ullar  = ",spilamadur[0][3])
        print ("|4| Fjöldi afkvæma  = ",spilamadur[0][4])
        print ("|5| Einkunn læris  = ",spilamadur[0][5])
        print ("|6| Frjósemi  = ",spilamadur[0][6])
        print ("|7| Gerð / Þykkt bakvöðva  = ",spilamadur[0][7])
        print ("|8| Einkun fyrir malir  = ",spilamadur[0][8])
        
        val = int(input("Sláðu inn töluna sem þér langar velja?: "))# hér er valið flokk
        
        
        vinningsbunki.append(spilamadur[0])#Bæði spilinn sem verður spilað með verður settur í vinningsbunkann 
        vinningsbunki.append(tolvan[0])
        
        
        print("")
        print("--------------------------") #Þetta er bara útkoma þannig þú sérð þitt og tölvunar
        print("Þín útkoma er", spilamadur[0][val])
        print("Útkoma tölvunnar er", tolvan[0][val])
        print("--------------------------")
        print("")
        
        if spilamadur[0][val] > tolvan[0][val]: #ef spilamaðurinn er með meira en tölvan þá kemur þetta út
            print("Þú vannst, til hamingju!")
            for x in vinningsbunki: #hann vinnur og fær lista eftir lista inn í listann sinn með append
                spilamadur.append(x)
            del vinningsbunki[:] #þegar hann er búinn að vinna hreinsast bunkinn
            stadap = stadap + 1
            stadat = stadat - 1
                
        elif spilamadur[0][val] < tolvan[0][val]: #ef tolvan er með meira en spilamaðurinn þá kemur þetta út
            print("Tölvann vann, Því miður!")
            for x in vinningsbunki: #hann vinnur og fær lista eftir lista inn í listann sinn með append
                tolvan.append(x)
            del vinningsbunki[:]#þegar hann er búinn að vinna hreinsast bunkinn
            stadap = stadap - 1
            stadat = stadat + 1
                
        elif spilamadur[0][val] == tolvan[0][val]: #ef það er jafntefli þá prentast þetta bara út en við gerum ekkert með bunkann þvi allt er enn geymt inn í því sem var spilað með
            print("Jafntefli, stokkurinn geymdur")
            stadap = stadap - 1
            stadat = stadat - 1
        print("----------SPILA STAÐAN----------")
        print("Þú ert með :", stadap, " spil eftir")
        print("Tölvan er með :", stadat, " spil eftir")
        print("--------------------------------")
        print("")

        spilamadur.remove(spilamadur[0]) #svo er tekið spilinn sem voru notuð úr efsta bunkanum remove-aðar svo þær myndu ekki spilast endalaust aftur og aftur
        tolvan.remove(tolvan[0])


        '''
        print("+++++++++++++++++++")
        print(spilamadur)
        print("+++++++++++++++++++")
        print(tolvan)                     #Til þess að sjá hver heldur á hvaða spil einnig hvaða spil eru haldinn í jafnteflis búnkann
        print("+++++++++++++++++++")      #Mátt kveikja á þvi en þetta er bara auka
        print(vinningsbunki)
        print("+++++++++++++++++++")
        '''
        
        
        if not spilamadur: #hér er gáð aftur hvort þegar talvan á að gera hvort leikari er búinn að klára búnkann
            print("Þvi miður kláraðiru spilinn")
            print("Tölvan vann leikinn!")
            break
        if not tolvan: #þetta er alveg það sama command og fyrir commandið efst upp í leiknum
            print("Tölvan kláraði öll spilinn!")
            print("Þú vannst leikinn, til hamingju!")
            break

        
        tolvaturn = random.randint(1, 8) #hér er automatískt tölvan að velja flokk sem verður spilað með í næstu spili
        time.sleep(3)# hér er gefið smá pása svo það er hægt að lesa hver vann siðasta spil
            
        print()
        print("Tölvan á leik")
        print("Tölvan hugsar", end="")
        text = ( "......")
        for char in text:
             #þetta er svona auka sem mér langaði gera
            sys.stdout.flush() #Command sem lætur eins og tölvan sé að hugsa en það er bara smá pása með time.sleep
            print (char, end="") #fyrir hverja sekondu þá printast út punktar eins og tölvan sé að hugsa
            time.sleep(1) 
        print ("\nTölvan valdi ", tolvaturn)#hér er sagt hvaða númer tölvan valdi
        vinningsbunki.append(spilamadur[0]) #spilinn verða svo sett í vinningsbunkann
        vinningsbunki.append(tolvan[0])
        
        
        print("")
        print("--------------------------") #Þetta er bara útkoma þannig þú sérð þitt og tölvunar
        print("Þín útkoma er", spilamadur[0][val])
        print("Útkoma tölvunnar er", tolvan[0][val])
        print("--------------------------")
        print("")

        if spilamadur[0][val] > tolvan[0][val]: #ef spilamaðurinn er með meira en tölvan þá kemur þetta út
            print("Þú vannst, til hamingju!")
            for x in vinningsbunki: #hann vinnur og fær lista eftir lista inn í listann sinn með append
                spilamadur.append(x)
            del vinningsbunki[:] #þegar hann er búinn að vinna hreinsast bunkinn
            stadap = stadap + 1
            stadat = stadat - 1
                
        elif spilamadur[0][val] < tolvan[0][val]: #ef tolvan er með meira en spilamaðurinn þá kemur þetta út
            print("Tölvann vann, Því miður!")
            for x in vinningsbunki: #hann vinnur og fær lista eftir lista inn í listann sinn með append
                tolvan.append(x)
            del vinningsbunki[:]#þegar hann er búinn að vinna hreinsast bunkinn
            stadap = stadap - 1
            stadat = stadat + 1
                
        elif spilamadur[0][val] == tolvan[0][val]: #ef það er jafntefli þá prentast þetta bara út en við gerum ekkert með bunkann þvi allt er enn geymt inn í því sem var spilað með
            print("Jafntefli, stokkurinn geymdur")
            stadap = stadap - 1
            stadat = stadat - 1
        print("----------SPILA STAÐAN----------")
        print("Þú ert með :", stadap, " spil eftir")
        print("Tölvan er með :", stadat, " spil eftir")
        print("--------------------------------")
        print("")

        spilamadur.remove(spilamadur[0]) #hér er efsti bunkurinn í stokknum þeirra remove-að aftur
        tolvan.remove(tolvan[0])

        '''
        print("+++++++++++++++++++")
        print(spilamadur)
        print("+++++++++++++++++++")
        print(tolvan)                     #Til þess að sjá hver heldur á hvaða spil einnig hvaða spil eru haldinn í jafnteflis búnkann
        print("+++++++++++++++++++")      #Mátt kveikja á þvi en þetta er bara auka
        print(vinningsbunki)
        print("+++++++++++++++++++")
        '''

    # eins og þú sérð þá er þetta ekki inn í leikja loopuna, þegar vinningshafi er
    #fundinn þá er alltaf "BREAK" í endanum sem leiðir beint inn í þetta    
    print("Langar þer að spila aftur?")
    
    spurning = input("y/n: ")#spurt hvort þú viljir spila aftur eða ekki
    if spurning == "y":
        loop = "1" #hér verður spilað aftur ef það er sagt "y"
    elif spurning == "n":
        loop = "2" #hér verður hætt að spila ef það verður sagt "n"
        print ("Takk fyrir að prófa leikinn")
        exit() #command sem exitar beint út úr forritinu, þú mátt closea forritið eða cancel-a
            
        
        
        

