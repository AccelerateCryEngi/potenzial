"""Задание 2"""
with open('new_time.txt', encoding='utf-8') as f:  # потокобезопасно
    a = [x.split() for x in f]  # Список списков

slovar = {item[2]: item for item in a}  # Ключи - номера станций, значения - данные станции
keys = list(slovar.keys())  # Ключи будут сортироваться

def greaterThan(a, b):
    """Сравнивает абсолютные значения таблицы ASCII двух цепочек из трех символов и возвращает булево значение
    a: первый символ (если он больше, вернуть True)
    b: второй символ (если он больше, вернуть False
    """
    for i in range(3):
        if ord(a[i]) < ord(b[i]):
            return False
    else:
        return True  # Если не было выхода из функции по return

for i in range(len(keys)):
    for k in range(i-1, -1, -1):  # Сортировка вставками. Берем символ и сравниваем с предыдущими
        if greaterThan(keys[i], keys[k]):  # Если искомый символ больше предыдущего
            keys[i], keys[k] = keys[k], keys[i]  # Меняем местами

for i in range(3):  # Вывести первые три символа
    item = slovar[keys[i]]
    print(' '.join(item))