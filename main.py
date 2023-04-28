import argparse
import util
import os
import random
from commands import *

#Fungsi len
def Length (object) -> int :
    count = 0
    for i in object :
        count += 1
    return count    

# Fungsi Absolut
def Abs (a,b):
    c = a - b
    if c < 0 :
        c * -1
    return c



while True:
    masukkan = input(">>> ")
    if (masukkan == "login"):
        login()
    elif (masukkan == "logout"):
        logout()
    elif (masukkan == "summonjin"):
        main_summonjin(users)
        print(users)
    elif (masukkan == "hapusjin"):
        hilangkanJin(users, candi)
        print(users)
        print(candi)
    elif (masukkan == "ubahjin"):
        ubah()
    elif (masukkan == "bangun"):
        bangun(candi)
        print(bahan)
        print(candi)
    elif (masukkan == "bahan"):
        print (bahan)
    elif (masukkan == "batchkumpul"):
        batchkumpul()
        print(bahan)
    elif (masukkan == "batchbangun"):
        batchbangun()
        print(bahan)
    elif (masukkan == "ayamberkokok"):
        ayamberkokok()
    elif(masukkan== "laporancandi"):
        laporancandi()
    elif (masukkan == "hancurkancandi"):
        hancurkan_candi()
        print(candi)
    elif (masukkan =="save"):
        save()
    elif (masukkan == "laporanjin"):
        laporanjin()
    elif (masukkan == "laporancandi"):
        laporancandi()
    elif (masukkan == "status"):
        print (currentusers)
    elif (masukkan == "help"):
        help()
    elif (masukkan == "exit"):
        exit()
        break
    else :
        break


#print(candi)