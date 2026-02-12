student = [
    {'sno':101,'sname':'小张','sgrade':'97'},
    {'sno':102,'sname':'小张','sgrade':'73'},
    {'sno':103,'sname':'小张','sgrade':'88'},
    {'sno':104,'sname':'小张','sgrade':'92'},
]

def sort_student(student):
    sorted_student = sorted(student,key=lambda x: x['sgrade'],reverse=True)
    return sorted_student

print(f"source:{student}")
print(f"result:{sort_student(student)}")