from turtle import left, right


def triangle(height, position = None):
    for i in range(height):
        print (" " *(position-i-1) + "*"*(2*i+1))

triangle(position = 10, height= 5)
triangle(5, 10)
triangle(8, position = 10)
triangle(height= 5, position = 10)



