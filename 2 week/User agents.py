def ultra_helix_sun_split(strstr):
    is_needed_split = True
    index = 0
    result = []
    for i, el in enumerate(strstr):
        if el == ' ' and is_needed_split:
            result.append(strstr[index:i])
            index = i + 1
        if el == '"' or el == '[' or el == ']':
            is_needed_split = not is_needed_split
    result.append(strstr[index:])
    return result


systems = {'Windows': 0, 'OS X': 0, 'Ubuntu': 0, 'Unknown': 0}

file = open('input.txt', 'r')
lines = file.readlines()
file.close()
for line in lines:
    s = ultra_helix_sun_split(line)
    flag = False
    if 'Windows' in s[8]:
        systems['Windows'] += 1
        flag = True
    if 'Macintosh' in s[8]:
        systems['OS X'] += 1
        flag = True
    if 'Ubuntu' in s[8]:
        systems['Ubuntu'] += 1
        flag = True
    if not flag:
        systems['Unknown'] += 1
for k, v in sorted(systems.items(), key=lambda x: x[1]):
    print(k + ": ", v)
