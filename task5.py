with open('astronaut_time.csv', encoding='utf-8') as f:
    a = [[y.strip() for y in x.split(',')] for x in f]
a.pop(0)
slovar = {}
for item in a:
    group = item[1].split('-')[0]
    if group not in slovar:
        slovar[group] = [[item[2]], [int(item[-1])]]
    else:
        slovar[group][0].append(item[2])
        slovar[group][1].append(int(item[-1]))
for key in slovar:
    slovar[key][1] = sum(slovar[key][1])/len(slovar[key][1])
    print(f'Номер группы: {key}. Каюты: {', '.join(slovar[key][0])}. Время простоя: {slovar[key][1]} ')