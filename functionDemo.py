from random import randint


def factorial(num):
    """求阶乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


# m = int(input('m = '))
# n = int(input('n = '))
# # 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
# print(factorial(m) // factorial(n) // factorial(m - n))


def roll_dick(n=2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a+b+c


# print(roll_dick(n=2))
# print(add(c=50, a=12, b=24))


# 可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))


def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    return  x * y // gcd(x, y)

if __name__ == '_main_':
    number = 10 #全局变量