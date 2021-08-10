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
#================숫자형
# 덧셈
print(4 + 7)
# 뺄셈
print(2 - 4)
#곱셈
print(5 * 3)
#나머지
print(6 % 3)
#거듭제곱
print(2 ** 3)
#나눗셈
print(4 / 2)
# 소수 > 정수 하나라도 소수형이면 수수형으로 나옴 나눗셈은 항상 소수형으로 나옴
# 일반적인 사칙연산 법칙을 따름
print(2 * (2 + 3))

#floor division (버림 나눗셈)
print(7 // 2) #3.5 => 3
print(8.0 // 3) #2.666 => 2.0 둘중 하나가 소수형이면 소수형으로 출력
#round
print(round(3.1415926135, 2)) # 그냥 쓰면 소숫점 밑으로는 출력 x

# ==========문자형
print('hello ' * 3)
print("'I'm excited to learn Python!")
print("I\'m \"excited\" to learn Python!")
print("hello" + " world")
print("3" + "5")

#=========== 형변환

print(int(3.6))
print(float(2))
print(int("2") + int("5"))
print(float("2.5") + float("1.6"))
print(str(2) + str(5))
age = 7
print("제 나이는 " + str(age) + "살 입니다.")





