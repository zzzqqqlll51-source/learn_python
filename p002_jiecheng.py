def getjiecheng(num):
    result = 1
    while num > 1:
        result  *= num
        num -= 1
    return result

print(getjiecheng(5))  # 输出 120
print(getjiecheng(0))  # 输出 1