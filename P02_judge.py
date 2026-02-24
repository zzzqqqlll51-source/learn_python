# # if：B站登陆功能实现
# # 正确账号和密码
# corr_acount = "18888888888"
# corr_password = "666888"

# # receive the inputed account and password
# acount = input("please input your account:")
# password = input("please input your password:")

# # judge if the account and password is correct simutaneously,then land or give the message

# if acount == corr_acount:
#     if password == corr_password:
#         print("you land successfully!")
#     else:
#         print("the password is false")
# else:
#     print("the account is false")



# judge a number
number = int(input("please input a number:"))
if number > 0:
    print(">0")
elif number < 0:
    print("<0")
else:
    print("=0")