from pemrosesanArray import addToArr

def isValid(username, arr_user) -> bool:
    for i in range(arr_user[0]):
        if (username == arr_user[2][i][0]):
            return False
    return True

def inputUsernameJin(arr_user):
    username_jin = input("Masukkan username jin: ")
    while not isValid(username_jin, arr_user):
        print('Username "' + username_jin + '" sudah diambil!')
        username_jin = input("Masukkan username jin: ")
    return username_jin

def inputPasswordJin(arr_user):
    password_jin = input("Masukkan password jin: ")
    while (len(password_jin) < 5 or len(password_jin) > 25):
        print("Password harus terdiri dari 5-25 karakter!")
        password_jin = input("Masukkan password jin: ")
    return password_jin

def summonjin(arr_pengumpul, arr_pembangun, arr_user) -> None:
    global new_arr_pembangun, new_arr_pengumpul, new_arr_user
    total_jin = arr_pembangun[0] + arr_pengumpul[0]
    if (total_jin == 100):
        # Data pada array tidak berubah
        new_arr_pembangun = arr_pembangun
        new_arr_pengumpul = arr_pengumpul
        new_arr_user = arr_user
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu.")
    else:   # total_jin < 100 Asumsi jumlah total jin tidak akan lebih dari 100 karena 100 adalah batas jumlah jin maksimal
        print("Jenis jin yang dapat dipanggil:")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi")
        jenis_jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
        while (jenis_jin != '1' and jenis_jin != '2'):
            print("Tidak ada jenis jin bernomor " + '"' + jenis_jin + '" !')
            jenis_jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
        if (jenis_jin == "1"):
            print('Memilih jin "Pengumpul"')
            new_username = inputUsernameJin(arr_user)
            password = inputPasswordJin(arr_user)
            new_arr_pembangun = arr_pembangun
            new_arr_pengumpul = [arr_pengumpul[0]+1, addToArr(new_username, arr_pengumpul[1], arr_pengumpul[0])]
            new_arr_user = [arr_user[0]+1, arr_user[1], addToArr([new_username, password, "jin_pengumpul"], arr_user[2], arr_user[0])]
        else:   # jenis_jin == "2"
            print('Memilih jin "Pembangun"')
            new_username = inputUsernameJin(arr_user)
            password = inputPasswordJin(arr_user)
            new_arr_pengumpul = arr_pengumpul
            new_arr_pembangun = [arr_pembangun[0]+1, addToArr(new_username, arr_pembangun[1], arr_pembangun[0])]
            new_arr_user = [arr_user[0]+1, arr_user[1], addToArr([new_username, password, "jin_pembangun"], arr_user[2], arr_user[0])]
            
        print("Mengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")
            
      
