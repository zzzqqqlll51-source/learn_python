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



# # judge a number
# number = int(input("please input a number:"))
# if number > 0:
#     print(">0")
# elif number < 0:
#     print("<0")
# else:
#     print("=0")


# judge a day
# day = input("please input a day:")

# match day:
#     case "1":
#         print("Monday")
#     case "2":
#         print("Tuesday")
#     case "3":
#         print("Wednesday")
#     case "4":
#         print("Thursday")
#     case "5":
#         print("Friday")
#     case "6"|"7":
#         print("Weekend")
#     case _:
#         print("error")


# # print words for 10 times
# i = 0
# while(i < 10):
#     print("aaa")
#     i += 1
# else:
#     print("The end.The cycling worked well.")


# #The sum of even numbers within 1-100
# i = 1
# total = 0
# while i <= 100:
#     if i % 2 == 0:
#         total += i
#     i += 1

# print(f"total = {total}")


# # try to use for
# msg = input("please input a message:")
# for word in msg:
#     print(f"word:{word}")
# else:
#     print("The end.The cycling worked well.")


# # try to use range
# total = 0
# for i in range(102,501,3):
#     total += i
# else:
#     print(f"total = {total}")



# # Nested Loops: Print Rectangles
# m = int(input("please input the lenth:"))
# n = int(input("please input the width:"))
# for i in range(n):
#     for k in range(m):
#         print("*  ",end="")
#     print("\n")


# # Print the multiplication table
# for i in range(1,10):
#     for k in range(1,i+1):
#         print(f"{k} * {i} = {i * k}",end="\t")
#     print("\n")


# # Make the user log in repeatedly until successful.

# def islanded(username,password):
#     if (username == "admin" and password == "666888") or (username == "zhangsan" and password == "123456"):
#         print("Login successful!")
#         return True
#     elif username == "" or password == "":
#         print("Username or password cannot be empty, please re-enter.")
#         return False
#     else:
#         print("Username or password incorrect, please re-enter.")
#         return False

# while True:
#     username = input("input your username:")
#     password = input("input your password:")
#     if(islanded(username,password)):
#         break


# Number Guessing Game
import random
answer = random.randint(a=0,b=100)
while True:
    num = int(input("please input a number:"))
    
    if num > answer:
        print("the number is too big!")
        continue
    elif num < answer:
        print("the number is too small!")
        continue
    else:
        print(f"correct!the correct number is {answer}.")
        break