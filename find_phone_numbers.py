import re

contex = "床头明月光18062366709，疑似地上霜，" \
"举头望18986662020明2321月，低头思1231231231231312故乡"

pattern = r"1[3-9]\d{9}"

results = re.findall(pattern,contex)

for result in results:
    print(result)