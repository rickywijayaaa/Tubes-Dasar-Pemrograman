from base import *
import argparse
from util import *
import os
import random


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

currentusers = [-1,-1,-1]
import random


def login():
    if currentusers[0] != -1:
        print("anda sudah login")
        return None
    username = input("Username: ")
    password = input("Password: ")
    for i in range(len(users)):
        if (username == users[i][0]):
            if (password == users[i][1]):
                print("")
                print(f"Selamat datang, {username}!")
                currentusers[0] = users[i][0]
                currentusers[1] = users[i][1]
                currentusers[2] = users[i][2]
                return None
            print("")
            print("Password salah!")
            return None
    print("user tidak ditemukan")
    return None

def logout():
    if currentusers[0] == -1:
        print("anda belum login")
        return None
    currentusers[0] = -1
    currentusers[1] = -1
    currentusers[2] = -1
    print("Log out berhasil, bye!")
    return None

# Fungsi untuk memasukkan username jin
def uname_summonjin(users, jenis_jin):
    # Counter untuk check username sudah ada dalam file csv atau tidak
    check = 0
    # Input pertama username 
    uname = input("\nMasukkan username jin: ")
    # Perulangan untuk cek apakah ada username yang sama dengan username yang diinput user
    for i in range(Length (users)):
        if (users[i][0] == uname):
                check += 1
    # Percabangan apabila terdapat username yang sama
    if check == 0:
        password(users, uname, jenis_jin)
    else: # Rekursif apabila username sama sampai ditemukan username yang tidak sama
        print(f'\nUsername "{uname}" sudah diambil!')
        uname_summonjin(users, jenis_jin)
    return users

# Fungsi untuk memasukkan password jin setelah didapatkan username yang valid
def password(users, uname, jenis_jin):
    newusers =[]
    # Input pertama password
    pw = input("Masukkan password jin: ")
    # Percabangan pemenuhan 5 sampai 25 karakter dalam password
    if Length(pw) < 5 or Length(pw) > 25: # Belum memenuhi syarat karakter
        print("\nPassword panjangnya harus 5-25 karakter!\n")
        password(users, uname, jenis_jin) # Rekurens
    else: # Telah memenuhi syarat karakter
            newusers = [uname,pw,jenis_jin] 
            users.append(newusers)
            print("\nMengumpulkan sesajen...")
            print("Menyerahkan sesajen...")
            print("Membacakan mantra...")
            print(f"\nJin {newusers[0]} berhasil dipanggil!")
    return users

def main_summonjin (users):
    print("Jenis jin yang dapat dipanggil: ")
    print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print(" (2) Pembangun - Bertugas membangun candi")
    
    summon (users)

    return users

def summon (users):
    jenis_jin = int(input("\nMasukkan nomor jenis yang ingin dipanggil: "))

    if (jenis_jin == 1):
        print('\nMemilih jin "Pengumpul".')
        jenis_jin = "jin_pengumpul"
        uname_summonjin(users, jenis_jin)

    elif (jenis_jin == 2):
        print('\nMemilih jin "Pembangun".')
        jenis_jin = "jin_pembangun"
        uname_summonjin(users, jenis_jin)

    else:
        print(f'\nTidak ada jenis jin bernomor “{jenis_jin}”!')
        summon (users)
    return users

