# Constant
header = "=========== HELP ==========="
LoggedText = "1. logout\n   Untuk keluar dari akun yang digunakan sekarang"

# Procedure
def help(logged = bool(), role = str()) -> None:
    print(header)
    if not logged:
        print("1. login\n   Untuk masuk menggunakan akun\n2. exit\n   Untuk keluar dari program dan kembali ke terminal")
    else:
        if role == "bandung_bondowoso":
            print(LoggedText)
        elif role == "roro_jonggrang":
            print (LoggedText)
