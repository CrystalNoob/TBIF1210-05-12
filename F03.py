import variabel
import database

def summon_jin():
    if login == False:
        print ("Anda belum login")
    elif (role != "bandung_bondowoso") :
        print("Anda tidak mempunyai akses")
    elif banyak_jin==100:
        print("Jumlah jin telah maksimal")
    else:
        print("Jenis jin yang dapat dipanggil:")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pemangun - Bertugas membangun candi")

        nomor_jenis_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        while (nomor_jenis_jin != 1) and (nomor_jenis_jin !=2):
            print(f"Tidak ada jenis jin bernomor \"{nomor_jenis_jin}\" !")
        if nomor_jenis_jin == 1:
            print ("Memilih jin \"Pengumpul\".")
            role = "jin_pengumpul"
        elif nomor_jenis_jin == 2:
            print ("Memilih jin \"Pembangun\".")
            role = "jin_pembangun"
            
        username = input("Masukkan username jin: ")
        exist, user = database.is_user_exist(username)
        while exist:
            print(f"Username \"{user.username}\" sudah diambil!")
            username = input("Masukkan username jin: ")
            exist, user = database.is_user_exist(username)
        
        password = input("Masukkan password jin: ")
        is_pass_valid = database.is_pass_valid(password)
        while not is_pass_valid:
            print (f"Password panjangnya harus 5-25 karakter!")
            password = input("Masukkan password jin: ")
            is_pass_valid = database.is_pass_valid(password)
        
        database.add_user(username, password, role)
        print("Mengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")
        print(f"Jin {username} berhasil dipanggil!")

        return 

