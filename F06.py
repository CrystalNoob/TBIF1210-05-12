import time
from B01 import random
from pemrosesanArray import addToArr, init_arr

def bangun(isBatch, username, arr_id, arr_jinCandi, arr_candi, arr_bahan) -> None:
    global new_arr_bahan, new_arr_candi, new_arr_id, new_arr_jinCandi, req_air, req_batu, req_pasir
    if (arr_candi[0] == 101):
        new_arr_bahan = arr_bahan
        new_arr_candi = arr_candi
        new_arr_id = arr_id
        new_arr_jinCandi = arr_jinCandi
        print("Candi berhasil dibangun.")
        print("Sisa candi yang perlu dibangun: 0.")
    else:
        seed = int(time.time())
        X0 = seed  
        # Generate bahan
        if not isBatch:
            req_pasir = random(X0, 1, 5)
            X0 = req_pasir
            req_batu = random(X0, 1, 5)
            X0 = req_batu
            req_air = random(X0, 1, 5)
            X0 = req_air
            
        else:
            # Set nilai agar melewati kondisional if
            req_pasir = 0
            req_batu = 0
            req_air = 0
            
        
        if (arr_bahan[0] == 4 and req_pasir <= int(arr_bahan[2][1][2]) and req_batu <= int(arr_bahan[2][2][2]) and req_air <= int(arr_bahan[2][3][2])):
            # Update bahan bangunan
            if not isBatch:
                arr_bahan[2][1][2] = str(int(arr_bahan[2][1][2])-req_pasir)
                arr_bahan[2][2][2] = str(int(arr_bahan[2][2][2])-req_batu)
                arr_bahan[2][3][2] = str(int(arr_bahan[2][3][2])-req_air)
                new_arr_bahan = arr_bahan
            # Menentukan ID Candi
            n_eff_id = arr_id[0]
            is_newID = True
            if (n_eff_id == 0):
                getID = 1
                new_arr_id = [getID, [1]]
            else:
                for i in range(n_eff_id):
                    if (arr_id[1][i] == 0):
                        getID = i + 1
                        is_newID = False
                        break
                if (is_newID):
                    getID = n_eff_id+1
                    new_arr_id = [n_eff_id+1, addToArr(getID, arr_id[1], n_eff_id)]
                else:
                    new_arr_id = arr_id
                    for i in range(arr_id[0]):
                        if (i == getID-1):
                            new_arr_id[1][i] = getID
                            
            # Update arr_jinCandi
            if (arr_jinCandi[0] == 0):
                new_arr_jinCandi = [1, [[username, 1]]]
            else:
                is_newJin = True
                for i in range(arr_jinCandi[0]):
                    if (username == arr_jinCandi[1][i][0]):
                        arr_jinCandi[1][i][1] = arr_jinCandi[1][i][1] + 1
                    new_arr_jinCandi = arr_jinCandi
                    is_newJin = False
                if is_newJin:
                    new_arr_jinCandi = [arr_jinCandi[0]+1, addToArr([username, 1], arr_jinCandi[1], arr_jinCandi[0])]
            # Update arr_candi
            n_eff_candi = int(arr_candi[0]) + 1
            new_arr_candi = [n_eff_candi, arr_candi[1], addToArr([str(getID), username, req_pasir, req_batu, req_air], arr_candi[2], int(arr_candi[0])) ]
            if not isBatch:
                print("Candi berhasil dibangun!")
                print("Sisa candi yang perlu dibangun:", 100-int(arr_candi[0])+1)
        else:
            new_arr_bahan = arr_bahan
            new_arr_candi = arr_candi
            new_arr_id = arr_id
            new_arr_jinCandi = arr_jinCandi
            if not isBatch:
                print("Bahan bangunan tidak mencukupi!")
                print("Candi tidak bisa dibangun!")