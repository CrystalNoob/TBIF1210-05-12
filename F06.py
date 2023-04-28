def hitung_candi(data_candi): #untuk menghitung jumlah candi dan membuat agar jika jumlah cani >= 100, tetap berhasil, tetapi tidak
    #disimpan di dalam data
    banyak_candi = 0
    for i in range or i in range(1,101): 1
    if data_candi[i][1] != "": 
            banyak_candi += 1 
    return banyak_candi 


def bangun(username, id, batch, data_bahan, data_candi):
    #id berupa array yang berisi id yang telah dibuat untuk tiap jin
    #batch adalah variabel dari file batchbangun yang berfungsi dalam "for batch in range yang" untuk menunjukkan banyaknya jin
    #id dan batch igunakan dalam batch bangun

    import random as rd
    bahan_bangun_terpakai = [0,0,0]
    for i in range (1,4): #Data bahan bangunan hnya sampai 3
        if data_bahan[i][0] =="pasir":
            pasir = data_bahan[i][2] 
        elif data_bahan [i][0] == "batu" :
            batu = data_bahan [i][2]
        elif data_bahan[i][0] == "air" :
            air = data_bahan[i][2] 

    butuhpasir = rd.randint (1,5) #jumlah pasir yang diperlukan
    butuhbatu = rd.randint (1,5) #jumlah batu yang diperlukan
    butuhair = rd.randint (1,5) #jumlah air yang dibutuhkan
    bisa = False #menunjukkan apakah program bisa jalan
    banyak_candi = hitung_candi(data_candi) #Menghitung banyak candi di awal

    if (pasir >= butuhpasir) and (batu >= butuhbatu) and (air >= butuhair) :
        for j in range (1,4) :
            if data_bahan [j][0] == "pasir" :
                data_bahan [j][2] -= butuhpasir #untuk mengecek jumlah pasir yang tersedia
            elif data_bahan [j][0] == "batu" :
                data_bahan [j][2] -= butuhbatu 
            elif data_bahan [j][0] == "air" : 
                data_bahan [j][2] -= butuhair
        
        if (banyak_candi<100): 
            i = 1
            datakosong = False  #menentukan apakah data sudah terisi
            while datakosong == False :
                if data_candi [i][0] == 0 : 
                    if data_candi [i-1][0] == "id" : 
                        data_candi[i][0] = 1
                        data_candi [i][1] = username
                        data_candi [i][2] = butuhpasir 
                        data_candi [i][3] = butuhbatu
                        data_candi [i][4] = butuhair
                        datakosong = True
                    else : 
                        data_candi[i][0] = data_candi[i-1][0] + 1
                        data_candi [i][1] = username
                        data_candi [i][2] = butuhpasir 
                        data_candi [i][3] = butuhbatu
                        data_candi [i][4] = butuhair
                        datakosong = True 
                    id[batch] = data_candi[i][0]
                i +=1
        bisa = True
    else:  #bahan tidak cukup
        bisa = False

    if bisa:
        bahan_bangun_terpakai[0] += butuhpasir
        bahan_bangun_terpakai[1] += butuhair
        bahan_bangun_terpakai[2] += butuhbatu
    
    return [data_bahan, data_candi, bisa, id, bahan_bangun_terpakai] 



def hasil_bangun(hasil): #untuk melihat hasil outptdri fungsi
    bisa = hasil[2] 
    banyak_candi=hitung_candi(hasil[1])

    if bisa:
        print("Candi berhasil dibangun.")
        print("Sisa candi yang perlu dibangun: " + str(100-banyak_candi) +".")
    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi gagal dibangun")
    return hasil