def ubah ():
    if currentusers[2] != "bandung_bondowoso":
        print("Hanya dapat diakses oleh bandung bondowoso")
        return None
    username= input("Masukkan username jin : ")
    idx = 0
    for i in range (Length(users)) :
        if (username == users[i][0]):
            idx = 1
            if (users[i][2]== "jin_pengumpul"):
                print("")
                print ("Jin ini bertipe 'Pengumpul'. Yakin ingin mengubah ke tipe 'Pembangun' (Y/N)?" )
                persetujuan = input()
                if (persetujuan == "Y"):
                    users[i][2] = "jin_pembangun"
                    print("Jin telah berhasil diubah.")
                    break
                elif (persetujuan =="N"):
                    print("Jin tidak jadi diubah")
                    break
                else :
                    print("input invalid (Y/N)")  
                    break              
            elif (users[i][2]== "jin_pembangun"):
                print("")
                print ("Jin ini bertipe 'Pembangun'. Yakin ingin mengubah ke tipe 'pengumpul' (Y/N)?" )
                persetujuan = input()
                if (persetujuan == "Y"):
                    users[i][2] = "jin_pengumpul"
                    print("Jin telah berhasil diubah.")
                    break
                elif (persetujuan =="N"):
                    print ( "Jin tidak jadi diubah")
                    break
                else :
                    print("input invalid (Y/N)")
                    break
            else:
                print("id terdaftar namun bukan jin pengumpul maupun pembangun")
    if (idx == 0): # Jika username jin tidak tersedia
        print("Tidak ada jin dengan username tersebut.")


def hilangkanJin (users, candi):
    if currentusers[2] != "bandung_bondowoso":
        print("Hanya dapat diakses oleh bandung bondowoso")
        return None    
    check = 0
    uname = input("Masukkan username jin : ")
    for i in range(Length(users)):
        if (users[i][0] == uname):
                check += 1
    if check != 0:
            yn_hilangkanjin(uname, candi, users)
    else: # check == 0 
        print('\nTidak ada jin dengan username tersebut.')
       # KEMBALI KE COMMAND
    return users

def yn_hilangkanjin (uname, candi, users):
    check_yn = input(f"Apakah anda yakin ingin menghapus jin dengan username {uname} (Y/N)? ")
    if (check_yn == "Y"):
        for i in range (Length(candi)): # Candi tetap terhitung 100 
            if candi[i][1] == uname: 
                candi[i]= None
            else:
                continue
        for i in range (Length(users)):
            if users[i][0] == uname:
                users[i] = None
            else:
                continue
        print("\nJin telah berhasil dihapus dari alam gaib.")
    elif (check_yn == "N"): # Kreativitas 1
        print("\nPenghapusan jin akan dibatalkan. Kamu akan dikembalikan ke pemilihan daftar command.")
        # KEMBALI KE COMMAND     
    else: # Kreativitas 2
        print('Masukkan tidak sesuai dengan pilihan. Silakan masukkan kembali dengan pilihan masukkan "Y" atau "N"!')
        yn_hilangkanjin(uname, candi, users)

candi_sisa = [100]
def bangun(candi):
    if currentusers[0] == "bondowoso" or currentusers[0] == "roro" or currentusers[2] != "jin_pembangun":
        print("hanya jin pembangun yang dapat membangun")
        return None

    for i in range (3):
        if (bahan[i][0] == "pasir"):
            pasir = bahan[i][2]
        elif (bahan[i][0] == "batu"):
            batu = bahan[i][2]
        elif (bahan[i][0] == "air"):
            air = bahan[i][2]
    pasir_c = random.randint(1, 5)
    batu_c = random.randint(1, 5)
    air_c = random.randint(1, 5)
     
    if pasir_c > pasir and batu_c > batu and air_c > air:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
    else:
        for d in range (1,101): 
            ada = 0
            for i in (candi):
                if d == i[0]:
                    ada = 1
                    break
            if ada == 0:
                newcandi = [d, currentusers[0], pasir_c, batu_c, air_c]
                my_append(candi,newcandi) 
                candi_sisa[0] -= 1
                print("Candi berhasil dibangun.")
                print(f"Sisa candi yang perlu dibangun: {candi_sisa[0]}")
                

                for i in range(Length(bahan)):
                        if (bahan[i][0] == "pasir"):
                            bahan[i][2] -= pasir_c
                        elif (bahan[i][0] == "batu"):
                            bahan[i][2] -= batu_c
                        elif (bahan[i][0] == "air"):
                            bahan[i][2] -= air_c
                return None

