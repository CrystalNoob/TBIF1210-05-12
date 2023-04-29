from pemrosesanArray import deleteFromArr

# jin_pembangun dan jin_pengumpul bisa filter dari array users
# jin_candi dan id_candi bisa filter dari array candi
def hapusjin(arr_user, arr_candi, arr_jinCandi)-> None:
    global new_arr_candi, new_arr_user
    username = input("Masukkan username jin: ")
    isFound = False
    for i in range(arr_user[0]):
        if (username == arr_user[2][i][0]):
            indeks = i
            isFound = True
    if isFound:
        # Hapus dari arr_user
        new_arr_user = [arr_user[0]-1 , arr_user[1], deleteFromArr(arr_user[2][indeks], arr_user[2], arr_user[0])]
        
        # Hapus dari arr_candi
        isMembangun = False
        for i in range(arr_jinCandi[0]):
            if (username == arr_jinCandi[1][i][0]):
                isMembangun = True
                jmlCandiHancur = i  
                
        if isMembangun:  
            indeksCandiHancur = [-1 for i in range(arr_jinCandi[1][jmlCandiHancur][1])] # Inisialisasi array
            j = 0
            for i in range(arr_candi[0]):
                if (username == arr_candi[2][i][1]):
                    indeksCandiHancur[j] = i
                    j += 1
            
            for i in range(jmlCandiHancur):
                arr_candi = [arr_candi[0]-1 , arr_candi[1], deleteFromArr(arr_candi[2][indeksCandiHancur[i]], arr_candi[2], arr_candi[0])]
            
            new_arr_candi = arr_candi
            
        else:   # Kalau jin tersebut tidak membangun sama sekali
            new_arr_candi = arr_candi   # array tetap
 
    else:   # not isFound
        print("Tidak ada jin dengan username tersebut!")