def nEff(raw_arr, raw_N) -> int:
    n_eff = 0
    for i in range(raw_N):
        if (raw_arr != ''):
            n_eff += 1
    return n_eff

def init_arr(n) -> list:
    return ['' for i in range(n)]
    
def addToArr(x, arr, n_eff) -> list:
    new_arr = init_arr(n_eff+1)
    if (n_eff == 0):
        new_arr[n_eff] = x 
    else:
        for i in range(n_eff):
            new_arr[i] = arr[i]
        new_arr[n_eff] = x
    return new_arr

def deleteFromArr(x, arr, n_eff):
    new_arr = init_arr(n_eff-1)
    j = 0
    for i in range(n_eff):
        if (x != arr[i]):
            new_arr[j] = arr[i]
            j += 1
    return new_arr

def filterRole(role, arr) -> list:
    n_eff = int(arr[0])
    if (n_eff == 0):
        return [0, []]
    len_newArr = 0
    newArr = []
    for i in range(n_eff):
        if (arr[2][i][2] == role):
            newArr = addToArr(arr[2][i][0], newArr, len_newArr)
            len_newArr += 1
    return [len_newArr, newArr]
            
    
