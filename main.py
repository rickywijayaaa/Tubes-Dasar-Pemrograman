import argparse
import util
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

# Define command-line arguments
parser = argparse.ArgumentParser(description='Load a CSV file')
parser.add_argument('folder', help='CSV file to load',nargs='?',default="")

# Parse arguments
args = parser.parse_args()
users =[]
candi =[]
bahan = []

#ambil path program yang dijalankan
root = os.path.dirname(os.path.realpath(__file__))

#cek apakah argumen folder yang diberi valid
if args.folder =="":
    print ("Tidak ada nama folder yang diberikan!\n")
    print("Usage: python main.py <nama_folder>")
    quit()

dir = os.path.join(root, args.folder)
if not os.path.isdir (dir):
    print(f"Folder {dir} tidak ditemukan.")
    quit()
#mulai membaca data
print("Loading....")

# Membaca CSV file

with open(os.path.join(args.folder,"user.csv"), 'r') as csv_file:
    for line in csv_file:
        # Remove newline character and split by ;
        row = line.strip().split(';')
        if (row[0] != 'username'):
            users = util.appendArr(users,row)


with open(os.path.join(args.folder,"candi.csv"), 'r') as csv_file:
    for line in csv_file:
        # Remove newline character and split by ;
        row = line.strip().split(';')
        if (row[0]!= 'id'):
            row[0] = int(row[0])
            candi = util.appendArr(candi,row)

with open(os.path.join(args.folder,"bahan_bangunan.csv"), 'r') as csv_file:
    for line in csv_file:
        # Remove newline character and split by ;
        row = line.strip().split(';')
        if (row[0]!= 'nama'):
            row[2] = int(row[2])
            bahan = util.appendArr(bahan,row)


currentusers = [-1,-1,-1]
import random


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

candi_sisa = [100]
def bangun(candi):
    if currentusers[0] == "bondowoso" or currentusers[0] == "roro" or currentusers[2] != "jin_pembangun":
        print("tidak bisa membangun")
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
                candi.append(newcandi) 
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
    else :
        break


#print(candi)