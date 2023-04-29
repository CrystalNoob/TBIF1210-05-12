import F01
import F02
import F03
# import F04
import F06
import F08
import F10
import F13
import F14
import F15
import F16
from csv_arr_Converter import csvToArr
from pemrosesanArray import filterRole
from length_CSV import *
from F09 import laporanjin
# STRUKTUR ARRAY
# users = [lenRow, lenCol, [ [username, password, role], [username1, password1, role1], ... ] ]
# candi = [lenRow, lenCol, [ [id, pembuat, pasir, batu, air], [id1, pembuat1, pasir1, batu1, air1], ... ] ]
# bahan_bangunan = [lenRow, lenCol, [ [nama, deskripsi, jumlah], ["pasir", deskripsi_pasir, jumlah_pasir], ["batu", deskripsi_batu, jumlah_batu], ["air", deskripsi_air, jumlah_air] ] ]
    # ASUMSI bahan bangunan selalu berurut pasir, batu, lalu air.
# jin_pengumpul = [jml_jinPengumpul, [usernamePengumpul1, usernamePengumpul2, usernamePengumpul3, ... ] ]
# jin_pembangun = [jml_jinPembangun, [usernamePembangun, usernamePembangun2, usernamePembangun3, ... ] ]
# jin_candi = [jumlah_jin, [ [usernameJin1, JmlCandiJin1], [usernameJin2, JmlCandiJin2], ... ] ]
# id_candi = [n_eff, [1, 2, 3, 4, 5, 0, ... ] ]
    # angka 0 menunjukkan bahwa candi dihancurkan


F13.load()

users = F13.arr_userCSV
candi = F13.arr_candiCSV
bahan_bangunan = F13.arr_bahan_bangunanCSV
jin_candi = [0, []]
id_candi = [0, []]

# Untuk Debugging
# print(users)
# print(candi)
# print(bahan_bangunan)

logged = False
loggedUser = ''
role = ''

jin_pengumpul = filterRole("jin_pengumpul", users)
jin_pembangun = filterRole("jin_pembangun", users)

# Infinite loop
while True:
    # checker(input())
    cmd = input(">>> ")
    if cmd == 'login':
        F01.login(logged, users[2], users[0])
    elif cmd == 'logout':
        F02.logout()
    elif cmd == 'summonjin':
        F03.summonjin(jin_pengumpul, jin_pembangun, users)
        jin_pengumpul = F03.new_arr_pengumpul
        jin_pembangun = F03.new_arr_pembangun
        users = F03.new_arr_user
        print(jin_pembangun)
        print(jin_pengumpul)
        print(users)
    # elif cmd == 'hapusjin':
    #     F04.hapus_jin()
    elif cmd == 'batchbangun':
        F08.batchbangun(jin_pembangun,candi, id_candi, jin_candi, bahan_bangunan)
        id_candi = F08.new_arr_id
        jin_candi = F08.new_arr_jinCandi
        candi = F08.new_arr_candi
        bahan_bangunan = F08.new_arr_bahan_bangunan
        print(id_candi)
        print(jin_candi)
        print(candi)
        print(bahan_bangunan)
    elif cmd == 'laporancandi':
        F10.laporancandi(candi)
    elif cmd == 'save':
        F14.save(users, candi, bahan_bangunan)
    elif cmd == 'help':
        F15.help()
    elif cmd == 'exit':
        F16.exit(users, candi, bahan_bangunan)
    elif cmd == 'bangun':
        F06.bangun(False, "usernameJin1", id_candi, jin_candi, candi, bahan_bangunan)
        candi = F06.new_arr_candi
        id_candi = F06.new_arr_id
        jin_candi = F06.new_arr_jinCandi
        bahan_bangunan = F06.new_arr_bahan
        # Untuk Debugging:
        # print(candi)
        # print(id_candi)
        # print(jin_candi)
        # print(bahan_bangunan)
    elif cmd == 'laporanjin' :
        laporanjin(jin_pengumpul, jin_pembangun, bahan_bangunan, candi, jin_candi)
        