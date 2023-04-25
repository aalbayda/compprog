def solve():
    morse = {"A":"*-", "B":"-***", "C": "-*-*", "D":"-**", "E":"*", "F":"**-*","G":"--*","H":"****", "I": "**", "J": "*---", "K":"-*-", "L":"*-**", "M": "--", "N":"-*", "O": "---", "P": "*--*", "Q": "--*-", "R": "*-*", "S": "***", "T":"-","U":"**-","V":"***-","W":"*--","X":"-**-","Y":"-*--","Z":"--**","0":"-----","1":"*----","2":"**---","3":"***--", "4":"****-", "5":"*****", "6":"-****","7":"--***","8":"---**","9":"----*"}
    chars = 0
    word = list(input())
    for i in range(len(word)):
        if not word[i].isalnum():
            word[i] = " "
            chars += 1
            continue
        word[i] = morse[word[i].upper()]
    if len(word) == chars:
        return 0
    ans = "".join(word).replace(" ","")
    if ans == ans[::-1]:
        return 1
    return 0

print(solve())