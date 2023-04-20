# Prosedur Logout
def logout():
    listOfGlobals = globals()
    if listOfGlobals['logged']:
        listOfGlobals['logged'] = False
        listOfGlobals['loggedUser'] = False
        listOfGlobals['role'] = ''
    else:
        print("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
