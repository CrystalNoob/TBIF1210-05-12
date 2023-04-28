# Declare the existence of global vars
userName = ''
logged = bool()
role = ''

# Logout procedure
def logout() -> None:
    listOfGlobals = globals()           # declare to use the global var instead of local
    if listOfGlobals['logged']:
        listOfGlobals['userName'] = ''  # Empty every user-related logged-in state
        listOfGlobals['logged'] = False
        listOfGlobals['role'] = ''
    else:                               # How to logout when you haven't even logged in?
        print("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout")

# Debug & Testing [Passed]
# if __name__ == "__main__":
#     userName = 'Bondowoso'
#     logged = True
#     role = 'bandung_bondowoso'
#     logout()
#     print(userName)
#     print(logged)
#     print(role)
