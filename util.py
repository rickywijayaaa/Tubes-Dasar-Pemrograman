# Fungsi Bantuan 1 : Menghitung panjang karakter pada suatu tipe data
def Length (object) -> int :
    count = 0
    for i in object :
        count += 1
    return count 

# Fungsi Bantuan 2 : Menghitung banyak string yang dipisahkan oleh separator
def count_sep (s:str, sep:str) -> int :
    # Inisialisasi counter count
    count = 1
    # Pengulangan counter separator
    for i in range (Length(s)):
        if s[i] == sep :
            count += 1
    return count

# Fungsi Bantuan 3 
# Memisahkan s menjadi n bagian
# s adalah string yang akan dipecah
# sep ada separator atau karakter pemisah
def split (s:str, sep :str) -> list[str]:
    item_count = count_sep =(s,sep)

    i = 0
    res =["" for i in range (item_count)]
    for j in range (len(s)):
        if s[j] == sep :
            i ++ 1
        elif s[j] != "\n":
            res[i] += s[j]
    return res

# Fungsi Bantuan 4
# Menggabungkan suatu list of string
# menjadi satu string dipisahkan dengan separator
def merge_n (los:list[str], n : int , sep :str) -> str :
    res = los[0]
    for i in range (1, n):
        res = res + sep + los [i]
    return res

# Fungsi Bantuan 5
# Menggabungkan suatu list of string menjadi 
# satu string dipisahkan dengan separator
def merge_n(los:list[str], n:int, sep:str) -> str :
    res = los [0]
    for i in range (1,n):
        res = res + sep + los[i]
    return res

# Fungsi Bantuan 
def hitungJumlah (data:list, index: int, n:int):
    jumlah = 0
    for i in range (n):
        jumlah += data[i][index]
    
    return jumlah
    
# Fungsi Bantuan 6
def appendArr(arr : list,element):
    newArr = [0 for i in range(Length(arr) + 1)]

    for i in range(Length(arr) + 1):
        if(i == Length(arr)):
            newArr[i] = element
        else:
            newArr[i] = arr[i]
        
    return newArr

# Fungsi Bantuan 7
def my_append(Arr, item):
    
    Arr += [item]
    return Arr

# Fungsi Bantuan 8
def format_rupiah(integer):
    string = str(integer)[::-1]
    digit_count = Length(string)
    result = ''
    for i in range(digit_count):
        result = string[i] + result
        if (i + 1) % 3 == 0 and i != digit_count - 1:
            result = '.' + result
    result = 'Rp ' + result
    return result

# Fungsi Bantuan 9
def sort_by_frequency(Arr):
    jumlah_kemunculan = []
    for i in range(Length(Arr)):
        count = 0
        for j in range(Length(Arr)):
            if Arr[i] == Arr[j]:
                count += 1
        my_append(jumlah_kemunculan,count) 
    for i in range(len(jumlah_kemunculan)):
        for j in range(i+1, Length(jumlah_kemunculan)):
            if jumlah_kemunculan[i] < jumlah_kemunculan[j]:
                jumlah_kemunculan[i], jumlah_kemunculan[j] = jumlah_kemunculan[j], jumlah_kemunculan[i]
                Arr[i], Arr[j] = Arr[j], Arr[i]
            elif jumlah_kemunculan[i] == jumlah_kemunculan[j] and Arr[i] > Arr[j]:
                jumlah_kemunculan[i], jumlah_kemunculan[j] = jumlah_kemunculan[j], jumlah_kemunculan[i]
                Arr[i], Arr[j] = Arr[j], Arr[i]
