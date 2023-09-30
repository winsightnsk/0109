import os

codecs = [
    "cp1252",
    "cp1251",
    "cp437",
    "utf-16be",
    "utf-16",
    "ascii",
]

dirname, filename = os.path.split(os.path.abspath(__file__))
txtfile = os.path.join(dirname, 'war_and_peace.txt')

if __name__ == '__main__':
    for codec in codecs:
        try:
            with open(txtfile, "r", encoding=codec) as f:
                print(f.readline())
                print(codec)
        except UnicodeError:
            ...
