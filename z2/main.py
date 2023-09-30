def get_fib_numbers(qty: int) -> int:
    fib = [0, 1]
    if qty < 0:
        raise Exception('количество элементов не может быть отрицательным')
    if qty < 3:
        return fib[:qty]
    for _ in range(2, qty):
        fib.append(fib[-1]+fib[-2])
    return fib


fib_numbers = get_fib_numbers(10)
assert len(fib_numbers) == 10
print(fib_numbers)
