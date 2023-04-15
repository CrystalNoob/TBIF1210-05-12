# Variabel
header = "=========== HELP ==========="
LoggedText = "1. logout\n   Untuk keluar dari akun yang digunakan sekarang"

# Procedure
def help() -> None:
    print(header)
    if not logged:
        print("1. login\n   Untuk masuk menggunakan akun\n2. exit\n   Untuk keluar dari program dan kembali ke terminal")
    else:
        if role == "bandung_bondowoso":
            print(LoggedText)
        elif role == "roro_jonggrang":
            print ("1. ")
if __name__ == "__main__":
    logged = False
    role = "bandung_bondowoso"
    help()
