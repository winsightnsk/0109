from utils import txtfile
import string
import re

with open(txtfile, "r", encoding='cp1251') as f:
    txt = f.read()
txt_len = len(txt)
txt_low = txt.lower()

simb_arr = ''.join([chr(s) for s in range(ord('А'), ord('я')+1)])
simb_skip = [chr(s) for s in range(ord('A'), ord('z')+1)]
for ch in string.printable:
    if ch not in simb_skip:
        simb_arr += ch

simb_dict = dict()

for ch in txt:
    if simb_arr.find(ch) >= 0:
        simb_dict[ch] = simb_dict.get(ch, 0) + 1

print('Статистика: \n')
for key, val in simb_dict.items():
    print(key, ' : ', '{:.3f}'.format(val/txt_len))

stxt = txt.split('.')

andrey = []
for pr in stxt:
    if re.fullmatch(r'^ .*Андре[й|я|ю|ем].*', pr):
        andrey.append(pr+'.')
        if len(andrey) >= 10:
            break

for i, item in enumerate(andrey):
    print(i+1, ":", item)