def kumpul ():
    if currentusers[0] == "bondowoso" or currentusers[0] == "roro" or currentusers[2] != "jin_pengumpul":
        print("hanya jin pengumpul yang dapat melakukan")
        return None
    pasir = random.randint (0,5)
    batu = random.randint (0,5)
    air = random.randint (0,5)
    print ("Jin menemukan :",pasir,"pasir,", batu,"batu,", air,"air")
    for i in range(len(bahan)):
        if (bahan[i][0] == "pasir"):
            bahan[i][2] += pasir
        elif (bahan[i][0] == "batu"):
            bahan[i][2] += batu
        elif (bahan[i][0] == "air"):
            bahan[i][2] += air
    return None

def batchkumpul():
    if currentusers[2] != "bandung_bondowoso":
        print("Hanya dapat diakses oleh bandung bondowoso")
        return None
    total_jin = 0
    for i in range (Length(users)):
        if users[i][2] == "jin_pengumpul":
            total_jin += 1
    
    if total_jin == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:
        sum_pasir = 0
        sum_batu = 0
        sum_air = 0
        for i in range (total_jin) :
            pasir = random.randint (0,5)
            batu = random.randint (0,5)
            air = random.randint (0,5)
            sum_pasir += pasir
            sum_batu += batu
            sum_air += air
        print(f"Mengerahkan {total_jin} jin untuk mengumpulkan bahan.")
        print(f"Jin menemukan total {sum_pasir} pasir, {sum_batu} batu, dan {sum_air} air.")
        for i in range(Length(bahan)):
            if (bahan[i][0] == "pasir"):
                bahan[i][2] += sum_pasir
            elif (bahan[i][0] == "batu"):
                bahan[i][2] += sum_batu
            elif (bahan[i][0] == "air"):
                bahan[i][2] += sum_air
        return None
def laporanjin ():
    if currentusers[2] != "bandung_bondowoso":
        print("Laporan jin hanya dapat diakses oleh bandung bondowoso")
        return None
    total_jin = 0
    total_jin_pengumpul = 0
    total_jin_pembangun = 0
    sisa_pasir = int(bahan[0][2])
    sisa_air = int(bahan[1][2])
    sisa_batu = int(bahan[2][2])
    for i in range(Length(users)):
        if users[i][2] == "jin_pembangun":
            total_jin += 1
            total_jin_pembangun += 1
        elif users[i][2] == "jin_pengumpul":
            total_jin += 1
            total_jin_pengumpul += 1
        else:
            total_jin += 0
    jin_pembangun = []
    for i in range(Length(candi)):
        jin_pembangun.append(candi[i][1])
    sort_by_frequency(jin_pembangun)
    jin_terajin = jin_pembangun[0]
    jin_termalas = jin_pembangun[Length(jin_pembangun)-1]
    print("Total Jin: ", total_jin)
    print("Total Jin Pengumpul: ", total_jin_pengumpul)
    print("Total Jin Pembangun: ", total_jin_pembangun)
    if total_jin_pembangun == 0 :
        print("Jin Terajin: - ")
        print("Jin Termalas: - ")
    else:
        print("Jin Terajin: ", jin_terajin)
        print("Jin Termalas: ", jin_termalas)
    print(f"Jumlah Pasir: {sisa_pasir} unit")
    print(f"Jumlah Air: {sisa_air} unit")
    print(f"Jumlah Batu: {sisa_batu} unit")

