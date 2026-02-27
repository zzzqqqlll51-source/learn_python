# # Calculate the average, maximum, and minimum values ​​of ten numbers entered by the user.
# list1 = []
# for i in range(1,11):
#     list1.append(int(input(f"input the {i} item:")))

# print(list1)
# list1.sort()
# print(list1)
# print(list1[0])
# print(list1[-1])
# avg = sum(list1) / len(list1)
# print(avg)


# # Merge two lists and remove duplicates
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# num_list1 = num_list1 + num_list2

# print(num_list1)

# newlist = []
# for num in num_list1:
#     if num not in newlist:
#         newlist.append(num) 

# print(newlist)


# # 选修足球学生名单
# football_set = {"王林","曾牛","徐立国","遁天","天运子","韩立","厉飞雨","乌丑","紫灵"}
# #选修篮球学生名单
# basketba_set = {"张铁","墨居仁","王林","姜老道","曾牛","王蝉","韩立","天运子","李化元","厉飞雨","云露"}
# #选修法语学生名单
# french_set = {"许木","王卓","十三","虎咆","姜老道","天运子","红蝶","厉飞雨","韩立","曾牛"}
# # 选修艺术学生名单
# art_set = {"遁天","天运子","韩立","虎咆","姜老道","紫灵"}
# #1.找出同时选修了法语和艺术的学生
# # Method 1
# fa_set = french_set.intersection(art_set)
# print(fa_set)

# # Method 2
# fa_set = french_set & art_set
# print(fa_set)

# #2.找出同时选修了所有四门课程的学生
# all_set = football_set & basketba_set & french_set & art_set
# print(all_set)


# #3.找出选修了足球,但是没有选修篮球的学生
# # Method 1 
# f_de_b_set = football_set.difference(basketba_set)
# print(f_de_b_set)

# # Method 2
# f_de_b_set = football_set - basketba_set
# print(f_de_b_set)

# # Method 3
# f_de_b_set = {i for i in football_set if i not in basketba_set}
# print(f_de_b_set)


# # 4.统计每一个学生选修的课程数量
# stu_set = football_set | basketba_set | french_set | art_set

# # for student in stu_set:
# #     cnt = 0
# #     if student in football_set:
# #         cnt += 1
# #     if student in basketba_set:
# #         cnt += 1
# #     if student in french_set:
# #         cnt += 1
# #     if student in art_set:
# #         cnt += 1
# #     print(f"{student} : {cnt}")

# stu_list = [*football_set,*basketba_set,*french_set,*art_set]
# for student in stu_set:
#     print(f"{student}:{stu_list.count(student)}")




# # 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
# # 系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下:
# # 1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# # 2.修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# # 3.删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# # 4.查询购物车:将购物车中的商品信息展示出来，格式为:"商品名称:xxx，商品价格:xxx，商品数量:xxx"。
# # 5.退出购物车

# shopping_cart = {}

# # make a manu
# print("Welcome to the shopping cart managing system ~")
# manu = """
# ############## shopping cart system #############
# #              1. Add to cart                   # 
# #              2. Edit cart                     #
# #              3. Delete cart                   # 
# #              4. View cart                     #
# #              5. Exit cart                     #
# """
# print(manu)

# # Perform specific operations
# while True:
#     choice = input("please input your choice hear:")
#     match manu:
#         case "1":
#             name = input("please input the good\'s name:")
#             price = float(input("please input the price of the goods:"))
#             quantity = input("please input the quantity of goods:")

#             # If it already exists, the addition will not be performed, and a prompt message will be displayed.
#             if name in shopping_cart:
#                 print("the goods has aleady exists!")
#             else:
#                 shopping_cart[name] = {"price":price,"quantity":quantity}

#         case "2":
#             name = input("please input the good you want to edit:")
#             if name in shopping_cart:
#                 new_price = float(input("please input the new price:"))
#                 new_quantity = input("please input the new quantity:")
#                 shopping_cart[name] = {"price":new_price,"quantity":new_quantity}
#             else:
#                 print("This product does not exist!")

#         case "3":
#             name = input("please input the good you want to delete")
#             if name in shopping_cart:
#                 shopping_cart.pop(name)
#             else:
#                 price("This product does not exist!")
            
#         case "4":
#             for item in shopping_cart.items():
#                 print(item)

#         case "5":
#             print("bye~")
#             break

#         case _:
#             print("Illegal operation, not supported!")


