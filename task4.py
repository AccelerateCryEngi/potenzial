"""Задание 4"""
with open('astronaut_time.csv', encoding='utf-8') as f:  # Открыть потокобезопасным образом
    a = [[y.strip() for y in x.split(',')] for x in f]  # Список списков без пробельных символов
a.pop(0)  # Удаление заголовка
slovar = {}
for item in a:
    key = item[1]  # Номер станции
    value = item[-1]  # Время простоя
    if key in slovar:
        slovar[key] += int(value)
    else:
        slovar[key] = int(value)

b = [key for key in slovar if slovar[key] == 9]
print(b)
with open('station_max_downtime.csv', 'w') as f:
    f.write(','.join(b))