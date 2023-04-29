import F01
import F02
import F03
import F04
import F06
import F08
import F10
import F12
import F13
import F14
import F15
import F16
from csv_arr_Converter import csvToArr
from pemrosesanArray import filterRole, init_arr, addToArr
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

# Filter array jin_candi
def filter_jinCandi(arr_candi):
    if (arr_candi[0] == 1):
        arrFilter = [0, []]
    else:
        temp_arr = [arr_candi[0], [["", 0] for i in range(arr_candi[0]-1)], 0]
        l = 0
        for i in range(arr_candi[0]):
            if (i != 0):
                isFound = False
                temp_username = arr_candi[2][i][1]
                count = 1
                for j in range(temp_arr[0]-1):
                    if (temp_arr[1][j][0] == temp_username):
                        isFound = True
                if not isFound:
                    for k in range(arr_candi[0]):
                        if (i != k and arr_candi[2][i][1] == arr_candi[2][k][1]):
                            count += 1
                    temp_arr[1][l][0] = temp_username
                    temp_arr[1][l][1] = count
                    temp_arr[2] += 1
                    l += 1
                        
    arrFilter = [temp_arr[2], [["", 0] for i in range(temp_arr[2])]]
    for i in range(arrFilter[0]):
            arrFilter[1][i][0] = temp_arr[1][i][0]
            arrFilter[1][i][1] = temp_arr[1][i][1]

    return arrFilter

# Filter Array id_candi
def filter_id(arr_candi):
    if (arr_candi[0] == 1):
        arr_id = [0, []]
    else:
        arr_id = [0, []]
        temp_id = 1
        for i in range(arr_candi[0]):
            if (i != 0):
                while (str(temp_id) != arr_candi[2][i][0]):
                    arr_id[1] = addToArr(0, arr_id[1], arr_id[0])
                    temp_id += 1
                    arr_id[0] += 1
                arr_id[1] = addToArr(temp_id, arr_id[1], arr_id[0])
                temp_id += 1
                arr_id[0] += 1
    return arr_id    
                
F13.load()

users = F13.arr_userCSV
candi = F13.arr_candiCSV
bahan_bangunan = F13.arr_bahan_bangunanCSV

jin_pengumpul = filterRole("jin_pengumpul", users)
jin_pembangun = filterRole("jin_pembangun", users)

id_candi = filter_id(candi)
jin_candi = filter_jinCandi(candi)

# Untuk Debugging
# print(users)
# print(candi)
# print(bahan_bangunan)

logged = False
loggedUser = ''
role = ''

# Infinite loop
while True:
    print(id_candi)
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
    elif cmd == 'hapusjin':
        F04.hapusjin(users, candi, jin_candi)
        users = F04.new_arr_user
        candi = F04.new_arr_candi
        jin_pengumpul = filterRole("jin_pengumpul", users)
        jin_pembangun = filterRole("jin_pembangun", users)
        id_candi = filter_id(candi)
        jin_candi = filter_jinCandi(candi)
        
    # elif cmd == 'hapusjin':
    #     F04.hapus_jin()
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
    elif cmd == 'ayamberkokok':
        F12.ayamberkokok(candi)
    elif cmd == 'save':
        F14.save(users, candi, bahan_bangunan)
    elif cmd == 'help':
        F15.help()
    elif cmd == 'exit':
        F16.exit(users, candi, bahan_bangunan)
    elif cmd == 'laporanjin' :
        laporanjin(jin_pengumpul, jin_pembangun, bahan_bangunan, candi, jin_candi)
        