# Develop an academic affairs management system that can maintain and manage student academic information. Specific requirements are as follows:
# 1. Add Student Information: Enter student name, Chinese, Math, and English scores based on prompts, and save the information to the system.

# 2. Modify Student Information: Requires the student's name to be modified, followed by their Chinese, Math, and English scores. Modify the student's information after inputting the scores.

# 3. Delete Student Information: Requires the student's name to be deleted, and deletes the student's information based on that name.

# 4. Query Student Information: Requires the student's name to be queried, retrieves the student's information based on that name, and outputs the results.

# 5. List All Students: Iterate through all student information and output the results.

# 6. Calculate Class Grades: Calculate the highest, lowest, and average scores for Chinese, Math, and English in the class, and list the names of the students with the highest and lowest scores in each subject.

# 7. Exit System.

print("welcome to academic affairs management system~")
print("""
#####################academic affairs management system############################
1. Add Student Information: Enter student name, Chinese, Math, and English scores based on prompts, and save the information to the system.

2. Modify Student Information: Requires the student's name to be modified, followed by their Chinese, Math, and English scores. Modify the student's information after inputting the scores.

3. Delete Student Information: Requires the student's name to be deleted, and deletes the student's information based on that name.

4. Query Student Information: Requires the student's name to be queried, retrieves the student's information based on that name, and outputs the results.

5. List All Students: Iterate through all student information and output the results.

6. Calculate Class Grades: Calculate the highest, lowest, and average scores for Chinese, Math, and English in the class, and list the names of the students with the highest and lowest scores in each subject.

7. Exit System.
""")

stu_inform = {}

while True:
    choice = input("pleace input your choice here:")
    match choice:
        case "1":
            name = input("sdudent\'s name:")
            c_scores = float(input("Chinese scores:"))
            m_scores = float(input("Math scores:"))
            e_scores = float(input("English scores:"))
            stu_inform[name] = {'c_scores':c_scores,'m_scores':m_scores,'e_scores':e_scores}
            print("Data entry successful~")
        case "2":
            name = input("Please enter the student's name from whom you wish to modify the information:")
            c_scores = float(input("pleace input the new Chinese scores:"))
            m_scores = float(input("pleace input the new Math scores:"))
            e_scores = float(input("pleace input the new English scores:"))
            stu_inform[name] = {'c_scores':c_scores,'m_scores':m_scores,'e_scores':e_scores}
            print("Modification successful~")
        case "3":
            name = input("Please enter the name of the student you wish to delete:")
            if name in stu_inform:
                stu_inform.pop(name)
                print("Deletion successful~")
            else:
                print("This student does not exist. Please re-enter.")
        case "4":
            name = input("Pleace enter the name of the student you wish to query:")
            if name in stu_inform:
                print(name)
                for subject,scores in stu_inform[name].items():
                    print(subject,":",scores)
            else:
                print("This student does not exist.Pleace re-enter.")
        case "5":
            for item in stu_inform.items():
                print(item)
        case "6":
            c_list = []
            m_list = []
            e_list = []
            c_max = None
            m_max = None
            e_max = None
            c_min = None
            m_min = None
            e_min = None
            for name,scores in stu_inform.items():
                c_score = scores['c_scores']
                m_score = scores['m_scores']
                e_score = scores['e_scores']
                c_list.append(c_score)
                m_list.append(m_score)
                e_list.append(e_score)
                if c_score >= max(c_list):
                    c_max = name
                if m_score >= max(m_list):
                    m_max = name
                if e_score >= max(e_list):
                    e_max = name
                if c_score <= min(c_list):
                    c_min = name
                if m_score <= min(m_list):
                    m_min = name
                if e_score <= min(e_list):
                    e_min = name
            print(f"Average score in Chinese:{sum(c_list)/len(c_list)}")   
            print(f"Average score in Math:{sum(m_list)/len(m_list)}") 
            print(f"Average score in English:{sum(e_list)/len(e_list)}")  
            print(f"Highest score in Chinese:{c_max}:{max(c_list)}")
            print(f"Highest score in Math:{m_max}:{max(m_list)}")
            print(f"Highest score in English:{e_max}:{max(e_list)}")
            print(f"Lowest score in Chinese:{c_min}:{min(c_list)}")
            print(f"Lowest score in Math:{m_min}:{min(m_list)}")
            print(f"Lowest score in English:{e_min}:{min(e_list)}")

        case "7":
            break
        case _:
            print("Illegal operation, not supported.")



