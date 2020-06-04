'''
简单的if else     冒号前面不能有空格
'''
account = 'Zz'
password = '123456'


print('please input account:')
user_account = input()

print('please input password:')
user_password = input()

if account == user_account and password == user_password:
    print('success')
else:
    print('fail')
