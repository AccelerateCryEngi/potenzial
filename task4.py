with open('astronaut_time.csv', encoding='utf-8') as f:
    a = [[y.strip() for y in x.split(',')] for x in f]
a.pop(0)
slovar = {}
for item in a:
    key = item[1]
    value = item[-1]
    if key in slovar:
        slovar[key] += int(value)
    else:
        slovar[key] = int(value)
print([key for key in slovar if slovar[key] == 9])