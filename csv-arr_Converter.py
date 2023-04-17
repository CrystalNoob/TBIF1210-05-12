from pemrosesanArray import nEff, init_arr, addToArr
from length_CSV import lenCsvCol, lenCsvRow

def csvToArr(file):
    # Spesifikasi :
    f = open(str(file), 'r')
    
    arr = [init_arr(lenCsvCol(file)) for i in range(lenCsvRow(file))]
    
    temp_string = ""
    line_index = 0
    for line in f:
        count_semicolon = 0
        for i in range(len(line)-1):    # -1 karena tidak memperhitungkan '\n'
            if line[i] != ';':
                temp_string += line[i]  # QnA Sintaks No. 31
                if (i == len(line)-2):
                    arr[line_index][count_semicolon] = temp_string
                    temp_string = ""
                    
            else:   # line[i] == ';' 
                    arr[line_index][count_semicolon] = temp_string
                    temp_string = ""
                    count_semicolon += 1; 
        line_index += 1          
    f.close()
    return arr

def arrToCsv(arr, file):
    f = open(str(file), 'w')


