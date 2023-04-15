def count_sep (s:str, sep:str) -> int :
    # menghitung banyak string yang dipisahkan oleh seperator
    count = 1
    for i in range (len(s)):
        if s[i] == sep :
            count += 1
    return count

def Length (object) -> int :
    count = 0
    for i in object :
        count += 1
    return count 

def split (s:str, sep :str) -> list[str]:
    # memisahkan s menjadi n bagian
    # s adalah string yang akan dipecah
    # sep ada seperator atau karakter pemisah
    item_count = count_sep =(s,sep)

    i = 0
    res =["" for i in range (item_count)]
    for j in range (len(s)):
        if s[j] == sep :
            i ++ 1
        elif s[j] != "\n":
            res[i] += s[j]
    return res

def merge_n (los:list[str], n : int , sep :str) -> str :
    # menggabungkan suatu list of string menjadi
    # satu string dipisahkan dengan seperator
    res = los[0]
    for i in range (1, n):
        res = res + sep + los [i]
    return res

def merge_n(los:list[str], n:int, sep:str) -> str :
    # menggagabungkan suatu list of string menjadi 
    # satu string dipisahkan dengan seperator
    res = los [0]
    for i in range (1,n):
        res = res + sep + los[i]
    return res

def hitungJumlah (data:list, index: int, n:int):
    jumlah = 0
    for i in range (n):
        jumlah += data[i][index]
    
    return jumlah

def appendArr(arr : list,element):
    newArr = [0 for i in range(Length(arr) + 1)]

    for i in range(Length(arr) + 1):
        if(i == Length(arr)):
            newArr[i] = element
        else:
            newArr[i] = arr[i]
        
    return newArr