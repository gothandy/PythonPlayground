def A():
    print('A')

def B():
    print('B')

def C():
    print('C')

i = 'b'

# Using Eval
f = { 'a': 'A()', 'b': 'B()' }
eval(f[i])

# Classic if
if i == 'a':
    A()
elif i == 'b':
    B()

# Short circuit.
def sc(x):
    (x == 'a' and A()) or (x == 'b' and B())
sc(i)

# Lambda
l = lambda x: (x == 'a' and A()) or (x == 'b' and B()) or (x == 'c' and C())
l(i)

# Map
list(map(l, ['a','b','c']))

# Comprehensions
[l(x) for x in ['a','b','c']]
