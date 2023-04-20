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