import inspect

def isLambda(obj):
    return inspect.isfunction(obj)

def args(obj):
    if isLambda(obj):
        return inspect.getargspec(obj).args
    else:
        return None

#print(args(lambda x,y: x + y))
#print(args(lambda x: x))
#print(args(5.5)