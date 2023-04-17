def lenCsvCol(file):   
    # Spesifikasi : Mengitung panjang kolom dari data csv. Input berupa string dan output berupa integer.
    # KAMUS LOKAL
    # count_semicolon, i : integer
    # ALGORITMA
    f = open(file, 'r')
    count_semicolon = 0
    line = f.readline()
    for i in range(len(line)):
        if (line[i] == ';'):
            count_semicolon += 1
    f.close()
    return count_semicolon + 1


def lenCsvRow(file):
    # Spesifikasi : 
    # KAMUS LOKAL
    # count_data : integer
    # line : string
    # ALGORITMA
    f = open(str(file), 'r')
    count_line = 0
    for line in f:
        count_line += 1
    f.close()
    return count_line
