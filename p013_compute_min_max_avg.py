def compute():
    scores = []
    with open("./students_grades.txt",encoding="utf8") as fin:
        for line in fin:
            line = line[:-1]
            feilds = line.split(",")
            scores.append(int(feilds[-1]))
    score_max = max(scores)
    score_min = min(scores)
    score_avg = round(sum(scores) / len(scores),2)
    return score_max,score_min,score_avg

score_max,score_min,score_avg = compute()
print(f"score_max = {score_max},score_min = {score_min},score_avg = {score_avg}")