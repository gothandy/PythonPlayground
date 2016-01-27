def result(x,y):
    return int((x * x + y * y) * 19)

def line(width, height, row):
    a = ""
    for col in range(width):
        a = a + str(result((col/width) - 0.5,(row/height) - 0.5))
    return a

def grid(width,height):
    for row in range(height):
        print(line(width, height, row))

grid(79,40)