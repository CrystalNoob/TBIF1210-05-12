# Declare global vars
userName = ''
logged = bool()
role = ''

# Login Procedure
def login(logState, arr, NMax) -> None:     # arr with format [["name", "pass", "role"]]
    global userName             # Declare global var to edit/read
    nameFound = False
    passMatch = False           # Init state

    if logState:          # Why log in when you're already logged?
        print(f"Login gagal!\nAnda telah login dengan username {userName}, silahkan lakukan “logout” sebelum melakukan login kembali.")
    else:
        loggedUser = input("Username: ")    # Ask for input to authorize
        loggedPass = input("Password: ")
        i = 0                               # For looping
        while not nameFound and i < NMax:   # NMax to search until the end of the array
            if loggedUser == arr[i][0]:     # If match any username that exist in the array of users
                nameFound = True
                if loggedPass == arr[i][1]:     # Inputted pass matched with pass in username's index
                    global logged, role         # Declare global var to edit
                    userName = loggedUser       # Change global values
                    passMatch = True
                    logged = True
                    role = arr[i][2]
                    print(f"Selamat datang, {loggedUser}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.")
                else:                           # Wrong pass
                    print("Password salah!")
            i += 1
        if not nameFound:                           # Not found in any array of users
            print("Username tidak terdaftar!")

# Debug & Testing [Passed]
# if __name__ == "__main__":
#     users = [["username", "password", "role"],
#              ["Bondowoso", "cintaroro", "bandung_bondowoso"],
#              ["Roro", "gasukabondo", "roro_jonggrang"],
#              ["Test", "asdf", "jin_pembangun"]]
#     # logged = True
#     # userName = "Bondowoso"
#     # role = "bandung_bondowoso"
#     login(logged, users, len(users))
#     print(userName)
#     print(logged)
#     print(role)