import F01
import F02
import F03
import F04
import F05
import F06
import F07
import F08
import F09
import F10
import F11
import F12
import F13
import F14
import F15
import F16
from csv_arr_Converter import csvToArr
from pemrosesanArray import filterRole, init_arr, addToArr
from length_CSV import *
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
        arr_id = [0,[]]
    else:
        idMax = int(arr_candi[2][1][0])
        # Mencari id terbesar
        for i in range(arr_candi[0]):
            if (i != 0):
                if(idMax < int(arr_candi[2][i][0])):
                    idMax = int(arr_candi[2][i][0])
                    
        # Inisialisasi array dengan panjang array sesuai dengan idMax           
        arr_id = [idMax, [0 for i in range(idMax)]]
        
        # Memperbarui arr_id dengan id yang ada pada candi, jika tidak ada id nya maka akan tetap nol
        for i in range(idMax):
            for j in range(arr_candi[0]):
                if (j != 0):
                    if (i+1 == int(arr_candi[2][j][0])):
                        arr_id[1][i] = int(arr_candi[2][j][0])          
    return arr_id    
                
F13.load()

# Deklarasi Variable
users = F13.arr_userCSV
candi = F13.arr_candiCSV
bahan_bangunan = F13.arr_bahan_bangunanCSV
jin_pengumpul = filterRole("jin_pengumpul", users)
jin_pembangun = filterRole("jin_pembangun", users)
id_candi = filter_id(candi)
jin_candi = filter_jinCandi(candi)

logged = False
loggedUser = ''
role = ''

# Infinite loop
while True:
    cmd = input(">>> ")
    
    if cmd == 'login':
        F01.login(loggedUser, role, logged, users[2], users[0])
        logged = F01.logged
        loggedUser = F01.userName
        role = F01.role
    elif cmd == 'logout':
        F02.logout(logged)
        role = F02.get_role
        logged = F02.get_logged
        loggedUser = F02.get_username
    elif cmd == 'save':
        F14.save(users, candi, bahan_bangunan)
    elif cmd == 'help':
        F15.help(role, logged)
    elif cmd == 'exit':
        F16.exit(users, candi, bahan_bangunan)
        
    if logged:
        if (role == 'bandung_bondowoso'):
            if cmd == 'summonjin':
                F03.summonjin(jin_pengumpul, jin_pembangun, users)
                jin_pengumpul = F03.new_arr_pengumpul
                jin_pembangun = F03.new_arr_pembangun
                users = F03.new_arr_user
            elif cmd == 'hapusjin':
                F04.hapusjin(users, candi, jin_candi)
                users = F04.new_arr_user
                candi = F04.new_arr_candi
                jin_pengumpul = filterRole("jin_pengumpul", users)
                jin_pembangun = filterRole("jin_pembangun", users)
                id_candi = filter_id(candi)
                jin_candi = filter_jinCandi(candi)
            elif cmd == 'ubahjin':
                F05.ubahjin(users)
                users = F05.new_arr_user
                jin_pengumpul = filterRole("jin_pengumpul", users)
                jin_pembangun = filterRole("jin_pembangun", users)
            elif cmd == 'batchbangun':
                F08.batchbangun(jin_pembangun,candi, id_candi, bahan_bangunan)
                candi = F08.new_arr_candi
                bahan_bangunan = F08.new_arr_bahan_bangunan
                jin_candi = filter_jinCandi(candi)
                id_candi = F08.new_arr_id
            elif cmd == 'batchkumpul':
                F08.batchkumpul(jin_pengumpul, bahan_bangunan)
                bahan_bangunan = F08.new_arr_bahan_bangunan_kumpul
            elif cmd == 'laporancandi':
                F10.laporancandi(candi)
            elif cmd == 'laporanjin' :
                F09.laporanjin(jin_pengumpul, jin_pembangun, bahan_bangunan, candi, jin_candi)
                
        elif (role == 'roro_jonggrang'):
            if cmd == 'hancurkancandi':
                F11.hancurkancandi(candi)
                candi = F11.new_arr_candi
                id_candi = filter_id(candi)
                jin_candi = filter_jinCandi(candi)      
            elif cmd == 'ayamberkokok':
                F12.ayamberkokok(candi)
                
        elif (role == 'jin_pengumpul'):
            if cmd == 'kumpul':
                F07.kumpul(False, bahan_bangunan)
                bahan_bangunan = F07.new_arr_bahan_bangunan        
        elif (role == 'jin_pembangun'):
            if cmd == 'bangun':
                F06.bangun(False, "usernameJin1", id_candi, candi, bahan_bangunan)
                candi = F06.new_arr_candi
                id_candi = F06.new_arr_id
                jin_candi = filter_jinCandi(candi)
                bahan_bangunan = F06.new_arr_bahan
