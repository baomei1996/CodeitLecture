#======== format 을 이용한 문자영 포맷팅

# 오늘은 2019년 10월 29일입니다.
year = 2019
month = 10
day = 29

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일입니다.")
date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day))
print("저는 {1}, {0}, {2}를 좋아합니다.".format("박지성", "유재석", "백종원"))
num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1 / num_2))

# ======== 불대수
#
# 대한민국의 수도는 서울이다. => 참인 명제
# 2는 1보다 작다 => 거짓인 명제
# 한국의 수도는 어디입니까? => 명제가 아님
# 김태희는 이쁘다. => 명제가 아님
# x and y
print(True and True)# 참 참 => 참
print(True and False)# 참 거짓 => 거짓
print(False and True)# 거짓 참 => 거짓
print(False and False)# 거짓 거짓 => 거짓
# x or y
print(True or True)# 참 참 => 참
print(True or False)# 참 거짓 => 참
print(False or True)# 거짓 참 => 참
print(False or False)# 거짓 거짓 => 거짓
# not 연산
print(not True)# 참 => 거짓
print(not False)# 거짓 => 참
# ========= 불린형
print(True)
print(False)
print(2 > 1)
print(2 < 1)
print(3 >= 2)
print(3 <= 2)
print(2 == 2)
print(2 != 2)

print("Hello" == "Hello")
print("Hello" != "Hello")
x = 3
print(x > 4 or not (x < 2 or x == 3)) # False or False => False


# ========= type 함수
print(type(3))
print(type(3.0))
print(type("3"))
print(type(True))

def hello():
    print("Hello world")

print(type(hello))