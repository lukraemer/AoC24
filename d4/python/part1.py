def search_north(matrix, i, j, string):
    if i-3<0:
        return 0
    try:
        if matrix[i][j] == string[0] and matrix[i-1][j] == string[1] and matrix[i-2][j] == string[2] and matrix[i-3][j] == string[3]:
            return 1 
        else:
            return 0
    except IndexError:
        return 0

def search_north_east(matrix, i, j, string):
    if i-3<0:
        return 0
    try:
        if matrix[i][j] == string[0] and matrix[i-1][j+1] == string[1] and matrix[i-2][j+2] == string[2] and matrix[i-3][j+3] == string[3]:
            return 1 
        else:
            return 0
    except IndexError:
        return 0

def search_east(matrix, i, j, string):
    try:
        if matrix[i][j] == string[0] and matrix[i][j+1] == string[1] and matrix[i][j+2] == string[2] and matrix[i][j+3] == string[3]:
            return 1 
        else:
            return 0
    except IndexError:
        return 0

def search_south_east(matrix, i, j, string):
    try:
        if matrix[i][j] == string[0] and matrix[i+1][j+1] == string[1] and matrix[i+2][j+2] == string[2] and matrix[i+3][j+3] == string[3]:
            return 1 
        else:
            return 0
    except IndexError:
        return 0

def search_south(matrix, i, j, string):
    try:
        if matrix[i][j] == string[0] and matrix[i+1][j] == string[1] and matrix[i+2][j] == string[2] and matrix[i+3][j] == string[3]:
            return 1 
        else:
            return 0
    except IndexError:
        return 0

def search_south_west(matrix, i, j, string):
    if j-3<0:
        return 0
    try:
        if matrix[i][j] == string[0] and matrix[i+1][j-1] == string[1] and matrix[i+2][j-2] == string[2] and matrix[i+3][j-3] == string[3]:
            return 1 
        else:
            return 0
    except IndexError:
        return 0

def search_west(matrix, i, j, string):
    if j-3<0:
        return 0
    try:
        if matrix[i][j] == string[0] and matrix[i][j-1] == string[1] and matrix[i][j-2] == string[2] and matrix[i][j-3] == string[3]:
            return 1 
        else:
            return 0
    except IndexError:
        return 0

def search_north_west(matrix, i, j, string):
    if i-3<0 or j-3<0:
        return 0
    try:
        if matrix[i][j] == string[0] and matrix[i-1][j-1] == string[1] and matrix[i-2][j-2] == string[2] and matrix[i-3][j-3] == string[3]:
            return 1 
        else:
            return 0
    except IndexError:
        return 0

def search_string_in_matrix(matrix, string) -> int:
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            count += search_north(matrix, i, j, string)
            count += search_north_east(matrix, i, j, string)
            count += search_east(matrix, i, j, string)
            count += search_south_east(matrix, i, j, string)
            count += search_south(matrix, i, j, string)
            count += search_south_west(matrix, i, j, string)
            count += search_west(matrix, i, j, string)
            count += search_north_west(matrix, i, j, string)
    return count
f = open("../input", "r")

width = 140
height = 140

matrix = [0 for y in range(height)]
line_number = 0
for line in f:
    splitted_line =list(line.rstrip("\n"))
    matrix[line_number] = splitted_line
    line_number += 1

print(f"Result Part 1: ", search_string_in_matrix(matrix, "XMAS"))
