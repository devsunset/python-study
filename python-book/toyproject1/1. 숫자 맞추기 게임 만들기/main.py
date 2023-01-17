import random

# 0.0 ~ 0.999999 사이의 실수 반환
print(random.random())
# random.uniform(a,b)  a, b 사이의 실수 값을 반환
print(random.uniform(1,10))
# random.randint(a,b)  a, b 사이의 정수 값을 반환
print(random.randint(1,10))
# random.randrange(a,b)  a, b 사이의 정수 값을 반환
print(random.randrange(1,10))
# random.randrange(a)  인자 하나일 경우 0~a 사이의 정수 값 반환
print(random.randrange(10))
# random.choice(type) type에는 문자열, 리스트, 튜플 , range의 값을 입력받을 수 있고 무작위로 하나의 원소 반환
print(random.choice([1,2,3,4,5]))

random_number = random.randint(1, 100)
#print(random_number)

game_count = 1

while True:
    try:
        my_number = int(input("1~100 사이의 숫자를 입력하세요:"))
        
        if my_number > random_number:
            print("다운")
        elif my_number < random_number:
            print("업")
        elif my_number == random_number:
            print(f"축하합니다.{game_count}회 만에 맞췄습니다")
            break
        
        game_count = game_count + 1
    except:
        print("에러가 발생하였습니다. 숫자를 입력하세요")