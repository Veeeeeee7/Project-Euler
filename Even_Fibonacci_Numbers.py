def even_fibonacci_numbers(limit):
    a = 1
    b = 2
    sum = 0
    while b < limit:
        # print(a)
        if b % 2 == 0:
            sum += b
        atemp = a
        a = b
        b = atemp+b
    
    return sum

if __name__ == "__main__":
    sum = even_fibonacci_numbers(4000000)
    print(sum)