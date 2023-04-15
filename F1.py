# Konstanta
NMax = 102

# Prosedur Login
def login() -> None:
    match = False
    logged = False
    loggedUser = input("Username: ")
    loggedPass = input("Password: ")

    if logged:
        print("Login gagal!\nAnda telah login dengan username Bandung, silahkan lakukan “logout” sebelum melakukan login kembali.")
    else:
        i = 1
        while not match and i <= NMax:
            if loggedUser == 'test':
                if loggedPass == 'test':
                    match = True
                    logged = True
                    role = "Bandung"
                    print(f"Selamat datang, {loggedUser}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.")
                else:
                    print("Password salah!")
            i += 1
        if not match:
            print("Username tidak terdaftar!")
