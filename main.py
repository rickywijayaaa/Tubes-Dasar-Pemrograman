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
            candi = util.appendArr(candi,row)

with open(os.path.join(args.folder,"bahan_bangunan.csv"), 'r') as csv_file:
    for line in csv_file:
        # Remove newline character and split by ;
        row = line.strip().split(';')
        if (row[0]!= 'nama'):
            row[2] = int(row[2])
            bahan = util.appendArr(bahan,row)

# print(users[0][2])

# print ("Selamat datang di program “Manajerial Candi”")
# print ("Silahkan masukkan username Anda")
# lanjut masuk ke main program
# print(users)
# print(candi)
#print(bahan)
# F7 kumpul
# def kumpul ():
#     jumlahtemp =[0,0,0]
#     for i in range (len(users)):
#         if (users != "Bondowoso") and (users != "Roro") and users[i][2] == "jin_pengumpul":
#             pasir = random.randint (0,5)
#             jumlahtemp[0]+= pasir
#             batu = random.randint (0,5)
#             jumlahtemp[1]+= batu
#             air = random.randint (0,5)
#             jumlahtemp[2] += air

        
#     print ("Jin menemukan",jumlahtemp[0],"pasir",jumlahtemp[1],"batu",jumlahtemp[2],"air")

#     for i in range (3):
#         if (bahan[i][0] == "pasir"):
#             bahan [i][2] += jumlahtemp[0]
#         elif (bahan[i][0] == "batu"):
#             bahan [i][2] += jumlahtemp[1]
#         elif (bahan[i][0] == "air"):
#             bahan[i][2] += jumlahtemp[2]
currentusers = [-1,-1,-1]
def kumpul ():
    if currentusers[0] == "bondowoso" or currentusers[0] == "roro" or currentusers[2] != "jin_pengumpul":
        print("lu gabisa ngumpulin bahan anjg")
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

while True:
    menu = input()
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
    else :
        break


#print(candi)