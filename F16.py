import sys
from F14 import save

# Constant
question = "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "

# Procedure
def isAnsValid(resp) -> bool:   # Cek apakah jawaban valid
    return resp in ('y', 'n')

def exit(arr_user, arr_candi, arr_bahan_bangunan) -> None:
    print(question, end='')
    ans = input().lower()       # Menghilangkan faktor huruf kapital
    while not isAnsValid(ans):  # Kasih ans ke fungsi cek
        print(question, end='') # Meminta input sampai jawabannya benar
        ans = input().lower()
    if ans == 'y':
        save(arr_user, arr_candi, arr_bahan_bangunan)                  # Save
        sys.exit()              # Exit program
    else:                       # Jika sudah sampai tahap ini, berarti jawaban pasti 'n'
        sys.exit()              # Exit program
