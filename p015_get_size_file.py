import os

print(os.path.getsize("p014_word_count_text.py"))

sum_size = 0
for file in os.listdir("."):
    if os.path.isfile(file):
        sum_size += os.path.getsize(file)
        print(file)

print("all size of the files is",sum_size/1024)
