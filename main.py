import argparse
import util
import os
import random
from commands import *

# Fungsi Bantuan
# Fungsi len
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

# Algoritma Program Utama secara Keseluruhan (MAIN)
while True:
    masukkan = input(">>> ")
    if (masukkan == "login"):
        login()
    elif (masukkan == "logout"):
        logout()
    elif (masukkan == "summonjin"):
        if currentusers[0] == -1: # User tidak melakukan login
            print("Anda terdeteksi tidak login, lakukan login terlebih dahulu sebelum melakukan summon jin")
        else: # Terdapat ketentuan jin tidak boleh melebihi 100
            if (Length(users) - 2) >= 100:
                print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
            else:
                main_summonjin(users)
    elif (masukkan == "hapusjin"):
        if currentusers[0] == -1: # User tidak melakukan login
            print("Anda terdeteksi tidak login, lakukan login terlebih dahulu sebelum melakukan menghapus jin")
        else:
            hilangkanJin(users,candi)
    elif (masukkan == "ubahjin"):
        if currentusers[0] == -1: # User tidak melakukan login
            print("Anda terdeteksi tidak login, lakukan login terlebih dahulu sebelum melakukan mengubah jin")
        else:
            ubah()
    elif (masukkan == "bangun"):
        if currentusers[0] == -1: # User tidak melakukan login
            print("Anda terdeteksi tidak login, lakukan login terlebih dahulu sebelum melakukan pembangunan candi")
        else:
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
    elif (masukkan == "laporanjin"):
        laporanjin()
    elif (masukkan == "laporancandi"):
        laporancandi()
    elif (masukkan == "hancurkancandi"):
        hancurkan_candi()
        print(candi)
    elif (masukkan == "ayamberkokok"):
        ayamberkokok()
    elif (masukkan =="save"):
        save()
    elif (masukkan == "status"):
        print (currentusers)
    else :
        break
