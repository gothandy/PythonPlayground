print(sum(x**2 for x in range(10)))

def countdown(n):
    while n > 0:
        yield n
        n -= 1

print(','.join(str(x) for x in countdown(10)))

