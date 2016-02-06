def isFloat(obj):
    try:
        f = float(obj)
        return True
    except ValueError:
        return False

value = 0

while True:

    cmd = ""
    cmd = input(':')
    
    if isFloat(cmd):
        value = float(cmd)

    print(value)
