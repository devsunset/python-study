# -----------------------------------------

# Hello World

print("Hello World")


# Document
# https://docs.python.org/ko/3/tutorial/
# http://pythonstudy.xyz/

# -----------------------------------------

# pip list

'''
    pip install 패키지명
    pip install django --upgrade
    pip uninstall 패키지명
    pip install -r requirements.txt
    pip freeze > requirements.txt

    ex)
    pip install django
    pip uninstall django
    pip install django --upgrade
'''
# -----------------------------------------

# debugger

'''
    python -m pdb filename.py

    import pdb
    
    def sum(x, y):
        z = x + y
        return z
    
    a = 10
    pdb.set_trace()  
    b = 20
    c = sum(a, b)
    print(c)
'''
# -----------------------------------------

# instll virtualenv && create venv  && upgrade pip && install django && startproject web

'''
    Windows Python38 

    pip install virtualenv

    python -m venv C:\dev\python-work\venv\

    C:\dev\python-work\venv\Scripts\activate.bat

    C:\dev\python-work\venv\Scripts\python -m pip install --upgrade pip

    C:\dev\python-work\venv\Scripts\pip install django

    C:\dev\python-work\  C:\dev\python-work\venv\Scripts\django-admin.exe startproject www

    # defalt port 8000
    C:\dev\python-work\www> C:\dev\python-work\venv\Scripts\python.exe .\manage.py runserver

    # port 8080
    C:\dev\python-work\www> C:\dev\python-work\venv\Scripts\python.exe .\manage.py runserver 8080
'''

# -----------------------------------------

# database (MySQL)

'''
    $ pip install PyMySQL
    $ pip install pymssql
    $ pip install cx_Oracle

    import pymysql
    
    conn = pymysql.connect(host='localhost', user='root', password='admin',  db='test', charset='utf8')
    
    curs = conn.cursor()
    
    sql = "select * from person"
    curs.execute(sql)
    
    rows = curs.fetchall()

    print(rows)    


    sql = """insert into person(first_name,last_name,email)
            values (%s, %s, %s)"""
    curs.execute(sql, ('TEST1', 'TEST1', 'test1@test.com'))
    curs.execute(sql, ('TEST2', 'TEST2', 'test2@test.com'))

    data = (
        ('TEST1', 'TEST1', 'test1@test.com'),
        ('TEST2', 'TEST2', 'test2@test.com')
    )
    sql = """insert into person(first_name,last_name,email)
                values (%s, %s, %s)"""
    curs.executemany(sql, data)

    sql = "select * from person"
    curs.execute(sql) 
    rows = curs.fetchall()
    print(rows)   

    sql = """update person
            set last_name = 'TEST1'
            where last_name = 'TEST2'"""
    curs.execute(sql)

    sql = "select * from person"
    curs.execute(sql) 
    rows = curs.fetchall()
    print(rows)   
    
    sql = "delete from person where last_name=%s"
    curs.execute(sql, 'TEST1')

    # ? Placeholder
    sql = "delete from person where last_name =?"
    cur.execute(sql, (1, 'TEST1'))

    # Named Placeholder
    sql = "delete from person where last_name= :last_name"
    cur.execute(sql, {"last_name": 'TEST1'})
    
    conn.commit()

    sql = "select * from person"
    curs.execute(sql) 
    rows = curs.fetchall()
    print(rows)   

    conn.close()

    conn = pymysql.connect(host='localhost', user='root', password='admin',  db='test', charset='utf8')
    
    try:
        with conn.cursor() as curs:
            sql = "insert into person(first_name,last_name,email) values (%s, %s, %s)"
            curs.execute(sql, ('TEST1', 'TEST1', 'test1@test.com'))
            conn.commit() 


        with conn.cursor() as curs:
            sql = "select * FROM person"
            curs.execute(sql)
            rs = curs.fetchall()
            for row in rs:
                print(row)

    finally:
        conn.close()
'''

# -----------------------------------------

# JSON

