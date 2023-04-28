# Constant
HEADER = "====================     HELP    ===================="
LOGGED_TEXT = "\
 1. help\n    Untuk melihat pesan yang sedang Anda baca sekarang\n\
 2. logout\n    Untuk keluar dari akun yang digunakan sekarang\n\
 3. save\n    Untuk menyimpan permainan\n\
 4. exit\n    Untuk keluar dari permainan dan kembali ke terminal"

# Global variable
logged = bool()
role = ''

# Get-Help Procedure
def help() -> None:
    print(HEADER)
    if not logged:      # Not logged state
        print(" 1. login\n    Untuk masuk menggunakan akun\n 2. exit\n    Untuk keluar dari permainan dan kembali ke terminal")
    else:       # ASUMSI ROLE SELALU BENAR
        if role == "bandung_bondowoso":         # Self-explanatory
            print(LOGGED_TEXT)
            print(" 5. summonjin\n    Untuk memanggil jin dari dunia lain")
            print(" 6. hapusjin\n    Untuk menghapus jin [Peringatan: candi yang telah dibuat oleh jin tersebut juga ikut terhapus]")
            print(" 7. ubahjin\n    Untuk mengubah tipe jin")
            print(" 8. batchkumpul\n    Untuk memerintahkan seluruh jin pengumpul untuk mengumpulkan bahan")
            print(" 9. batchbangun\n    Untuk memerintahkan seluruh jin pembangun untuk membangun candi")
            print("10. laporanjin\n    Untuk mengetahui kinerja para jin")
            print("11. laporancandi\n    Untuk mengetahui perkembangan pembangunan candi")
        elif role == "roro_jonggrang":
            print (LOGGED_TEXT)
            print(" 5. hancurkancandi\n    Untuk menghancurkan candi yang tersedia")
            print(" 6. ayamberkokok\n    Untuk menyelesaikan permainan dan keluar dari permainan")
        elif role == "jin_pengumpul":
            print(LOGGED_TEXT)
            print(" 7. kumpul\n    Untuk mengumpulkan bahan bangunan candi")
        elif role == "jin_pembangun":
            print(LOGGED_TEXT)
            print(" 7. bangun\n    Untuk membangun candi")

# Debug & Testing [Passed]
# if __name__ == "__main__":
#     logged = True
#     role = 'bandung_bondowoso'
#     help()
