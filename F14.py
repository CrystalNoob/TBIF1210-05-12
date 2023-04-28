import os
import sys
from csv_arr_Converter import arrToCsv

# Procedure
# ASUMSI : Nama folder yang diinput sudah pasti valid (dalam artian tidak mengandung simbol yang tidak dapat digunakan)
def save(arr_user, arr_candi, arr_bahan_bangunan) -> None:
    directory = input("Masukkan nama folder : ")
    print("Saving...")
    isFound_save = False
    isFound_dir = False
    parent = './save/'
    path = os.path.join(parent, directory)
    for root, dirs, files in os.walk('.'):  
       if (root == ".\save"):
           isFound_save = True
    if isFound_save:
        for root, dirs, files in os.walk(parent):
            for _dir in dirs:
                if (_dir == directory):
                    isFound_dir = True
        if not isFound_dir:
            os.mkdir(path)
            print("Membuat folder save/" + directory + "...")       
    else:  # not isFound_save       
        os.makedirs(path)
        print("Membuat folder save...")
        print("Membuat folder save/" + directory + "...")       
        
    arrToCsv(arr_user, path + '/' + "user.csv")
    arrToCsv(arr_candi, path + '/' + "candi.csv")
    arrToCsv(arr_bahan_bangunan, path + '/' + "bahan_bangunan.csv")
    print("Berhasil menyimpan data di folder save/" + directory + '!')
