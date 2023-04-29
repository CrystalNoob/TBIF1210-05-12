def ubahjin(arr_user) -> None:
    global new_arr_user
    username = input("Masukkan username jin :")
    isFound = False
    for i in range(arr_user[0]):
        if (username == arr_user[2][i][0]):
            isFound = True
            indeks = i
    if isFound:
        if (arr_user[2][indeks][2] == "jin_pengumpul"):
            confirm = input('Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun" (Y/N)? ')
            while (confirm != "Y" and confirm != "N"):
                confirm = input('Jin ini bertipe "Pengumpul". Yakin ingin mengubah ke tipe "Pembangun" (Y/N)? ')
            if (confirm == 'Y'):
                arr_user[2][indeks][2] = "jin_pembangun"
                new_arr_user = arr_user
            else:
                new_arr_user = arr_user
                print("Jin tidak diubah") 
        else:   # arr_user[2][indeks][2] == "jin_pembangun"
            confirm = input('Jin ini bertipe "Pembangun". Yakin ingin mengubah ke tipe "Pengumpul" (Y/N)? ')
            while (confirm != "Y" and confirm != "N"):
                confirm = input('Jin ini bertipe "Pembangun". Yakin ingin mengubah ke tipe "Pengumpul" (Y/N)? ')
            if (confirm == 'Y'):
                arr_user[2][indeks][2] = "jin_pengumpul"
                new_arr_user = arr_user
            else:
                new_arr_user = arr_user
                print("Jin tidak diubah") 
            
    else:   # not isFound
        new_arr_user = arr_user
        print("Tidak ada jin dengan username tersebut.")
    