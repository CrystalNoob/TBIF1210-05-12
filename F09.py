def jinTerajin(arr_jin, arr_candi, n_eff):
    if (int(n_eff) == 0):
        return "-"
    else:
        tabJin = [ [arr_jin[i], "0"] for i in range(int(n_eff)) ]
        for i in range(int(arr_candi[0])):
            for j in range(int(n_eff)):
                if (tabJin[j][0] == arr_candi[2][i][1]):
                    tabJin[j][1] = str(int(tabJin[j][1]) + 1)
        jin_terajin = tabJin[0][0]
        jml_candi = int(tabJin[0][1])
        for i in range(int(n_eff)):
            if (int(tabJin[i][1]) > jml_candi) or (int(tabJin[i][1]) == jml_candi and tabJin[i][0] < jin_terajin):
                jin_terajin = tabJin[i][0]
                jml_candi = int(tabJin[i][1])
        return jin_terajin
    
def jinTermalas(arr_jin, arr_candi, n_eff):
    if (int(n_eff) == 0):
        return "-"
    else:
        tabJin = [ [arr_jin[i], "0"] for i in range(int(n_eff)) ]
        for i in range(int(arr_candi[0])):
            for j in range(int(n_eff)):
                if (tabJin[j][0] == arr_candi[2][i][1]):
                    tabJin[j][1] = str(int(tabJin[j][1]) + 1)
        jin_termalas = tabJin[0][0]
        jml_candi = int(tabJin[0][1])
        for i in range(int(n_eff)):
            if (int(tabJin[i][1]) < jml_candi) or (int(tabJin[i][1]) == jml_candi and tabJin[i][0] > jin_termalas):
                jin_termalas = tabJin[i][0]
                jml_candi = int(tabJin[i][1])
        return jin_termalas
    

def laporanjin(arr_pengumpul, n_pengumpul, arr_pembangun, n_pembangun, arr_bahan, arr_candi):
    print("> Total Jin:", int(n_pengumpul) + int(n_pembangun))
    print("> Total Jin Pengumpul:", n_pengumpul)
    print("> Total Jin Pembangun:", n_pembangun)
    print("> Jin Terajin:", jinTerajin(arr_pembangun, arr_candi, n_pembangun))
    print("> Jin Termalas:", jinTermalas(arr_pembangun, arr_candi, n_pembangun))
    print("> Jumlah Pasir:", arr_bahan[2][1][2], "unit")
    print("> Jumlah Air:", arr_bahan[2][2][2], "unit")
    print("> Jumlah Batu:", arr_bahan[2][3][2], "unit")
    