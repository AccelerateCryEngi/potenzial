"""Задание 3"""
with open('new_time.txt', encoding='utf-8') as f:  # Открыть потокобезопасным образом
    while True:
        key = input()  # Получить код станции
        if key == 'stop':
            # Совершить прерывание и закрыть файл
            f.close()
            break
        else:
            f.seek(0)  # Поиск с начала файла
            for string in f:
                if string.split()[2] == key:
                    print(string)
                    break  # Не проверять остальное
            else:
                print('На этой станции все хорошо')  # Если ничего не найдено
