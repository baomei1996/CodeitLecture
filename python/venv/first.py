print('hello world')

# 코멘트

# 자료형 숫자(정수, 소수, 문자, 불린)

# 추상화 (변수, 함수, 객체)
#1. 변수
burger_price = 4990
fries_price = 1490
drink_price = 1250

print(burger_price)
print(burger_price * 2)
print(burger_price + fries_price)
print(burger_price * 3 + fries_price * 2 + drink_price  * 5)

def hello():
    print('hello!')
    print('welcome to Codeit!')

hello()
hello()
hello()

# 파라미터

def hello2(name):
    print('hello!')
    print(name)
    print('welcome to Codeit!')

hello2("Chris")

def print_sum(a, b, c):
    print(a + b + c)

print_sum(7, 3, 10)

#return문

def get_squere(x):
    return x * x

print(get_squere(3))

y = get_squere(2)
print(y)


