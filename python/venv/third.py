x = 7
x = x + 1

print(x)

# = 같다의 의미가 아닌 지정 연산자

def hello():
    print("Hello")
    print("Welcome to Codeit!")


print("함수 호출 전")
hello()
print("함수 호출 후")
# return 의 역할 1. 함수를 즉시 종료시킴 2. 값을 되돌려줌

def square(x):
    return x * x
print("함수 호출 전")
print(square(3) + square(4))
print("함수 호출 후")

#scope : 변수가 사용 가는한 범위/ 지역변수 => 해당 범위 내에서만 / 글로벌 변수 => 전역 변수 함수 밖에서 정의한 변수
# 상수 (constant) 대문자
PI = 3.14 # 원주율 파이

def calculate_area(r):
    return PI * r * r

radius = 4 #반지름
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 6 #반지름
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 8 #반지름
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

# while 반복문
# while 조건구문 :
    # 수행 부분

i = 1
while i <= 3 :
    print("나는 잘생겼다!")
    i += 1

# if 반복문
# if 조건구문 :
    # 수행 부분

temperature = 8
if temperature <= 10:
    print("자켓을 입는다.")
else:
    print("자켓을 입지 않는다.")

# 리스트 list

numbers = [2, 4, 5, 7, 11, 13]
names = ["운수", "태호", "혜린", "영휸"]

# indexing

print(names[0])
print(numbers[1] + numbers[2])
print(numbers[-1]) # 뒤에서 첫번째
print(numbers[-2]) # 뒤에서 두번째

# list slicing
print(numbers[0:4])
print(numbers[2:])
print(numbers[:3])

new_list = numbers[0:3]
print(new_list)

numbers[0] = 7
print(numbers)
numbers[1] = numbers[2] + numbers[3]
print(numbers)

ages = []
ages.append(5)
ages.append(8)
print(len(ages))
print(ages)

num = [2, 4, 8, 12, 7, 15]
del num[3] # 삭제
print(num)
num.insert(4, 55) # 삽입 연산
print(num)

# 리스트 정렬
# sorted 기존의 리스트는 건드리지 않고 새로 정렬된 새로운 리스트를 리턴
new_num = sorted(num) # 오름차순
print(new_num)
new_num = sorted(num, reverse=True) # 뒤집어진 순서로 배티
print(new_num)
# sort 기존 리스트를 정렬
num2 = [2, 4, 8, 12, 7, 15]
num2.sort()
print(num2)
num2.sort(reverse=True)
print(num2)


