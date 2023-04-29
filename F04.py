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
        confirm = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
        while (confirm != 'Y' and confirm != 'N'):
            confirm = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
        if (confirm == 'Y'):
            # Hapus dari arr_user
            new_arr_user = [arr_user[0]-1 , arr_user[1], deleteFromArr(arr_user[2][indeks], arr_user[2], arr_user[0])]    
            # Hapus dari arr_candi
            isMembangun = False
            for i in range(arr_jinCandi[0]):
                if (username == arr_jinCandi[1][i][0]):
                    isMembangun = True
                    indeksJin = i            
            if isMembangun:  
                banyakCandiHancur = int(arr_jinCandi[1][indeksJin][1])
                indeksCandiHancur = ["" for i in range(banyakCandiHancur)] # Inisialisasi array
                j = 0
                for i in range(arr_candi[0]):
                    if (username == arr_candi[2][i][1]):
                        indeksCandiHancur[j] = i
                        j += 1  
                        
                # Data dihapus dari belakang supaya urutan indeks array yang didepan tidak berubah
                i = banyakCandiHancur-1
                while (i >= 0):
                    arr_candi = [arr_candi[0]-1 , arr_candi[1], deleteFromArr(arr_candi[2][indeksCandiHancur[i]], arr_candi[2], arr_candi[0])] 
                    i -= 1 
                new_arr_candi = arr_candi  
            else:   # Kalau jin tersebut tidak membangun sama sekali
                new_arr_candi = arr_candi   # array tetap
            print("Jin telah berhasil dihapus dari alam gaib.")
        else:   # confirm == 'N'
            new_arr_candi = arr_candi
            new_arr_user = arr_user
            print("Jin tidak dihapus.")
    else:   # not isFound
        new_arr_user = arr_user
        new_arr_candi = arr_candi
        print("Tidak ada jin dengan username tersebut!")