def yfizzbuzz(max: int):
    n = 1
    while n <= max:
        if n % 3 == 0 and n % 5 == 0:
            yield 'FizzBuzz'
        elif n % 3 == 0:
            yield 'Fizz'
        elif n % 5 == 0:
            yield 'Buzz'
        else:
            yield n
        n += 1


while True:
    userdata = input('Введите максимальное число: ')
    if not userdata.isdigit():
        print('Не корректный ввод...')
    elif int(userdata) < 2:
        print('Максимальное число должно быть больше 1')
    else:
        break

fizzbuzz = yfizzbuzz(int(userdata))

for item in fizzbuzz:
    print(item)
