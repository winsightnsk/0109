def vvod(subj: str) -> int:
    while True:
        userdata = input('Введите максимальное число": ')
        if not userdata.isdigit():
            print('Не корректный ввод...')
        elif int(userdata) < 1:
            print('Длина должна быть больше 0')
        else:
            return int(userdata)


max = vvod("")

# Создается список из значений от 0 до N включительно
primes = [i for i in range(max + 1)]

# Вторым элементом списка является единица, которую
# не считают простым числом. Забиваем ее нулем
primes[1] = 0

# Начинаем с 3-го элемента
i = 2
while i <= max:
    # Если значение текущей ячейки до этого не было обнулено,
    # значит в этой ячейке содержится простое число
    if primes[i] != 0:
        # Первое кратное ему будет в два раза больше
        j = i + i
        while j <= max:
            # и это число составное,
            # поэтому заменяем его нулем
            primes[j] = 0
            # переходим к следующему числу,
            # которое кратно i (оно на i больше)
            j = j + i
    i += 1

# Избавляемся от всех нулей в списке
primes = [i for i in primes if i != 0]

k = 1
for item in primes:
    ender = ', '
    if item < 10*k:
        prefix = ''
    else:
        prefix = '\n'
        k += 1
    if item == primes[-1]:
        ender = '.\n'
    print(f'{prefix}{item}', end=ender)
