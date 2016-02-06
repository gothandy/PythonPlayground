def IsFloat(s):
    try:
        v = float(s)
        return True
    except ValueError:
        return False