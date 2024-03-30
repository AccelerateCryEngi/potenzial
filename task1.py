with open('astronaut_time.csv', encoding='utf-8') as f:
    a = [[y.strip() for y in x.split(',')] for x in f.readlines()]
a.pop(0)
for item in a:
    numberStation = item[1]
    cabinNumber = item[2]
    timeStop = item[3]
    count = item[4]
    time = timeStop.split(':')
    time[0] = str((int(time[0])+int(count))%24)
    time = ':'.join('{:>02}'.format(x) for x in time)
    print(f'На станции {numberStation} в каюте {cabinNumber} восстановлено время. Актуальное время: {time}', file=open('new_time.txt', 'a', encoding='utf-8'))
with open('new_time.txt', encoding='utf-8') as f:
    for _ in range(3):
        print(f.readline(), end='')