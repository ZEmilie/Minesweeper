import random

def nb_mines_neighbour(matrix, w, l):
    # for a matrix (l*w) with mines(9)
    # return a matrix with m mines(9) and the number of neighbour mines
    for i in range(l):
        for j in range(w):
            if matrix[i][j]>8:
                # i-1
                if i-1>=0:
                    if j-1>=0:
                        matrix[i-1][j-1] += 1
                    matrix[i-1][j] += 1
                    if j+1<w:
                        matrix[i-1][j+1] += 1
                # i
                if j-1>=0:
                    matrix[i][j-1] += 1
                if j+1<w:
                    matrix[i][j+1] += 1
                # i+1
                if i+1<l:
                    if j-1>=0:
                        matrix[i+1][j-1] += 1
                    matrix[i+1][j] += 1
                    if j+1<w:
                        matrix[i+1][j+1] += 1
    for i in range(l):
        for j in range(w):
            if matrix[i][j]>8:
                matrix[i][j] = 9
    return matrix

def mines_position(w, l, m):
    # for width, length, and mines_number
    # return a matrix with m mines(>8) and the number of neighbour mines
    if m>l*w:
        raise ValueError("More mines than huts")
    indices = random.sample(range(l*w), m)
    matrix = [[9 if i*w+j in indices else 0 for j in range(w)] for i in range(l)]
    matrix = nb_mines_neighbour(matrix,w,l)
    return matrix