'''
    import json
    
    person = {
        'id': 1111,
        'key': '생일',
        'birthday': [
            {'date': '2011-05-17', 'name': 'j won'},
            {'date': '2016-01-13', 'name': 's won'},
        ]
    }

    # jsonString = json.dumps(person)
    jsonString = json.dumps(person,indent=4)
    
    print(jsonString)
    print(type(jsonString))   

    jsonString = '{"id": 1111, "key": "생일", "birthday": [{"date": "2011-05-17", "name": "j won"}, {"date": "2016-01-13", "name": "s won"}]}'

    dict = json.loads(jsonString)

    print(dict['key'])
    for h in dict['birthday']:
        print(h['date'], h['name'])
'''

# -----------------------------------------

# File

'''
    # 읽기(r), 쓰기(w 혹은 x), 추가(a), 수정(+) , 텍스트 파일(t), 바이너리 파일(b) 

    f = open('test.txt', mode='wt', encoding='utf-8')
    f.write("1111\n")
    f.write("2222")
    f.close()


    f = open('test.txt', mode='rt', encoding='utf-8')
    s1 = f.readline() 
    s2 = f.readline() 
    print(s1)
    print(s2)
    f.close()


    import sys
    f = open('test.txt', mode='rt', encoding='utf-8')
    for line in f:
        sys.stdout.write(line)
    f.close()


    import sys
    f = open('test.txt', mode='rt', encoding='utf-8')
    for line in f:
        sys.stdout.write(line)
    f.close()


    try:
        f = open('test.txt', mode='rt', encoding='utf-8')
        for line in f:
            print(line)
    finally:
        f.close()


    with open('test.txt', mode='rt', encoding='utf-8') as f:
        for line in f:
            print(line)


    data = [1, 2, 3, 4, 5]
    with open("test.bin", "wb") as f:
        f.write(bytes(data))
    

    with open("test.bin", "rb") as f:
        content = f.read()   
        print(type(content))
        for b in content:
            print(b)    
    

    import csv    
    f = open('test.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    wr.writerow([1, "A", True])
    wr.writerow([2, "B", False])
    f.close()

    f = open('test.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        print(line)
    f.close()    


    f = open('test.tsv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f, delimiter='\t')
    wr.writerow([1, "A", True])
    wr.writerow([2, "B", False])
    f.close()
    
    f = open('test.tsv', 'r', encoding='utf-8')
    rdr = csv.reader(f, delimiter='\t')
    r = list(rdr)
    print("one=%s : two=%s : three=%s" % (r[0][0], r[0][1], r[0][2]))
    
    f.close()
'''   

# -----------------------------------------

# Serialization & Deserialization

'''
    import pickle
    
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.area = width * height
    
    
    rect = Rectangle(10, 20)
    
    # Serialization
    with open('rect.data', 'wb') as f:
        pickle.dump(rect, f)
    
    
    # Deserialization
    with open('rect.data', 'rb') as f:
        r = pickle.load(f)
    
    print("%d x %d" % (r.width, r.height))
'''
# -----------------------------------------

# Regular Expression

'''
    import re
    text = "AB CD AB CD AB CD\n EF GH EF GH EF GH "
    regex = re.compile("AB CD")
    mo = regex.search(text)
    print(mo)
    if mo != None:
        print(mo.group()) 
    
    text = "핸드폰 번호는 010-1234-5678 입니다." 
    regex = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
    matchobj = regex.search(text)
    phonenumber = matchobj.group()
    print(phonenumber)  

    text = "핸드폰 번호는 010-1234-5678 입니다." 
    regex = re.compile(r'(\d{3})-(\d{4}-\d{4})')
    matchobj = regex.search(text)
    telcom = matchobj.group(1)
    print(telcom) 
    num = matchobj.group(2)
    print(num) 
    fullNum = matchobj.group()
    print(telcom, num) 

    text = "핸드폰 번호는 010-1234-5678 입니다." 
    regex = re.compile(r'(?P<telcom>\d{3})-(?P<num>\d{4}-\d{4})')
    matchobj = regex.search(text)
    telcom = matchobj.group("telcom")
    num = matchobj.group("num")
    print(telcom, num)  
'''

# -----------------------------------------