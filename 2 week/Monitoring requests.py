file = open('input.txt', 'r')
lines = file.readlines()
file.close()
count = 0
for strBase in lines:
    if '"Go-http-client/1.1"' in strBase:
        count += 1
print(count)
