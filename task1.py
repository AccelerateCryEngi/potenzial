"""Задание 1"""
with open('astronaut_time.csv', encoding='utf-8') as f:
    a = [[y.strip() for y in x.split(',')] for x in f.readlines()]  # Создание списка списков с удалением символов новой строки
a.pop(0)  # Удаление заголовка
for item in a:
    numberStation = item[1]
    cabinNumber = item[2]
    timeStop = item[3]
    count = item[4]
    time = timeStop.split(':')  # Необходимо извлечь часы из времени
    time[0] = str((int(time[0])+int(count))%24)  # Добавление простоя ко времени с учетом того, что в сутках 24 часа
    time = ':'.join('{:>02}'.format(x) for x in time)  # Форматирование с учетом того, что минимальное количество знаков для часов, минут, секунд - два
    print(f'На станции {numberStation} в каюте {cabinNumber} восстановлено время. Актуальное время: {time}',
          file=open('new_time.txt', 'a', encoding='utf-8'))  # Добавление записей в файл
with open('new_time.txt', encoding='utf-8') as f:
    for _ in range(3):
        print(f.readline(), end='')