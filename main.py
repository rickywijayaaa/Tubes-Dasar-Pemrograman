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
    menu = input("Menu: ")
    if (menu == "kumpul"):
        kumpul()
    elif (menu == "login"):
        login()
    elif (menu == "logout"):
        logout()
    elif (menu == "ubah"):
        ubah()
    elif (menu == "bahan"):
        print (bahan)
    elif (menu == "status"):
        print (currentusers)
    elif (menu == "batchkumpul"):
        batchkumpul()
        print(bahan)
    elif (menu == "batchbangun"):
        batchbangun()
        print(bahan)
    elif (menu == "bangun"):
        bangun(candi)
        print(bahan)
        print(candi)
    elif (menu == "ayamberkokok"):
        ayamberkokok()
    elif (menu == "summonjin"):
        main_summonjin(users)
        print(users)
    elif (menu == "hapusjin"):
        hilangkanJin(users, candi)
        print(users)
        print(candi)
    elif(menu== "laporancandi"):
        laporancandi()
    else :
        break


#print(candi)