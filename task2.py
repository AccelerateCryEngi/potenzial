with open('new_time.txt', encoding='utf-8') as f:
    a = [x.split() for x in f]
print(a[:20])
a.sort(key=lambda item: item[5].split('-')[1])
for i in range(3):
    print(' '.join(a[i]))

# добавить сортировку
