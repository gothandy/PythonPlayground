import math
import Lambda
import Numbers

def Calculate(cmd, x):

    a = {
        'exit': None,
        'pi': math.pi,
        'sqrt': lambda x: math.sqrt(x),
        'sqr': lambda x: x ** 2,
        'p': lambda x, y: x ** y,
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
        }

    if cmd == 'help':
        for action in iter(a):
            print(action)
        return x

    for action in iter(a):

        if cmd.startswith(action):

            if not Lambda.isLambda(a[action]):
                return a[action]

            elif Lambda.args(a[action]) == ['x']:
                return a[action](x)

            elif Lambda.args(a[action]) == ['x','y']:
                y = float(cmd[len(action):])
                return a[action](x,y)

        if Numbers.IsFloat(cmd):
            return float(cmd)

    print(cmd, "unrecognized.")
    return x

def Calculator():

    x= float(0)
    while True:
        x = Calculate(input(':'), x)

        if x is None:
            break

        print(x)

Calculator()
        
