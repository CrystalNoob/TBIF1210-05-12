import argparse
import os
import sys
from csv_arr_Converter import csvToArr

arr_userCSV = ["0", "0", []]
arr_candiCSV = ["0", "0", []]
arr_bahan_bangunanCSV = ["0", "0", []]


def load() -> None:
    global arr_userCSV, arr_candiCSV, arr_bahan_bangunanCSV
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", help='nama folder yang akan di load, jika belum pernah memulai sama sekali, silakan masukkan nama folder "New Folder" ', nargs='?')
    args = parser.parse_args()
    nama_folder = args.nama_folder
    if nama_folder is None:
        print("Tidak ada nama folder yang diberikan!")
        sys.exit()
    # elif (nama_folder == "New Folder"):
    #     path
    elif (nama_folder == "New Folder"):
        path = "./New Folder"
        for _file in os.listdir(path):
            if (_file == "user.csv"):
                arr_userCSV = csvToArr(path + '/' + _file)
            if (_file == "candi.csv"):
                arr_candiCSV = csvToArr(path + '/' + _file)
            if (_file == "bahan_bangunan.csv"):
                arr_bahan_bangunanCSV = csvToArr(path + '/' + _file)
    else:
        path = "./save/"
        isFound = False
        for root, dirs, files in os.walk(path): # Reference : https://www.w3resource.com/python-exercises/os/python-os-exercise-11.php
            for _dir in dirs:
                if (nama_folder == _dir):
                    isFound = True
                    for _file in os.listdir(path + _dir):
                        if (_file == "user.csv"):
                            arr_userCSV = csvToArr(path + _dir + '/' + _file)
                        if (_file == "candi.csv"):
                            arr_candiCSV = csvToArr(path + _dir + '/' + _file)
                        if (_file == "bahan_bangunan.csv"):
                            arr_bahan_bangunanCSV = csvToArr(path + _dir + '/' + _file)
        if (not isFound):
            print('Folder "' + nama_folder + '" tidak ditemukan.')
            sys.exit()
                        
                    
                