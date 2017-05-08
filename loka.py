#Höfundar Ágúst Örn Eiðsson og Alexander Smári Erlingsson
from random import *
import time
vann=True
winnerspil=[]
listicom=[]
listiplay=[]
teljari1=51
with open("hrutar.txt") as hrutar:
    listinn = [lidur for linan in hrutar.readlines() for lidur in linan.split(";")]
teljarinn=0
fjoldi=int(input("Hvað eru margir að fara að spila?? "))
fjoldispila=52/fjoldi
jafnteflispil=[]
gig=[]
if fjoldi==1:
    for x in range(26):
        com = randint(0, teljari1)
        teljari1 -= 1
        play = randint(0, teljari1)
        teljari1 -= 1
        listicom.append(listinn[com])
        listiplay.append(listinn[play])
    print("-----Þá byrjar þetta-----")
    while len(listicom)!=0 and len(listiplay)!=0:
        kindplay=[]
        kindcom=[]
        kindplay=str(listiplay[0])
        kindplay=kindplay.split(",")
        del listiplay[0]
        kindcom = str(listicom[0])
        kindcom = kindcom.split(",")
        del listicom[0]
        print("---Kindin þín---")
        print("Kindin heitir",kindplay[0])
        print("Kindin þín er", kindplay[1],"kíló - 1")
        print("Kindin þín er með", kindplay[2], "í mjólurlagni dætra - 2")
        print("Kindin þín er með", kindplay[3],"í ullar einkunn - 3")
        print("Kindin á", kindplay[4],"afkvæmi - 4")
        print("Kindin þín er með", kindplay[5],"í einkunn læris - 5")
        print("Kindin þín er með", kindplay[6],"í frjósemi - 6")
        print("Kindin þín er með", kindplay[7],"í gerð/þykt bakvöðva - 7")
        print("Kindin þín er með", kindplay[8],"í einkun fyrir malir - 8")
        if vann==True:
            svar=int(input("Frá 1-8 hvað viltu nota "))
        if svar>0 and svar<9:
            time.sleep(1)
            if float(kindplay[svar])>float(kindcom[svar]):
                print("Þú vannst með",kindplay[svar],"stig á meðan talvan var með",kindcom[svar])
                vann=True
                olli=False
            elif float(kindplay[svar])<float(kindcom[svar]):
                print("Talvan vann með",kindcom[svar],"stig á meðan þú varst með",kindplay[svar])
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
teljari5=1
if fjoldi==2:
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
        if vann==True:
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
        if vann==False:
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