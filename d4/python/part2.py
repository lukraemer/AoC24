def search_x(matrix, i, j, string):
    if i-1<0 or j-1<0:
        return 0
    try:
        s1 = matrix[i-1][j-1] + matrix[i][j] + matrix[i+1][j+1]
        s2 = matrix[i-1][j+1] + matrix[i][j] + matrix[i+1][j-1]
        if (s1 == string or s1 == string[::-1]) and (s2 == string or s2 == string[::-1]):
            return 1
        else:
            return 0
    except IndexError:
        return 0


def search_x_string_in_matrix(matrix, string) -> int:
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "A":
                count += search_x(matrix, i, j, string)
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

print(f"Result Part 2: ", search_x_string_in_matrix(matrix, "MAS"))
