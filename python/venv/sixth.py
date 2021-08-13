# 파일 읽기

with open('data/example.txt', 'r') as f:
    print(type(f))
    for line in f:
        print(line)


# strip 문자열에서 앞뒤로 있는 화이트스페이스를 제거 "", \t, \n
# 데이터 분석에 자주 쓰임

print("      abd      def     ".strip())

with open('data/example.txt', 'r') as f:
    print(type(f))
    for line in f:
        new_arr = (line.strip()).split(": ")
    print(new_arr[0])
    print(new_arr[1])

# split
my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split(". ")) # 보낸 문자열을 기준으로 문자를 나눔

full_name = "Kim, Yuna"
name_data = full_name.split(", ")
first_name = name_data[0]
last_name = name_data[1]

print("       \n\n    2    \t   3   \n  5  7  11  \n\n".split())

# 파일 쓰기
with open('data/new_file.txt', 'w') as sf: # a append 덮어쓰기가 아닌 추가를 하고자 한다면
    sf.write("Hello world!\n")
    sf.write("My name is Codeit.\n")

# with open('data/vocabulary.txt', 'a') as vc:
#    while True:
#        eng_word = input("영어 단어를 입력하세요: ")
#        if eng_word == 'q':
#            break
#        ko_word = input("한국어 뜻을 입력하세요: ")
#        if ko_word == 'q':
#            break
#        vc.write("{}: {}\n".format(eng_word, ko_word))

# with open('data/vocabulary.txt', 'r') as vcr:
#     for line in vcr:
#         new_quiz = line.strip().split(": ")
#         quiz = input("{}: ".format(new_quiz[1]))
#         answer = new_quiz[0]
#         if quiz == answer:
#             print("맞았습니다!")
#         else:
#             print("아쉽습니다. 정답은 {}입니다.".format(answer))


import random

# 사전 만들기
vocab = {}
with open('data/vocabulary.txt', 'r') as file:
    for line in file:
        data = line.strip().split(": ")

        english_word = data[0]
        korean_word = data[1]
        vocab[english_word] = korean_word

    keys = list(vocab.keys())

    while True:
        index = random.randint(0, len(keys) - 1)
        english_word = keys[index]
        korean_word = vocab[english_word]

        quess = input("{}: ".format(korean_word))

        if quess == 'q':
            break

        if quess == english_word:
            print('정답입니다!\n')
        else:
            print('아쉽습니다. 정답은 {}입니다.'.format(english_word))


            # Life is too short you need Python