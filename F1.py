# Prosedur Login
def login(logged, arr, NMax) -> None:
    nameFound = False
    passMatch = False           # Init state
    if logged:          # Why log in when you're already logged?
        print(f"Login gagal!\nAnda telah login dengan username {loggedUser}, silahkan lakukan “logout” sebelum melakukan login kembali.")
    else:
        loggedUser = input("Username: ")    # Ask for input to authorize
        loggedPass = input("Password: ")
        i = 0
        while not nameFound and i < NMax:
            if loggedUser == arr[i][0]:
                nameFound = True
                i = 0
                while not passMatch and i < NMax:
                    if loggedPass == arr[i][1]:
                        passMatch = True
                        logged = True
                        role = arr[i][2]
                        print(f"Selamat datang, {loggedUser}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.")
                    i += 1
            i += 1
        if not nameFound:
            print("Username tidak terdaftar!")
        elif not passMatch:
            print("Password salah!")
