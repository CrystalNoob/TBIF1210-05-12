from B01 import random
import F06
import F07
import time

def batchbangun(arr_jinPembangun, arr_candi, arr_id, arr_bahan_bangunan):
    global new_arr_bahan_bangunan, new_arr_candi, new_arr_id
    seed = int(time.time())
    X0 = seed   
    if (arr_jinPembangun[0] == 0):
        new_arr_candi = arr_candi
        new_arr_bahan_bangunan = arr_bahan_bangunan
        new_arr_id = arr_id
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu!")
    else:   # Ada jin
        # Menghitung total bahan yang diperlukan
        sum_req_pasir = 0
        sum_req_batu = 0
        sum_req_air = 0
        for i in range(arr_jinPembangun[0]):
            sum_req_pasir += random(X0, 1, 5)
            X0 = random(X0, 1, 5)
            sum_req_batu += random(X0, 1, 5)
            X0 = random(X0, 1, 5)
            sum_req_air += random(X0, 1, 5)
            X0 = random(X0, 1, 5)
        print("Mengerahkan", str(arr_jinPembangun[0]), "jin untuk membangun candi dengan total bahan", sum_req_pasir, "pasir,", sum_req_batu, "batu, dan", sum_req_air, "air.")
        if (sum_req_pasir <= int(arr_bahan_bangunan[2][1][2]) and sum_req_batu <= int(arr_bahan_bangunan[2][2][2]) and sum_req_air <= int(arr_bahan_bangunan[2][3][2])):
            X0 = seed   # X0 di-reset agar random bahan sama seperti random bahan yang dilakukan sebelumnya
            for i in range(arr_jinPembangun[0]):
                req_pasir = random(X0, 1, 5)
                X0 = random(X0, 1, 5)
                req_batu = random(X0, 1, 5)
                X0 = random(X0, 1, 5)
                req_air = random(X0, 1, 5)
                X0 = random(X0, 1, 5)
                # Update arr_bahan_bangunan
                arr_bahan_bangunan[2][1][2] = str(int(arr_bahan_bangunan[2][1][2])-req_pasir)
                arr_bahan_bangunan[2][2][2] = str(int(arr_bahan_bangunan[2][2][2])-req_batu)
                arr_bahan_bangunan[2][3][2] = str(int(arr_bahan_bangunan[2][3][2])-req_air) 
                F06.bangun(True, arr_jinPembangun[1][i], arr_id, arr_candi, arr_bahan_bangunan)
                arr_candi = F06.new_arr_candi
                arr_id = F06.new_arr_id
                arr_candi[2][arr_candi[0]-1][2] = req_pasir
                arr_candi[2][arr_candi[0]-1][3] = req_batu
                arr_candi[2][arr_candi[0]-1][4] = req_air
                    
            new_arr_bahan_bangunan = arr_bahan_bangunan
            new_arr_candi = arr_candi
            new_arr_id = arr_id
            print("Jin berhasil membangun total", arr_jinPembangun[0], "candi.")
                
        else:   # total bahan tidak mencukupi
            new_arr_bahan_bangunan = arr_bahan_bangunan
            new_arr_candi = arr_candi
            kurang_pasir = sum_req_pasir - int(arr_bahan_bangunan[2][1][2])
            kurang_batu = sum_req_batu - int(arr_bahan_bangunan[2][2][2])
            kurang_air = sum_req_air - int(arr_bahan_bangunan[2][3][2])
            if (kurang_pasir <= 0): #   Jika pasir tidak kurang
                kurang_pasir = 0
            if(kurang_batu <= 0):   #   Jika batu tidak kurang
                kurang_batu = 0
            if(kurang_air <= 0):    #   Jika air tidak kurang
                kurang_air = 0
            print("Bangun gagal. Kurang", kurang_pasir,"pasir,", kurang_batu, "batu, dan", kurang_air, "air.")

def batchkumpul(arr_pengumpul, arr_bahan_bangunan) -> None:
    global new_arr_bahan_bangunan_kumpul
    if (arr_pengumpul[0] == 0):
        new_arr_bahan_bangunan_kumpul = arr_bahan_bangunan
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:   # Ada jin pengumpul
        sum_get_pasir = 0
        sum_get_batu = 0
        sum_get_air = 0
        print("Mengerahkan", arr_pengumpul[0], "jin untuk mengumpulkan bahan.")
        print("Sedang mengumpulkan bahan...")
        for i in range(arr_pengumpul[0]):
            F07.kumpul(True, arr_bahan_bangunan)
            sum_get_pasir += F07.get_pasir
            sum_get_batu += F07.get_batu
            sum_get_air += F07.get_air
            arr_bahan_bangunan = F07.new_arr_bahan_bangunan
        print("Jin menemukan total", sum_get_pasir, "pasir,", sum_get_batu, "batu, dan", sum_get_air, "air.")
        new_arr_bahan_bangunan_kumpul = arr_bahan_bangunan   