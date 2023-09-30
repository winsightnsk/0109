def vvod(subj: str) -> int:
    while True:
        userdata = input(f'Введите длину "{subj}": ')
        if not userdata.isdigit():
            print('Не корректный ввод...')
        elif int(userdata) < 1:
            print('Длина должна быть больше 0')
        else:
            return int(userdata)


t = ['A', 'B', 'C']

for i, tdata in enumerate(t):
    t[i] = vvod(tdata)

assert max(t) < sum(t) - max(t)

p = sum(t)/2
area = (p*(p-t[0])*(p-t[1])*(p-t[2])) ** 0.5
print('Площадь треугольника = %0.3f' % area)
