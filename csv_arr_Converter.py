from pemrosesanArray import nEff, init_arr, addToArr
from length_CSV import lenCsvCol, lenCsvRow

def csvToArr(file):
    # Spesifikasi :
    f = open(str(file), 'r')
    
    arr = [lenCsvRow(str(file)), lenCsvCol(str(file)), [init_arr(lenCsvCol(file)) for i in range(lenCsvRow(file))]]
    
    temp_string = ""
    line_index = 0
    for line in f:
        count_semicolon = 0
        for i in range(len(line)-1):    # -1 karena tidak memperhitungkan '\n'
            if line[i] != ';':
                temp_string += line[i]  # QnA Sintaks No. 31
                if (i == len(line)-2):
                    arr[2][line_index][count_semicolon] = temp_string
                    temp_string = ""
                    
            else:   # line[i] == ';' 
                    arr[2][line_index][count_semicolon] = temp_string
                    temp_string = ""
                    count_semicolon += 1
        line_index += 1          
    f.close()
    return arr

def arrToCsv(arr, file):
    f = open(file, 'w')
    
    for i in range(arr[0]): # arr[0] menyimpan nilai panjang baris
        line = ""
        for j in range(arr[1]): # arr[1] menyimpan nilai panjang kolom
            line += str(arr[2][i][j])   # arr[2][i][j] menyimpan nilai data pada baris ke-i dan kolom ke-j
            if (j != (arr[1]-1)):   # kalau j bukan indeks terakhir
                line += ';'
            else:   # j == arr[1]-1 kalau j indeks terakhir
                line += '\n'
        f.write(line)
    
    f.close()
