#Höfundar Ágúst Örn Eiðsson og Alexander Smári Erlingsson
from random import *#importa random til að gera margt og mikið
import time #Importa time til að hægja á spilinu til að geta lesið smá hver vin
vann=True#set vann á True til að sjá hver á að gera
#Bý til lista
winnerspil=[]
listicom=[]
listiplay=[]
jafnteflispil=[]
gig=[]
kindplay=[]
kindcom=[]
teljari1=51
with open("hrutar.txt") as hrutar:#opna txt fileið svo ég fái spilin
    listinn = [lidur for linan in hrutar.readlines() for lidur in linan.split(";")]#set spilin í lista með því að splitta á ;
teljarinn=0#bý til teljara
fjoldi=int(input("Hvað eru margir að fara að spila?? "))#spyr hve margir eru að fara að spila
if fjoldi==1:#ef það er einn að fara að spila
    for x in range(26):#deili spilunum á leikmenn með random
        com = randint(0, teljari1)
        teljari1 -= 1
        play = randint(0, teljari1)
        teljari1 -= 1
        listicom.append(listinn[com])
        listiplay.append(listinn[play])
    print("-----Þá byrjar þetta-----")
    while len(listicom)!=0 and len(listiplay)!=0:#hættir að keyra þegar einn listinn er tómur
        kindplay=str(listiplay[0])#tek og set upp eitt spil
        kindplay=kindplay.split(",")
        del listiplay[0]#eyði því svo útúr listanum
        kindcom = str(listicom[0])
        kindcom = kindcom.split(",")
        del listicom[0]
        print("---Kindin þín---")#birti upplýsingarnar um kindina
        print("Kindin heitir",kindplay[0])
        print("Kindin þín er", kindplay[1],"kíló - 1")
        print("Kindin þín er með", kindplay[2], "í mjólurlagni dætra - 2")
        print("Kindin þín er með", kindplay[3],"í ullar einkunn - 3")
        print("Kindin á", kindplay[4],"afkvæmi - 4")
        print("Kindin þín er með", kindplay[5],"í einkunn læris - 5")
        print("Kindin þín er með", kindplay[6],"í frjósemi - 6")
        print("Kindin þín er með", kindplay[7],"í gerð/þykt bakvöðva - 7")
        print("Kindin þín er með", kindplay[8],"í einkun fyrir malir - 8")
        if vann==True:#fæ að velja ef ég vann seinast
            svar=int(input("Frá 1-8 hvað viltu nota "))
        elif vann==False:#talvan velur ef hún vann seinast og prenar út hvað hún valdi
            svar=randint(1,8)
            print("Talvan valdi",svar)
        if svar>0 and svar<9:
            time.sleep(1)
            if float(kindplay[svar])>float(kindcom[svar]):#kemur upp ef spilarinn vann
                print("Þú vannst með",kindplay[svar],"stig á meðan talvan var með",kindcom[svar])
                vann=True#læt mig velja næst
                olli=False#það er ekki jafntefli
            elif float(kindplay[svar])<float(kindcom[svar]):#kemur upp ef talvan vann og segir hvað talvan var með og hvað ég var með
                print("Talvan vann með",kindcom[svar],"stig á meðan þú varst með",kindplay[svar])
                vann=False#læt tölvuna velja næst
                olli=False#það er ekki jafntefli
            elif float(kindplay[svar])==float(kindcom[svar]):#kemur ef það var jafntefli
                print("Það var jafntefli")
                #Set spilin í jafnteflis lista
                jafnteflispil.append(kindplay[svar])
                jafnteflispil.append(kindcom[svar])
                #eyði úr hinum listunum
                del kindcom[:]
                del kindplay[:]
                olli=True#það var jafntefli
            if olli==False:
                #set spilin í lista
                winnerspil.append(kindcom)
                winnerspil.append(kindplay)
                del kindcom[:]
                del kindplay[:]
                if vann==True:#ef ég vann fæ ég spil
                    listiplay.append(winnerspil)
                    if len(jafnteflispil)<0:#ef það var jafntefli þá fæ ég spilin
                        listiplay.append(jafnteflispil)
                        del jafnteflispil[:]#eyði úr jafnteflis listanum
                elif vann==False:#talvan fær spilin
                    listicom.append(winnerspil)
                    if len(jafnteflispil)<0:#ef það var jafntefli þá fær talvan spilin
                        listicom.append(jafnteflispil)
                        del jafnteflispil[:]
                else:#ef það kemur einhver villa
                    listicom.append(winnerspil[0])
                    listiplay.append(winnerspil[1])
        else:#ef það var slegin inn ekki tala á bilinu 1-8
            print("Rangur innsláttur")
    #birti hver vann
    if len(listiplay)==0:
        print("Tölvan vann!!!")
    elif len(listicom)==0:
        print("Þú vannst!!!")
