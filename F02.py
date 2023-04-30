# Logout procedure
def logout(logged) -> None:
    global get_username, get_role, get_logged           # declare to use the global var instead of local
    if logged:
        print("Berhasil Logout!")
    else:                               # How to logout when you haven't even logged in?
        print("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    get_username = ''  # Empty every user-related logged-in state
    get_logged = False
    get_role = ''

# Debug & Testing [Passed]
# if __name__ == "__main__":
#     userName = 'Bondowoso'
#     logged = True
#     role = 'bandung_bondowoso'
#     logout()
#     print(userName)
#     print(logged)
#     print(role)
