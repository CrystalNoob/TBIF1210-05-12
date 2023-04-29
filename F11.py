from pemrosesanArray import deleteFromArr

def hancurkancandi(arr_candi):
    global new_arr_candi
    hapus_id = input("Masukkan ID candi: ")
    isFound = False
    for i in range(arr_candi[0]):
        if (i != 0):    # indeks 0 adalah header
            if (int(arr_candi[2][i][0]) == int(hapus_id)):
                isFound = True
                indeksHapus = i
    if isFound:
        confirm = input("Apakah anda yakin ingin menghancurkan candi ID: " + str(hapus_id) +" (Y/N)? ")
        while (confirm != 'Y' and confirm != 'N'):
            confirm = input("Apakah anda yakin ingin menghancurkan candi ID: " + str(hapus_id) +" (Y/N)? ")
        if (confirm == 'Y'):
            new_arr_candi = [arr_candi[0]-1 , arr_candi[1], deleteFromArr(arr_candi[2][indeksHapus], arr_candi[2], arr_candi[0])]
            print("***************************************")
            print("* DUARRR! Candi berhasil dihancurkan! *")
            print("***************************************")
        else:   # confirm == 'N'
            new_arr_candi = arr_candi
            print("Candi tidak dihancurkan.")
    else:   # not isFound
        new_arr_candi = arr_candi
        print("Tidak ada candi dengan ID tersebut.")