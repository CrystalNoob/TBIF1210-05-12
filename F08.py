from B01 import random
import F06
import time

def batchbangun(arr_jinPembangun, arr_candi, arr_id, arr_jinCandi, arr_bahan_bangunan):
    global new_arr_bahan_bangunan, new_arr_candi, new_arr_id, new_arr_jinCandi
    seed = int(time.time())
    X0 = seed   
    if (arr_jinPembangun[0] == 0):
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
        if (sum_req_pasir <= int(arr_bahan_bangunan[2][1][2]) and sum_req_batu <= int(arr_bahan_bangunan[2][2][2]) and sum_req_air <= int(arr_bahan_bangunan[2][3][2])):
            X0 = seed
            print("Mengerahkan", str(arr_jinPembangun[0]), "jin untuk membangun candi dengan total bahan", sum_req_pasir, "pasir,", sum_req_batu, "batu, dan", sum_req_air, "air.")
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
                F06.bangun(True, arr_jinPembangun[1][i], arr_id, arr_jinCandi, arr_candi, arr_bahan_bangunan)
                arr_id = F06.new_arr_id
                arr_jinCandi = F06.new_arr_jinCandi
                arr_candi = F06.new_arr_candi
            
            new_arr_bahan_bangunan = arr_bahan_bangunan
            new_arr_candi = arr_candi
            new_arr_jinCandi = arr_jinCandi
            new_arr_id = arr_id
                
        else:   # total bahan tidak mencukupi
            new_arr_bahan_bangunan = arr_bahan_bangunan
            new_arr_candi = arr_candi
            new_arr_jinCandi = arr_jinCandi
            new_arr_id = arr_id
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
                
                      
                
            
            


     
    