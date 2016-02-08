# First using splicing
def EnglishList(list, seperator = ', ', finalSeperator = ' or '):
    
    x = len(list) - 1

    return seperator.join(list[0:x]) + finalSeperator + list[x]

print(EnglishList(['blue', 'green', 'red']))

# Using generator with yield statements
def joinGen(list, a = ', ', b = ' and '):
    z = len(list) -2
    for i, x in enumerate(list):
        yield(str(x))
        if i < z:
            yield(a)
        elif i == z:
            yield(b)

print(''.join(joinGen(range(10))))

# Using multiple generators
def reverseEnumerate(list):
    for i,x in enumerate(list):
        yield len(list) - i - 1, x

def addChar(enum, c = ','):
    for i,x in enum:
        yield i, str(x) + c if i > 1 else str(x)

def addLast(enum, s = 'and'):
    for i,x in enum:
        if i == 0:
            yield s
        yield x

print(' '.join(addLast(addChar(reverseEnumerate(range(10))))))