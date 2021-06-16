import os
import time
import random

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)

def main():
    content='北京欢迎你为你开天辟地……'
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content=content[1:]+content[0]

def main():
    print(generate_code())

def generate_code(code_len=4):
    all_chars='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos=len(all_chars)-1
    code=''
    for _ in range(code_len):
        index = random.randint(0,last_pos)
        code+=all_chars[index]
    return code

if __name__ == '__main__':
    main()

a=6
if a<5<8:
    print(a)
else:
    print(False)