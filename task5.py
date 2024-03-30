"""Задание 5"""
with open('astronaut_time.csv', encoding='utf-8') as f:  # Открыть файл потокобезопасным образом
    a = [[y.strip() for y in x.split(',')] for x in f]  # Список списков без пробельных символов
a.pop(0)  # Удаление заголовка
slovar = {}
for item in a:
    group = item[1].split('-')[0]  # Получение номера группы (часть с цифрами)
    if group not in slovar:
        slovar[group] = [[item[2]], [int(item[-1])]]
    else:
        slovar[group][0].append(item[2])
        slovar[group][1].append(int(item[-1]))
for key in slovar:
    slovar[key][1] = sum(slovar[key][1])/len(slovar[key][1])  # Посчитать среднее значение
    print(f'Номер группы: {key}. Каюты: {', '.join(slovar[key][0])}. Время простоя: {slovar[key][1]} ')  # И сразу же вывести