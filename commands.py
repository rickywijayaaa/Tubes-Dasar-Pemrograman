from base import *
import argparse
from util import *
import os
import random


# FUNGSI BANTUAN 
# Fungsi Length : Menghitung panjang dari karakter
def Length (object) -> int :
    count = 0
    for i in object :
        count += 1
    return count    

# Fungsi Absolut : Menghitung selisih dari kedua variabel 
def Abs (a,b):
    c = a - b
    if c < 0 :
        c * -1
    return c

# Inisalisasi currentusers sebagai indikator user yang telah login
currentusers = [-1,-1,-1]
import random

# F01 - Login
# Melakukan login ke dalam sistem dengan mengakses username dan password yang terdaftar dalam users
# Apabila username yang dimasukkan user tidak terdaftar dan password yang dimasukkan tidak sesuai, akan dikeluarkan pesan kesalahan sesuai permasalahannya
# Pesan kesalahan juga akan dikeluarkan apabila username telah terdeteksi login sebelumnya dan belum melakukan logout

# Fungsi Main Login 
def login():
    # Menerima input user setelah menu Login
    uname = input("Username: ")
    pw = input("Password: ")
    # User sudah melakukan login sebelumnya
    if currentusers[0] != -1:
        print("Login gagal!")
        print(f'Anda telah login dengan username {uname}, silahkan lakukan "logout" sebelum melakukan login kembali.')
        return None
    # Pengecekan apakah username serta password yang dimasukkan terdaftar dalam users
    for i in range(Length(users)):
        # Apabila username terdaftar pada users
        if (username == users[i][0]):
            # Apabila password terdaftar pada users
            if (password == users[i][1]):
                print(f"\nSelamat datang, {uname}!")
                print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.')
                # Perubahan currentusers sebagai tanda terdeteksinya user yang sudah melakukan login
                currentusers[0] = users[i][0]
                currentusers[1] = users[i][1]
                currentusers[2] = users[i][2]
                return None
            # Password tidak terdaftar dalam users
            print("\nPassword salah!")
            return None
    # Username tidak terdaftar dalam users
    print("\nUser tidak terdaftar")
    return None

# F02 - Logout
# Melakukan logout ke luar sistem dengan menghilangkan akses dari akun sebelumnya dan dapat melakukan Login kembali ke dalam akun lain sesuai data pada users
# Pesan kesalahan akan diberikan apabila terdeteksi belum ada akun yang masuk atau melakukan Login

# Fungsi Main Logout
def logout():
    # User belum melakukan login sebelumnya
    if currentusers[0] == -1:
        print("Login gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        return None
    # User sudah melakukan login sebelumnya
    # currentusers[0] == -1 
    currentusers[0] = -1
    currentusers[1] = -1
    currentusers[2] = -1
    print("\nLogout berhasil, sampai jumpa lagi!\n")
    return None
    # Keluar dari akun

# F03 - Summon Jin
# Memanggil 2 jenis jin, yaitu jin pengumpul dan jin pembangun
# Pemanggilan jin hanya dapat dilakukan oleh user Bandung Bondowoso
# Jumlah maksimal Jin yang dapat di-summon yaitu sebanyak 100 jin
# Fungsi ini dapat memasukkan username jin dan password dengan panjang 5-25 karakter
# Jin yang telah di-summon dapat melakukan login untuk melakukan tugasnya

# Fungsi 1 untuk Summon Jin : Memasukkan username jin yang dipanggil
# Memasukkan username dari jin yang akan di-summon dan check apakah ada nama yang sama pada users yang ada dalam program
# Apabila terdapat nama yang sama maka akan dipanggil kembali function uname_summonjin
# Apabila tidak tersedia nama yang sama maka akan diproses function password
def uname_summonjin(users, jenis_jin):
    # Counter untuk check username sudah ada dalam users atau tidak
    check = 0
    
    # Input pertama username 
    uname = input("\nMasukkan username jin: ")
    
    # Perulangan untuk cek apakah ada username yang sama dengan username yang diinput user
    for i in range(Length (users)):
        if (users[i][0] == uname):
                check += 1
                
    # Percabangan sesuai dengan ada atau tidaknya username yang sama berdasarkan counter
    if check == 0: # Tidak ada username yang sama
        password(users, uname, jenis_jin) # Rekurens Fungsi Lain : Input Password
    else: # Tidak ada username yang sama
        print(f'\nUsername "{uname}" sudah diambil!')
        uname_summonjin(users, jenis_jin) # Rekurens Fungsi Ini Kembali
    return users

# Fungsi 2 untuk Summon Jin : Memasukkan password jin yang dipanggil
# Memasukkan password yang memenuhi syarat 5 sampai 25 karakter
# Apabila memenuhi maka akan diproses pemanggilan jin
# Apabila tidak memenuhi maka akan dipanggil kembali function password
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
            my_append(users,newusers)
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

# F04 - Hilangkan Jin

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

# F05 : Ubah Tipe Jin
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
                    print("Jin tidak jadi diubah")  
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
                    print("Jin tidak jadi diubah")
                    break
            else:
                print("id terdaftar namun bukan jin pengumpul maupun pembangun")
    if (idx == 0): # Jika username jin tidak tersedia
        print("Tidak ada jin dengan username tersebut.")


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


def hancurkan_candi():
    if currentusers[2] == "roro_jonggrang" :
        id = int(input("Masukkan ID candi: "))
        muncul = False
        for i in range (Length(candi)):
            if id != candi[i][0]:
                continue
            else:
                muncul = True
                no = i
                break 

        if muncul == False:
            print("Tidak ada candi dengan ID tersebut.")
        else:
            confirm = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ")

            if confirm == "Y" or confirm == "y":
                for i in range (5):
                    candi[no][i] = None
                print("Candi telah berhasil dihancurkan.")
            elif confirm == "n" or confirm == "N":       
                print("Batal menghancurkan candi")

    else:
        print("Tidak dapat diakses")


def save ():
    dir = input("Masukkan nama folder :")


    path = os.path.join(root)
    path = os.path.join(path,"save")
    path = os.path.join(path,dir)
    if not(os.path.isdir(path)):
        print("Saving...")
        os.mkdir(path)
    users2 =[]
    candi2= []
    bahan2=[]

    for i in range(Length(candi)):
        candi[i][0] = str(candi[i][0])
    for i in range(Length(bahan)):
        bahan[i][2] = str(bahan[i][2])

    for i in range (Length(users)):
        my_append(users2,util.merge_n (users[i],3,";"))

    for i in range (Length(candi)):
        my_append(candi2,util.merge_n (candi[i],5,";"))
    for i in range (Length(bahan)):
        my_append(bahan2,util.merge_n (bahan[i],3,";"))

    print(util.merge_n (users[i],3,";"))
    text = ""
    textcandi =""
    textbahan = ""
    for i in range (Length(users2)):
        text += users2[i] + "\n"
    for i in range (Length(candi2)):
        textcandi += candi2[i] + "\n"
    for i in range (Length(bahan2)):
        textbahan += bahan2[i] + "\n"


    with open (os.path.join(path,'user.csv'),'w') as f :
        f.write (text)
        

    with open (os.path.join(path,'candi.csv'),'w') as f :
        f.write (textcandi)


    with open (os.path.join(path,'bahan_bangunan.csv'),'w') as f :
        f.write (textbahan)

    print(f"Berhasil menyimpan data di folder {path}")
