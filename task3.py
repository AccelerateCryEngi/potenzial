with open('new_time.txt', encoding='utf-8') as f:
    a = [x.split() for x in f]
slovar = {item[2]: item for item in a}
while True:
    key = input()
    if key == 'stop':
        break
    elif key not in slovar:
        print('На этой станции все хорошо')
    else:
        print(' '.join(slovar[key]))