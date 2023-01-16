# 1.print
print('1.--------------------------')
print("Hello World")
print('hello')
print('hello 안녕하세요')
print('안녕','하세요','반갑습니다')
print('안녕'+'하세요'+'반갑습니다')
print("""안녕하세요
오늘은 날씨가 좋네요""")
print('''안녕하세요
오늘은 날씨가 좋네요''')
print("안녕하세요"\
      "오늘은 날씨가 좋네요")
a = 123
b = "안녕하세요"
print("a값:{} b값:{}".format(a,b))
print(f"a값:{a} b값:{b}")

# 2.input
print('2.--------------------------')
# text = input()
# print(text)

# 3.변수 - 숫자형, 문자형, 소수점형, BOOL형
print('3.--------------------------')
i = 1
j = 2
k = 1+2
print(k)
l = '3'
print(k+int(l))
print(str(k)+l)
e = 3.14
f = 10
print(e+f)
print(i+j)
print(float(i)+float(j))
a_bool = True
b_bool = False
a_int = 1
b_int = 0
print(a_bool)
print(b_bool)
print(type(a_bool))
print(type(b_bool))
print(a_int)
print(b_int)
print(type(a_int))
print(type(b_int))

# 4.자료형 - 리스트, 튜플, 딕셔너리, 집합
print('4.--------------------------')
print('List')
a_list = [1,2,3,4,5]
print(a_list)
print(a_list[0])
print(a_list[1])
print(a_list[:2])
print(a_list[2:])
b_list = []
b_list.append(1)
b_list.append(2)
b_list.append(3)
print(b_list)
c_list=[1,3.14,"hello",[1,2,3]]
print(c_list)
print(c_list[1:3])
d_list = [1,2,3,4,5]
print(d_list)
d_list[0] = 5
print(d_list)

print("Tuple")
a_tuple = (1,2,3,4,5)
print(a_tuple)
# a_tuple[0] = 5

print("Dictionary")
a_dic = {'a':1, 'b':2, 'c':3}
print(a_dic)
print(a_dic['a'])
print(a_dic['b'])
print(a_dic['c'])
b_dic={1:'a','b':[1,2,3],'c':3}
print(b_dic[1])
print(b_dic['b'])
print(b_dic['c'])
b_dic['d']= 4
print(b_dic)

print('Set')
a_set = set([1,2,3,4])
print(a_set)
b_set = set([1,1,2,2,3,3,4,5,6])
print(b_set)
c_set = set("python40s")
print(c_set)

# 5.연산 - 사칙연산, 논리연산, 비교연산
print('5.--------------------------')
print("사칙연산")
print("더하기 : ",10+20)
print("빼기 : ",10-20)
print("나누기 : ",10/20)
print("곱하기 : ",10*20)
print("10**2 : ",10**2)
print("10**3 : ",10**3)
print("10**4 : ",10**4)
print("몫 : ",40//6)
print("너머지 : ",40%6)

print("논리연산")
print(0 or 0)
print(0 or 1)
print(1 or 0)
print(1 or 1)
print(False or False)
print(False or True)
print(True or False)
print(True or True)
print(0 and 0)
print(0 and 1)
print(1 and 0)
print(1 and 1)
print(False and False)
print(False and True)
print(True and False)
print(True and True)
print(not 0)
print(not 1)
print(not False)
print(not True)

print("비교연산")
print(10 == 10)
print(10 >= 10)
print(10 <= 10)
print(10 < 5)
print(10 > 5)
print(10 != 10)
x_list = ['a',2,'hello',3]
print('a' in x_list)
print(1 in x_list)
print('hello' in x_list)
print(3 in x_list)
a_str = "hello python"
print("python" in a_str)
print("py" in a_str)
print("40" in a_str)

# 6.조건문
print('6.--------------------------')
a = 1
b = 1
if a == b:
      print("두 개의 값은 같습니다.")
if a != b:
      print("두 개의 값은 같지 않습니다.")

if a == b:
      print("두 개의 값은 같습니다.")
else:
      print("두 개의 값은 같지 않습니다.")

a = 1
b = 2
if a > b:
      print("a 값이 더 큽니다.")
elif a < b:
      print("b 값이 더 큽니다.")
else:
      print("두개의 값은 같습니다.")

a = 1
b = 1
if a >= b:
      print("a 값이 더 크거나 같습니다.")
if a <= b:
      print("a 값이 더 적거나 같습니다")

a = 1
b = 1
c = 2
d = 2
if a == b and c == d:
      print("두 조건 모두 만족")
if a == b or c == d:
      print("두 조건 중 하나라도 만족")

a_str = "hello python"
if a_str == "hello python":
      print("hello python 문자열과 같음")
if a_str == "hi python":
      print("hi python 문자열과 같음")
