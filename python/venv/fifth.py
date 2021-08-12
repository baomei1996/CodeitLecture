# 모듈

# import calculator as calc
from calculator import add, multiply

print(add(3, 4))
print(multiply(3, 4))

# standard library(표준 라이브러리)

import math

print(math.log10(100))
print(math.cos(0))
print(math.pi)

import random

print(random.random())
print(random.randint(3, 5)) # a <= N <= b 두 수 사이에 랜덤한 정수
print(random.uniform(3, 5)) # 두 수 사이에 랜덤한 소수

import os

print(os.getlogin())
print(os.getcwd()) # 경로

import datetime

pi_day = datetime.datetime(2020, 3, 14)
print(pi_day)
print(type(pi_day))

today = datetime.datetime.now()
print(today)
print(type(today))

today = datetime.datetime.now()

print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)
print(today.second)
print(today.microsecond)

print(today)
print(today.strftime("%A, %B, %dth, %Y")) # datetime 포맷팅


# input

name = input("이름을 입력하세요: ")
print(name)

x = int(input("숫자를 입력하세요: "))
print(x + 5)

num = random.randint(1, 20)
cnt = 4

while cnt > 0:
    a = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(cnt)))
    if a == num:
        cnt -= 1
        break
    elif a < num:
        print("Up")
    else:
        print("Down")
    cnt -= 1
if a == num:
    print("축하합니다. {}번 만에 숫자를 맞히셨습니다. ".format(4 - cnt))
else:
    print("아쉽습니다. 정답은 {}입니다.".format(num))
