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




import random
import time


def download(filename):
    """下载文件"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')

    
def upload(filename):
    """上传文件"""
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')

    
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')


def record_time(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__}执行时间: {end_time - start_time:.2f}秒')
        return result
    
    return wrapper

@record_time
def download(filename):
    """下载文件"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


download('MySQL从删库到跑路.avi')



from functools import wraps

def record_time(func):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__}执行时间: {end_time - start_time:.2f}秒')
        return result
    
    return wrapper

@record_time
def download(filename):
    """下载文件"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


download('MySQL从删库到跑路.avi')

download.__wrapped__('Python从入门到住院.pdf')