from functools import reduce
def normalize(name):
    w = [x.lower() for x in name]
    return w[0].upper() + ''.join(w[1:])

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


from functools import reduce

def prod(L):
    reduce(lambda x, y: x * y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456

def str2float(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(c):
        if c == '.':
            return 0
        return ord(c) - ord('0')

    s = s.replace('.', '')  # 去掉小数点
    return reduce(fn, map(char2num, s)) / (10 ** (len(s) - s.index('.')))