from csv_arr_Converter import csvToArr
from length_CSV import lenCsvRow

# Konstanta
NMax = lenCsvRow("user.csv")
arr = csvToArr("user.csv")

# Prosedur Login
def login() -> None:
    nameFound = False
    passMatch = False
    logged = False
    loggedUser = input("Username: ")
    loggedPass = input("Password: ")

    if logged:
        print("Login gagal!\nAnda telah login dengan username Bandung, silahkan lakukan “logout” sebelum melakukan login kembali.")
    else:
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
