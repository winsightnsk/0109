import re
from pathlib import Path


math_str = '1+6*54-3/2+56-12*4'


def math_act(s: str) -> str:
    if s[0] == '-':
        x = '-'
        st = s[1:]
    else:
        x = ''
        st = s[0:]
    regex = re.compile(r'[/\+\*-]')
    regres = regex.search(st)
    s_arr = st.split(regres.group())
    a = float(x + s_arr[0])
    b = float(s_arr[1])
    if regres.group() == '/':
        return str(a/b)
    if regres.group() == '*':
        return str(a*b)
    if regres.group() == '+':
        return str(a+b)
    if regres.group() == '-':
        return str(a-b)


def math_skob(s: str) -> str:
    actions = [
        r'[\d\.]+[\*/]+[\d\.]+',
        r'-?[\d\.]+[\+-]+[\d\.]+'
    ]
    for action in actions:
        regex = re.compile(action)
        while regres := regex.search(s):
            s = re.sub(regex.pattern, math_act(regres.group()), s, 1)
    if re.match(r'\(-?\d+\.?\d*\)', s):
        return s[1:-1]
    return s


def math_formula(mstr: str) -> str:
    if len(mstr) < 1:
        return 'Пустая строка'
    mstr = mstr.replace(' ', '')
    xstr = re.sub(r'[0-9]|\*|/|\+|-|\.|\(|\)', '', mstr)
    if len(xstr) > 0:
        return f'Неопознанные сымволы: {xstr}'

    regex = re.compile(r'/0[\d\.]*')
    if regres := regex.search(mstr):
        dz = regres.group()
        regex = re.compile(r'[1-9]')
        regres = regex.search(dz)
        if not regres:
            return 'Деление на ноль'

    mstr = math_skob(mstr)
    return f' = {mstr}'


if __name__ == '__main__':
    regex = re.compile(r'.+\.\w+')
    namefile = input('Введите има файла: ')
    if not regex.search(namefile):
        namefile += '.txt'
    print(namefile)
    with open(Path(__file__).parents[0].joinpath(namefile), 'r') as f:
        formulas = f.readlines()
    for formula in formulas:
        f = re.sub(r'\n', '', formula)
        print(f, math_formula(f))
