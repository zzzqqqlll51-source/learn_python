def isprime(num):
    if num == 1 or num == 2:
        return True
    for i in range(2,num):
        if i*i <= num and num % i == 0:
            return False
    return True



def print_primes(begin,end):
    for i in range(begin,end+1):
        if isprime(i):
            print(i)

begin = 4
end = 56
print_primes(begin,end)