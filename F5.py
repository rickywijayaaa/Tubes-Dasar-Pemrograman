# Fungsi mencari panjang object
def Length (object) -> int :
    count = 0
    for i in object :
        count += 1
    return count 

users =[["username","password","role"],
        ["Bondowoso","cintaroro","bandung_bondowoso"],
        ["Roro","gasukabondo","roro_jonggrang"],
        ["Jin1","IfritGantengXX:*","jin_pengumpul"],
        ["Jin2","hahahahaha","jin_pembangun"]]

user_data = [users[i][0] for i in range (1, Length(users))]
role_data = [users[i][2] for i in range (1, Length(users))]
print(">>> ubahjin")
username= input("Masukkan username jin : ")
for i in range (Length(user_data)) :
    if (username == user_data[i]  ):
        if (role_data[i]== "jin_pengumpul"):
            print("")
            print ("Jin ini bertipe 'Pengumpul'. Yakin ingin mengubah ke tipe 'Pembangun' (Y/N)?" )
            persetujuan = input()
            if (persetujuan == "Y"):
                role_data[i] = "jin_pembangun"
                print("Jin telah berhasil diubah.")
                break
        elif (role_data[i]== "jin_pembangun"):
            print("")
            print ("Jin ini bertipe 'Pembangun'. Yakin ingin mengubah ke tipe 'pengumpul' (Y/N)?" )
            persetujuan = input()
            if (persetujuan == "Y"):
                role_data[i] = "jin_pengumpul"
                print("Jin telah berhasil diubah.")
                break
else : # Jika username jin tidak tersedia
    print("Tidak ada jin dengan username tersebut.")


