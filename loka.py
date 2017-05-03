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