def A():
    print('A')

def B():
    print('B')

f = { 'a': 'A()', 'b': 'B()' }

eval(f['b'])