teljari5=1
if fjoldi==2:#tveir spilarar
    for x in range(26):
        com = randint(0, teljari1)
        teljari1 -= 1
        play = randint(0, teljari1)
        teljari1 -= 1
        listicom.append(listinn[com])
        listiplay.append(listinn[play])
    print("-----Þá byrjar þetta-----")
    while len(listicom)!=52 and len(listiplay)!=52:
        kindplay=[]
        kindcom=[]
        kindplay=str(listiplay[0])
        kindplay=kindplay.split(",")
        del listiplay[0]
        kindcom = str(listicom[0])
        kindcom = kindcom.split(",")
        del listicom[0]
        if vann==True:#ef spilari eitt vann
            print("Spilari Eitt")
            print("---Kindin þín---")
            print("Kindin heitir", kindplay[0])
            print("Kindin þín er", kindplay[1], "kíló - 1")
            print("Kindin þín er með", kindplay[2], "í mjólurlagni dætra - 2")
            print("Kindin þín er með", kindplay[3], "í ullar einkunn - 3")
            print("Kindin á", kindplay[4], "afkvæmi - 4")
            print("Kindin þín er með", kindplay[5], "í einkunn læris - 5")
            print("Kindin þín er með", kindplay[6], "í frjósemi - 6")
            print("Kindin þín er með", kindplay[7], "í gerð/þykt bakvöðva - 7")
            print("Kindin þín er með", kindplay[8], "í einkun fyrir malir - 8")
            svar=int(input("Frá 1-8 hvað viltu nota "))
        if vann==False:#ef spilari tvö vann
            print("Spilari Tvö")
            print("---Kindin þín---")
            print("Kindin heitir", kindcom[0])
            print("Kindin þín er", kindcom[1], "kíló - 1")
            print("Kindin þín er með", kindcom[2], "í mjólurlagni dætra - 2")
            print("Kindin þín er með", kindcom[3], "í ullar einkunn - 3")
            print("Kindin á", kindcom[4], "afkvæmi - 4")
            print("Kindin þín er með", kindcom[5], "í einkunn læris - 5")
            print("Kindin þín er með", kindcom[6], "í frjósemi - 6")
            print("Kindin þín er með", kindcom[7], "í gerð/þykt bakvöðva - 7")
            print("Kindin þín er með", kindcom[8], "í einkun fyrir malir - 8")
            svar=int(input("Frá 1-8 hvað viltu nota "))
        if svar>0 and svar<9:
            time.sleep(1)
            if float(kindplay[svar])>float(kindcom[svar]):
                print("Spilari eitt vann með",kindplay[svar],"stig á meðan spilari tvö var með",kindcom[svar])
                vann=True
                olli=False
            elif float(kindplay[svar])<float(kindcom[svar]):
                print("Spilari tvö vann með",kindcom[svar],"stig á meðan spilari eitt var með",kindplay[svar])
                vann=False
                olli=False
            elif float(kindplay[svar])==float(kindcom[svar]):
                print("Það var jafntefli")
                jafnteflispil.append(kindplay[svar])
                jafnteflispil.append(kindcom[svar])
                del kindcom[:]
                del kindplay[:]
                olli=True
            if olli==False:
                winnerspil.append(kindcom)
                winnerspil.append(kindplay)
                del kindcom[:]
                del kindplay[:]
                if vann==True:
                    listiplay.append(winnerspil)
                    if len(jafnteflispil)<0:
                        listiplay.append(jafnteflispil)
                        del jafnteflispil[:]
                elif vann==False:
                    listicom.append(winnerspil)
                    if len(jafnteflispil)<0:
                        listicom.append(jafnteflispil)
                        del jafnteflispil[:]
                else:
                    listicom.append(winnerspil[0])
                    listiplay.append(winnerspil[1])
        else:
            print("Rangur innsláttur")
    if len(listiplay)==0:
        print("Spilari Tvö vann!!!")
    elif len(listicom)==0:
        print("Spilari Eitt vann!!!")