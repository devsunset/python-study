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




