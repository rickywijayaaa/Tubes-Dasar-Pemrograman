# Fungsi mencari panjang object
def Length (object) -> int :
    count = 0
    for i in object :
        count += 1
    return count 

users =[["username","password","role"],["Bondowoso","cintaroro","bandung_bondowoso"],["Roro","gasukabondo","roro_jonggrang"]]
username = input("Username: ")
password = input("Password: ")
    
user_data = [users[i][0] for i in range (1, Length(users))]
pass_data = [users[i][1] for i in range (1, Length(users))]
# Validasi
for i in range (Length(user_data)) :
    if (username == user_data[i] and password == pass_data[i]):
        print("")
        print(f"Selamat datang, {username}!")
        break
        # MainMenu (users[i+1][2])
    elif (username == user_data[i]):
        print("")
        print("Password salah!")
        # Start()
    elif (i == Length(user_data) - 1) :
        print("")
        print("Username tidak terdaftar!")
        # Start()

