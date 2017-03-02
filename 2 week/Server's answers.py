import sys

ans200 = 0
ans300_309 = 0
others = 0
for strBase in sys.stdin:
    arr = strBase.split(' HTTP/1.1" ')
    strCur = ''
    if len(arr) == 1:
        strCur == arr[0]
    else:
        strCur = arr[1]
    num = strCur[0:3]
    if not num.isdigit():
        others += 1
    elif int(num) == 200:
        ans200 += 1
    elif 300 <= int(num) <= 309:
        ans300_309 += 1
    else:
        others += 1
print(ans200)
print(ans300_309)
print(others)
print(ans200 + ans300_309 + others)
