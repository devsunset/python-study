from distutils.dir_util import copy_tree

원본_폴더 = "원본"
백업될_폴더 = "백업"
result = copy_tree(원본_폴더, 백업될_폴더,update=1)
print(result)


# from win10toast import ToastNotifier
# toaster = ToastNotifier()
# toaster.show_toast("백업이 완료되었습니다.",원본_폴더 + " >>> " + 백업될_폴더,duration=10)