import cryptocode

내용 = "암호화 할 내용입니다. 여기에 쓰인 문자열을 암호화 합니다."
비밀번호 = "12345"

encoded_string = cryptocode.encrypt(내용,비밀번호)
print("암호화:",encoded_string)

decoded_string = cryptocode.decrypt(encoded_string, "3")
print("복호화 비밀번호 틀림:",decoded_string)

decoded_string = cryptocode.decrypt(encoded_string, 비밀번호)
print("복호화:",decoded_string)