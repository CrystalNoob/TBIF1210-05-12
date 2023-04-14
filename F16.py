import sys
import F14

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
        F14.save()
    else:
        sys.exit()
