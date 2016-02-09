def Coordinating(list, seperator = ', ', coordinator = ' and '):
    
    x = len(list) - 1

    return seperator.join(list[0:x]) + coordinator + list[x] if x > 0 else list[0] 