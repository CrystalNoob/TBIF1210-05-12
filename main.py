import F1
import F2
import F14
import F15
import F16
from csv_arr_Converter import csvToArr
from pemrosesanArray import filterRole
from length_CSV import *

users = csvToArr("user.csv")
candi = csvToArr("candi.csv")
bahan_bangunan = csvToArr("bahan_bangunan.csv")
NMax = lenCsvRow("user.csv")    # Limit
logged = False
loggedUser = ''
role = ''

jin_pengumpul = filterRole("jin_pengumpul", users[2], users[0])
jin_pembangun = filterRole("jin_pembangun", users[2], users[0])

# Command checker
def checker(cmd):
    if cmd == 'login':
        F1.login(logged, users, NMax)
    elif cmd == 'logout':
        F2.logout()
    elif cmd == 'help':
        F15.help(logged, role)
    elif cmd == 'exit':
        F16.exit()

print('>>>', end=' ')
# Infinite loop
while True:
    checker(input())
    print('>>>', end=' ')
