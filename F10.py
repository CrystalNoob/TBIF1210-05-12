def candiTermahal(arr_candi) -> int:
    # Spesifikasi : Mengetahui id candi dengan harga bahan termahal 
    # Jika ada lebih dari satu id candi yang memenuhi kondisi, dibebaskan untuk mengeluarkan yang mana
    # Menerima input array yang berisi id, pembuat, pasir, batu, dan air dari tiap candi yang telah dibangun
    
    if (arr_candi[0] == 1):
        return "-" # Kondisi ketika tidak ada candi yang telah dibangun
    else : # Kondisi ketika ada candi yang telah dibangun 
        hmax = (10000*int(arr_candi[2][1][2]))+(15000*int(arr_candi[2][1][3]))+(7500*int(arr_candi[2][1][4])) # Inisilisasi awal harga candi termahal
        idhmax = arr_candi[2][1][0] # Inisiasi awal id candi dengan harga bahan termahal
        for i in range(arr_candi[0]):
            if (i != 0):    # arr_candi [2][0][x] adalah header
                harga = (10000*int(arr_candi[2][i][2]))+(15000*int(arr_candi[2][i][3]))+(7500*int(arr_candi[2][i][4]))
                if harga >= hmax :
                    hmax = harga
                    idhmax = arr_candi[2][i][0]
    return idhmax,hmax        

def candiTermurah(arr_candi) -> int:
    # Spesifikasi : Mengetahui id candi dengan harga bahan termurah
    # Jika ada lebih dari satu id candi yang memenuhi kondisi, dibebaskan untuk mengeluarkan yang mana
    # Menerima input array yang berisi id, pembuat, pasir, batu, dan air dari tiap candi yang telah dibangun
    
    if (arr_candi[0] == 1):
        return "-" # Kondisi ketika tidak ada candi yang telah dibangun
    else : # Kondisi ketika ada candi yang telah dibangun 
        hmin = (10000*int(arr_candi[2][1][2]))+(15000*int(arr_candi[2][1][3]))+(7500*int(arr_candi[2][1][4])) # Inisiasi awal harga candi termurah
        idhmin = arr_candi[2][1][0] # Inisiasi awal harga candi termurah
        for i in range(arr_candi[0]):
            if (i != 0):    # arr_candi [2][0][x] adalah header 
                harga = (10000*int(arr_candi[2][i][2]))+(15000*int(arr_candi[2][i][3]))+(7500*int(arr_candi[2][i][4]))
                if harga <= hmin :
                    hmin = harga
                    idhmin = arr_candi[2][i][0]
        return idhmin,hmin

def pasir(arr_candi) -> int :
    if (arr_candi[0] == 1):
        banyakPasir = 0
        
    else :
        banyakPasir = 0
        for i in range(arr_candi[0]) :
            if (i != 0):    # arr_candi [2][0][x] adalah header
                banyakPasir += int(arr_candi[2][i][2])
    return banyakPasir

def batu(arr_candi) -> int :
    if (arr_candi[0] == 1):
        banyakBatu = 0
        
    else :
        banyakBatu = 0
        for i in range(arr_candi[0]) :
            if (i != 0):    # arr_candi [2][0][x] adalah header
                banyakBatu += int(arr_candi[2][i][3])
    return banyakBatu

def air(arr_candi) -> int :
    if (arr_candi[0] == 1):
        banyakAir = 0
        
    else :
        banyakAir = 0
        for i in range(arr_candi[0]) :
            if (i != 0):    # arr_candi [2][0][x] adalah header
                banyakAir += int(arr_candi[2][i][4])
    return banyakAir


def laporancandi(arr_candi) -> int :
    # Mengetahui total candi yang dibangun
    print("> Total Candi:", arr_candi[0]-1)
    # Mengetahui jumlah bahan bangunan yang digunakan untuk membangun candi
    print("> Total Pasir yang digunakan:", pasir(arr_candi))
    print("> Total Batu yang digunakan:", batu(arr_candi))
    print("> Total Air yang digunakan:", air(arr_candi))
    # Mengetahui ID candi dengen biaya bangun termahal dan termurah
    print("> ID Candi Termahal: " + str(candiTermahal(arr_candi)[0]) + " (Rp " + '{0:,}'.format(candiTermahal(arr_candi)[1]) + ")")
    print("> ID Candi Termurah: " + str(candiTermurah(arr_candi)[0]) + " (Rp " + '{0:,}'.format(candiTermurah(arr_candi)[1]) + ")")

# Debugging
# arr_candi = [3,3,[[11,"joko",2,2,2],[22,"budi",3,3,3],[33,"zidan",4,4,4]]]
# laporancandi(arr_candi)