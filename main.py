from csv_arr_Converter import csvToArr
from pemrosesanArray import filterRole

users = csvToArr("user.csv")
candi = csvToArr("candi.csv")
bahan_bangunan = csvToArr("bahan_bangunan.csv")

jin_pengumpul = filterRole("jin_pengumpul", users[2], users[0])
jin_pembangun = filterRole("jin_pembangun", users[2], users[0])