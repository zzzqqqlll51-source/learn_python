

def get_even_numbers(begin,end):
    evens = []
    for i in range(begin,end+1):
        if i % 2 == 0:
            evens.append(i)
    return evens

begin = 3
end = 14
print(f"begin = {begin},end = {end},evens:",get_even_numbers(begin,end))

data = [item for item in range(begin,end+1) if item % 2 == 0]
print(f"begin = {begin},end = {end},evens:",data)