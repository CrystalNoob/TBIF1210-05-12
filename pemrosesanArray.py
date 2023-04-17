def nEff(raw_arr, raw_N):
    n_eff = 0
    for i in range(raw_N):
        if (raw_arr != ''):
            n_eff += 1
    return n_eff

def init_arr(n):
    return ['' for i in range(n)]
    
def addToArr(x, arr, n_eff):
    new_arr = init_arr(n_eff+1)
    for i in range(n_eff):
        new_arr[i] = arr[i]
    new_arr[n_eff] = x
    return new_arr