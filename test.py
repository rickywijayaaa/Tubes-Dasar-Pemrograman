import util
from base import * 
def save ():
    dir = input("Masukkan nama folder :")
    print(users)


    path = os.path.join(root)
    path = os.path.join(path,"save")
    path = os.path.join(path,dir)
    if not(os.path.isdir(path)):
        print("Saving...")
        os.mkdir(path)
    users2 =[]
    candi2= []
    bahan2=[]

    for i in range(len(candi)):
        candi[i][0] = str(candi[i][0])
    for i in range(len(bahan)):
        bahan[i][2] = str(bahan[i][2])

    for i in range (len(users)):
        users2.append(util.merge_n (users[i],3,";"))

    for i in range (len(candi)):
        candi2.append(util.merge_n (candi[i],5,";"))
    for i in range (len(bahan)):
        bahan2.append(util.merge_n (bahan[i],3,";"))


    text = ""
    textcandi =""
    textbahan = ""
    for i in range (len(users2)):
        text += users2[i] + "\n"
    for i in range (len(candi2)):
        textcandi += candi2[i] + "\n"
    for i in range (len(bahan2)):
        textbahan += bahan2[i] + "\n"


    with open (os.path.join(path,'user.csv'),'w') as f :
        f.write (text)
        

    with open (os.path.join(path,'candi.csv'),'w') as f :
        f.write (textcandi)


    with open (os.path.join(path,'bahan_bangunan.csv'),'w') as f :
        f.write (textbahan)

    print(f"Berhasil menyimpan data di folder {path}")