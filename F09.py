def jinTerajin(arr_jin, arr_candi):
    # Spesifikasi : mengetahui siapa username jin terajin (paling banyak membuat candi).
    # Jika terdapat lebih dari 1 jin terajin, tampilkan username jin dengan urutan leksikografis terendah (contoh: Malik dan Akbar → pilih Akbar).
    # Menerima masukan array yang berisi username jin pembangun dan array yang berisi data candi yang telah dibangun.
    if (int(arr_jin[0]) == 0):
        return "-"  # Kalau tidak ada jin pembangun, tampilkan "-"
    else:   # (int(arr_jin[0]) != 0) Jin pembangun > 0
        tabJin = [ [arr_jin[1][i], "0"] for i in range(int(arr_jin[0])) ]   # Inisialisas array [ [username_jin1, jmlCandiDibangunJin1] , [username_jin2, jmlCandiDibangunJin2] , ... ]
        for i in range(int(arr_candi[0])):  # Looping array yang berisi data candi
            for j in range(int(arr_jin[0])):    # Looping array yang berisi username candi pembangun
                if (tabJin[j][0] == arr_candi[2][i][1]):    # Kalau username jin pembangun pada array jin pembangun = username jin pembangun pada array candi
                    tabJin[j][1] = str(int(tabJin[j][1]) + 1)   # Jumlah candi yang dibangun oleh username jin tersebut ditambah 1
        jin_terajin = tabJin[0][0]  # Inisialisasi jin terajin dimisalkan username jin pertama pada array tabJin
        jml_candi = int(tabJin[0][1])   # Inisalisasi jumlah candi terbanyak yang dibangun 
        for i in range(int(arr_jin[0])): # Looping pada array tabJin dengan panjang array sama seperti panjang array yang berisi username jin
            if (int(tabJin[i][1]) > jml_candi) or (int(tabJin[i][1]) == jml_candi and tabJin[i][0] < jin_terajin):  # Kalau (jumlah candi yang dibangun > jumlah candi terbanyak sementara) atau (jumlah candi yang dibangun = jumlah candi terbanyak sementara dan urutan leksikografisnya lebih kecil)
                jin_terajin = tabJin[i][0]  # Update username jin terajin
                jml_candi = int(tabJin[i][1])   # Update jumlah candi terbanyak sementara
        return jin_terajin  # Menghasilkan username jin terajin (yang paling banyak membuat candi)
    
def jinTermalas(arr_jin, arr_candi):
    # Spesifikasi : mengetahui siapa username jin termalas (paling sedikit membuat candi).
    # Jika terdapat lebih dari 1 jin termalas, tampilkan username jin dengan urutan leksikografis tertinggi (contoh: Hashemi dan Rafsanjani → pilih Rafsanjani).
    # Menerima masukan array yang berisi username jin pembangun dan array yang berisi data candi yang telah dibangun.
    if (int(arr_jin[0]) == 0):
        return "-"  # Kalau tidak ada jin pembangun, tampilkan "-"
    else:   # (int(arr_jin[0]) != 0) Jin pembangun > 0
        tabJin = [ [arr_jin[1][i], "0"] for i in range(int(arr_jin[0])) ]   # Inisialisas array [ [username_jin1, jmlCandiDibangunJin1] , [username_jin2, jmlCandiDibangunJin2] , ... ]
        for i in range(int(arr_candi[0])):  # Looping array yang berisi data candi
            for j in range(int(arr_jin[0])):    # Looping array yang berisi username candi pembangun
                if (tabJin[j][0] == arr_candi[2][i][1]):    # Kalau username jin pembangun pada array jin pembangun = username jin pembangun pada array candi
                    tabJin[j][1] = str(int(tabJin[j][1]) + 1)   # Jumlah candi yang dibangun oleh username jin tersebut ditambah 1
        jin_termalas = tabJin[0][0] # Inisialisasi jin termalas dimisalkan username jin pertama pada array tabJin
        jml_candi = int(tabJin[0][1])   # Update jumlah candi tersedikit sementara
        for i in range(int(arr_jin[0])):    # Looping pada array tabJin dengan panjang array sama seperti panjang array yang berisi username jin
            if (int(tabJin[i][1]) < jml_candi) or (int(tabJin[i][1]) == jml_candi and tabJin[i][0] > jin_termalas): # Kalau (jumlah candi yang dibangun < jumlah candi tersedikit sementara) atau (jumlah candi yang dibangun = jumlah candi terbanyak sementara dan urutan leksikografisnya lebih besar)
                jin_termalas = tabJin[i][0] # Update username jin termalas
                jml_candi = int(tabJin[i][1])   # Update jumlah candi tersedikit sementara
        return jin_termalas # Menghasilkan username jin termalas (yang paling sedikit membuat candi)
    

def laporanjin(arr_pengumpul, arr_pembangun, arr_bahan, arr_candi):
    # Mengetahui berapa jumlah jin per tipe dan jumlah jin total.
    print("> Total Jin:", int(arr_pengumpul[0]) + int(arr_pembangun[0]))
    print("> Total Jin Pengumpul:", arr_pengumpul[0])
    print("> Total Jin Pembangun:", arr_pembangun[0])
    # Mengetahui siapa username jin terajin (paling banyak membuat candi).
    print("> Jin Terajin:", jinTerajin(arr_pembangun, arr_candi))
    # Mengetahui siapa username jin termalas (paling sedikit membuat candi).
    print("> Jin Termalas:", jinTermalas(arr_pembangun, arr_candi))
    # Melihat berapa banyak material saat ini untuk melihat mungkin tidaknya melakukan batch bangun.
    print("> Jumlah Pasir:", arr_bahan[2][1][2], "unit")
    print("> Jumlah Air:", arr_bahan[2][2][2], "unit")
    print("> Jumlah Batu:", arr_bahan[2][3][2], "unit")
    