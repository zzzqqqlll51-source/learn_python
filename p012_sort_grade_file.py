def read_file():
    result = []
    with open("./students_grades.txt",encoding="utf8") as fin:  # 注意要加上encoding = “utf8”
        for line in fin:
            line = line[:-1]
            result.append(line.split(","))
    return result
    
def sort_grades(data):
    data = sorted(data,
                  key=lambda x : int(x[2]),
                  reverse=True)
    return data

def write_file(data):
    with open("./studens_sorted_grades.txt",'w',encoding="utf8") as fout:
        for hang in data:
            fout.write(",".join(hang)+"\n")


import os
print("当前文件路径:", __file__)
print("当前工作目录:", os.getcwd())

# 读取文件
data = read_file()
print(data)
# 排序成绩
data = sort_grades(data)
print(data)
# 打印文件
write_file(data)