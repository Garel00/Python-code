#Pascal triangle

def pascal_triangle(x, y):

    if y == 0 or x == y:
        return 1
    
    
    return pascal_triangle(x-1, y-1) + pascal_triangle(x-1, y)

print(pascal_triangle(4,2))