def laporancandi():
    if currentusers[2] != "bandung_bondowoso":
        print("Laporan candi hanya dapat diakses oleh bandung bondowoso")
        return None
    total_candi = Length(candi)
    total_pasir = 0
    total_batu = 0
    total_air = 0
    harga_candi = [0 for i in range(Length(candi))]
    max_harga = harga_candi[0]
    min_harga = harga_candi[0]
    idx_max = 0
    idx_min = 0
    for i in range(Length(candi)):
        total_pasir += int(candi[i][2])
        total_batu += int(candi[i][3])
        total_air += int(candi[i][4])
    for i in range(Length(candi)):
            harga_candi[i] = 10000*int(candi[i][2]) + 15000*int(candi[i][3]) + 7500*int(candi[i][4])
    for i in range(Length(candi)):
        if harga_candi[i] >= max_harga:
            max_harga = harga_candi[i]
            idx_max = i + 1
        if i == 0:
            min_harga = harga_candi[i]
            idx_min = i + 1
        else:
            if harga_candi[i] <= min_harga:
                min_harga = harga_candi[i]
                idx_min = i + 1
    rupiah_max = format_rupiah(max_harga)
    rupiah_min = format_rupiah(min_harga)
    print("Total Candi: ", total_candi)
    if total_candi == 0:
        print("Total Pasir yang digunakan : 0 ")
        print("Total Batu yang digunakan : 0 ")
        print("Total Air yang digunakan : 0 ")
        print("ID Candi Termahal: - ")
        print("ID Candi Termurah: - ")
    else:
        print("Total Pasir yang digunakan: ", total_pasir )
        print("Total Batu yang digunakan: ", total_batu)
        print("Total Air yang digunakan: ", total_air)
        print(f"ID Candi Termahal: {idx_max} ({rupiah_max}) ")
        print(f"ID Candi Termurah: {idx_min} ({rupiah_min}) ")

def batchbangun():
    if currentusers[2] != "bandung_bondowoso":
        print("Hanya dapat diakses oleh bandung bondowoso")
        return None
    total_jin = 0
    for i in range (Length(users)):
        if users[i][2] == "jin_pembangun":
            total_jin += 1
    
    if total_jin == 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:
        sum_pasir = 0
        sum_batu = 0
        sum_air = 0
        kurang_pasir = 0
        kurang_batu= 0
        kurang_air=0
        for i in range (total_jin):
            pasir = random.randint (1,5)
            batu = random.randint (1,5)
            air = random.randint (1,5)
            sum_pasir += pasir
            sum_batu += batu
            sum_air += air
        if sum_pasir > bahan [0][2] or sum_batu > bahan[1][2] or sum_air > bahan[2][2]:
            kurang_pasir = Abs(sum_pasir,bahan[0][2])
            kurang_batu = Abs(sum_batu,bahan[1][2])
            kurang_air = Abs(sum_air,bahan[2][2])
            print (f"Bangun gagal. kurang {kurang_pasir} pasir, {kurang_batu} batu, dan {kurang_air} air.")
        else:
            bahan[0][2] -= sum_pasir
            bahan[1][2] -= sum_batu
            bahan[2][2] -= sum_air

            print(f"Mengerahkan {total_jin} jin untuk membangun candi dengan total bahan {sum_pasir} pasir, {sum_batu} batu, {sum_air}, air.")
            print(f"Jin berhasil membangun total {total_jin} candi") 



