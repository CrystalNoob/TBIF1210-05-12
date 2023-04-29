import sys

def ayamberkokok(arr_candi) :
    # Spesifikasi : Kondisi yang menandakan saat pagi telah tiba.
    # Fungsi menerima intup array candi yang berisi id candi, jin  pembuat candi, pasir, batu, dan air yang dibutuhkan untuk membangun candi tersebut.
    if (int(arr_candi[0])-1 < 100) : # Kondisi jumlah candi yang telah dibangun kurang dari 100 candi
        print(f"Kukuruyuk.. Kukuruyuk..")
        print("Jumlah Candi:", (int(arr_candi[0])-1))
        print("Selamat, Roro Jonggrang memenangkan permainan! \n*Bandung Bondowoso angry noise* \nRoro Jonggrang dikutuk menjadi candi.")
    else : # Kondisi jumlah candi yang telah dibangun lebih besar dari 99 candi
        print(f"Kukuruyuk.. Kukuruyuk.. \nJumlah Candi: {(int(arr_candi[0]-1))} \nYah, Bandung Bondowoso memenangkan permainan!")
    sys.exit()
 

# Debugging
#arr_candi = [105,3,[["id","pembuat","pasir","air","batu"],[11,"joko",2,2,2],[22,"budi",3,3,3],[33,"zidan",4,4,4]]]
#ayamberkokok(arr_candi)