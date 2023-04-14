# Konstanta
NMax = 102

# Prosedur Login
def login() -> None:
    match = False
    logged = False
    loggedUser = input("Username: ")
    loggedPass = input("Password: ")

    if not logged:
        print("Login gagal!" + '\n' + "Anda telah login dengan username Bandung, silahkan lakukan “logout” sebelum melakukan login kembali.")
    else:
        i = 1
        while not match and i <= NMax:
            # if uname matched:
                # if pass matched:
                    # match = True
                    # logged = True
                    # role = role dari file csv
                    # print("Selamat datang," loggedUser + "!" + '\n' + "Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                # else:
                    # print("Password salah!")
            i += 1
        if not match:
            print("Username tidak terdaftar!")

# listUser = open("user.csv", 'r')
# userName = listUser.read(1)



# while True:
#     loginName += userName
#     userName = listUser.read(1)
#     if userName == mark:
#         break
# print(loginName)
# listUser.close()
