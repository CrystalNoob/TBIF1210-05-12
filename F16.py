import sys
from F14 import save

# Variable
question = "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "

# Procedure
def isAnsValid(resp) -> bool:
    return resp in ('y', 'n')

def exit() -> None:
    print(question, end='')
    ans = input().lower()
    while not isAnsValid(ans):
        print(question, end='')
        ans = input().lower()
    if ans == 'y':
        save()
    else:
        sys.exit()
