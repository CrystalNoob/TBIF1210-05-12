import F1
import F2
import F13
from F13 import load
import F14
import F15
import F16
from csv_arr_Converter import csvToArr
from pemrosesanArray import filterRole
from length_CSV import *
from F09 import laporanjin
load()
# users = csvToArr("user.csv")
# candi = csvToArr("candi.csv")
# bahan_bangunan = csvToArr("bahan_bangunan.csv")
users = F13.arr_userCSV
candi = F13.arr_candiCSV
bahan_bangunan = F13.arr_bahan_bangunanCSV

# Untuk Debugging
print(users)
print(candi)
print(bahan_bangunan)

# NMax = lenCsvRow("user.csv")    # Limit
logged = False
loggedUser = ''
role = ''

jin_pengumpul = filterRole("jin_pengumpul", users)
jin_pembangun = filterRole("jin_pembangun", users)

# # Testing Laporan Jin: (diuncomment aja kl mau dites)
# laporanjin(jin_pengumpul, jin_pembangun, bahan_bangunan, candi)

# Command checker
def checker(cmd):
    if cmd == 'login':
        F1.login(logged, users, NMax)
    elif cmd == 'logout':
        F2.logout()
    elif cmd == 'help':
        F15.help(logged, role)
    elif cmd == 'exit':
        F16.exit(users, candi, bahan_bangunan)

print('>>>', end=' ')
# Infinite loop
while True:
    checker(input())
    print('>>>', end=' ')
