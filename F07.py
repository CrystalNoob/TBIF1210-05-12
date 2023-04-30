from B01 import random
from pemrosesanArray import addToArr
import time

def kumpul(isBatch, arr_bahan_bangunan) -> None:
    global new_arr_bahan_bangunan, get_air, get_batu, get_pasir
    seed = int(time.time())
    X0 = seed
    time.sleep(random(X0, 0, 1))    # di sleep supaya lebih random dan sleepnya juga di random lagi supaya lebih random
    X0 = seed
    get_pasir = random(X0, 0, 5)
    X0 = random(X0, 0, 5)
    get_batu = random(X0, 0, 5)
    X0 = random(X0, 0, 5)
    get_air = random(X0, 0, 5)
    X0 = random(X0, 0, 5)
    
    if(arr_bahan_bangunan[0] == 1): # kalau data bahan bangunan belum ada sama sekali
        arr_bahan_bangunan = [arr_bahan_bangunan[0]+1, arr_bahan_bangunan[1], addToArr(["pasir", "bahan material berbentuk butiran", str(get_pasir)], arr_bahan_bangunan[2], arr_bahan_bangunan[0])]
        arr_bahan_bangunan = [arr_bahan_bangunan[0]+1, arr_bahan_bangunan[1], addToArr(["batu", "benda alam yang tersusun atas kumpulan mineral penyusun kerak bumi", str(get_batu)], arr_bahan_bangunan[2], arr_bahan_bangunan[0])]
        arr_bahan_bangunan = [arr_bahan_bangunan[0]+1, arr_bahan_bangunan[1], addToArr(["air", "sebagai pelincir campuran kerikil, pasir, dan semen agar memudahkan pencetakan", str(get_air)], arr_bahan_bangunan[2], arr_bahan_bangunan[0])]
        new_arr_bahan_bangunan = arr_bahan_bangunan
    else:   # sebelumnya sudah ada data pasir, batu, dan air
        arr_bahan_bangunan[2][1][2] = int(arr_bahan_bangunan[2][1][2]) + get_pasir
        arr_bahan_bangunan[2][2][2] = int(arr_bahan_bangunan[2][2][2]) + get_batu
        arr_bahan_bangunan[2][3][2] = int(arr_bahan_bangunan[2][3][2]) + get_air
        new_arr_bahan_bangunan = arr_bahan_bangunan
        
    if not isBatch:
        print("Jin menemukan", get_pasir,"pasir,", get_batu, "batu, dan", get_air, "air.")
    