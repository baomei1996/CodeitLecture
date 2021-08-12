# for 반복문

my_list = [2, 3, 5, 7, 11]

for number in my_list:
    print(number)

# range 함수

# for i in renge(start, stop):
#   print(i)  start -> stop

for i in range(3, 11): # 3 ~ 10
    print(i)

for i in range(10):
    print(i) # 0 ~ 9

# range(start, stop, step)

for i in range(3, 17, 3):
    print(i)

# 사전 (dictionary)
# key-value pair (키-값 쌍)

my_dictionary = {
    5: 25, # key = 5 , value = 25
    2: 4,
    3: 9
}

print(type(my_dictionary))
print(my_dictionary[3])
my_dictionary[9] = 81
print(my_dictionary)

my_family = {
    '엄마': '김자옥',
    '아빠': '이석진',
    '아들': '이동민',
    '딸': '이지영'
}

print('이지영' in my_family.values())

for value in my_family.values():
    print(value)

print(my_family.keys())

for key in my_family.keys():
    value = my_family[key]
    print(key, value)

for key, value in my_family.items():
    print(key, value)


# 문자열과 리스트의 유사점

alphabet_string = 'ABCDEFGHIJ'

print(alphabet_string[0])
print(alphabet_string[1])
print(alphabet_string[4])
print(alphabet_string[-1])

print(alphabet_string[0:5])
print(alphabet_string[4:])
print(alphabet_string[:4]) # 리스트처럼 문자열이 출력

print(len(alphabet_string))

# 문자열과 리스트의 차이점
# 1. 문자열은 리스트와 달리 수정이 불가능

