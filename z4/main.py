subjects = []

child = dict()


def vvod(subj: str) -> int:
    while True:
        userdata = input(f'Введите оценку по "{subj}": ')
        if not userdata.isdigit():
            print('Не корректный ввод...')
        elif int(userdata) < 1:
            print('Максимальное число должно быть больше 0')
        else:
            return int(userdata)


while True:
    txt = input('Введите предмет: ')
    if not txt:
        break
    subjects.append(txt)

if len(subjects) > 0:
    while True:
        lname = input('Введите фамилию: ')
        if not lname:
            break
        fname = input('Введите имя: ')
        if not fname:
            break
        name = lname + ' ' + fname
        child[name] = dict()
        for subj in subjects:
            bal = vvod(subj)
            child[name][subj] = bal

print('\nПредметы\n', subjects)
print('\nУченики: ')
for key, value in child.items():
    print(key, ': ', value)

child_sr_bal = dict()

for name, data in child.items():
    sum = 0
    for n in data.values():
        sum += n
    child_sr_bal[name] = sum/len(subjects)

print('\nСредний балл по ученикам: ')
for key, value in child_sr_bal.items():
    print(f'{key}: {value:.2f}')

subj_sr_bal = dict()

print('\nСредний балл по предметам: ')
for s in subjects:
    x = 0
    for ch_data in child.values():
        x += ch_data[s]
    x /= len(child)
    print(f'Средний бал по "{s}": {x:.2f}')