# def laporanjin ():
#     if currentusers[2] != "bandung_bondowoso":
#         print("Laporan jin hanya dapat diakses oleh bandung bondowoso")
#         return None
#     total_jin = 0
#     total_jin_pengumpul = 0
#     total_jin_pembangun = 0
#     sisa_pasir = int(bahan[1][2])
#     sisa_air = int(bahan[2][2])
#     sisa_batu = int(bahan[3][2])
#     for i in range(Length(users)):
#         if users[i][2] == "jin_pembangun":
#             total_jin += 1
#             total_jin_pembangun += 1
#         elif users[i][2] == "jin_pengumpul":
#             total_jin += 1
#             total_jin_pengumpul += 1
#         else:
#             total_jin += 0
#     list_jin_pembangun_candi = []
#     for i in range(Length(candi)):
#         jin = candi[i][1]
#         appendArr(list_jin_pembangun_candi, jin)
#     list_jin_terurut = sort_by_frequency(list_jin_pembangun_candi)
#     nama_jin_terurut = []
#     for i in range(Length(list_jin_terurut)-1):
#         if list_jin_terurut[i] != list_jin_terurut[i+1]:
#             appendArr(nama_jin_terurut, list_jin_terurut[i])
#     appendArr(nama_jin_terurut, list_jin_terurut[Length(list_jin_terurut)-1])
#     freq_found = countFrequency(nama_jin_terurut, list_jin_terurut )
#     jin_terajin = list_jin_terurut[0]
#     jin_termalas = list_jin_terurut[Length(list_jin_terurut)]
#     for i in range(Length(freq_found)-1):
#         if freq_found[i] == freq_found[i+1]:
#             if nama_jin_terurut[i] <= nama_jin_terurut[i+1]:
#                 jin_terajin = nama_jin_terurut[i]
#             else:
#                 jin_terajin = nama_jin_terurut[i+1]
#         else:
#             break
#     for i in range(len(freq_found)-1, 0, -1):
#         if freq_found[i] == freq_found[i-1]:
#             if nama_jin_terurut[i] >= nama_jin_terurut[i-1]:
#                 jin_termalas = nama_jin_terurut[i]
#             else:
#                 jin_termalas = nama_jin_terurut[i-1]
#         else:
#             break      
#     print("Total Jin: ", total_jin)
#     print("Total Jin Pengumpul: ", total_jin_pengumpul)
#     print("Total Jin Pembangun: ", total_jin_pembangun)
#     if list_jin_pembangun_candi == []:
#         print("Jin Terajin: - ")
#         print("Jin Termalas: - ")
#     else:
#         print("Jin Terajin: ", jin_terajin)
#         print("Jin Termalas: ", jin_termalas)
#     print(f"Jumlah Pasir: {sisa_pasir} unit")
#     print(f"Jumlah Air: {sisa_air} unit")
#     print(f"Jumlah Batu: {sisa_batu} unit")

def laporancandi():
    if currentusers[2] != "bandung_bondowoso":
        print("Laporan candi hanya dapat diakses oleh bandung bondowoso")
        return None
    total_candi = Length(candi)
    total_pasir = 0
    total_batu = 0
    total_air = 0
    harga_candi = [0 for i in range(Length(candi))]
    max_harga = harga_candi[0]
    min_harga = harga_candi[0]
    idx_max = 0
    idx_min = 0
    for i in range(Length(candi)):
        total_pasir += int(candi[i][2])
        total_batu += int(candi[i][3])
        total_air += int(candi[i][4])
    for i in range(Length(candi)):
            harga_candi[i] = 10000*int(candi[i][2]) + 15000*int(candi[i][3]) + 7500*int(candi[i][4])
    for i in range(Length(candi)):
        if harga_candi[i] >= max_harga:
            max_harga = harga_candi[i]
            idx_max = i + 1
        if i == 0:
            min_harga = harga_candi[i]
            idx_min = i + 1
        else:
            if harga_candi[i] <= min_harga:
                min_harga = harga_candi[i]
                idx_min = i + 1
    rupiah_max = util.format_rupiah(max_harga)
    rupiah_min = util.format_rupiah(min_harga)
    print("Total Candi: ", total_candi)
    if total_candi == 0:
        print("Total Pasir yang digunakan : 0 ")
        print("Total Batu yang digunakan : 0 ")
        print("Total Air yang digunakan : 0 ")
        print("ID Candi Termahal: - ")
        print("ID Candi Termurah: - ")
    else:
        print("Total Pasir yang digunakan: ", total_pasir )
        print("Total Batu yang digunakan: ", total_batu)
        print("Total Air yang digunakan: ", total_air)
        print(f"ID Candi Termahal: {idx_max} ({rupiah_max}) ")
        print(f"ID Candi Termurah: {idx_min} ({rupiah_min}) ")

def ayamberkokok ():
    if currentusers[2] == 'roro_jonggrang' :
        totalcandi = Length (candi)
        print()
        print("Kukuruyuk.. Kukuruyuk..")
        print()
        print("Jumlah candi:", totalcandi)
        if (totalcandi < 100):
            print("Selamat, Roro Jonggrang memenangkan permainan!") 
            print("*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi.")
        else:
            print('Yah, Bandung Bondowoso memenangkan permainan!')

    else :
        print("Hanya roro jonggrang yang dapat mengakses")