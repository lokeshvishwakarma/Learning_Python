"""
Transpose of a matrix
"""
import pprint
import copy

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def transpose(_matrix):
    result = copy.deepcopy(_matrix[:][:])
    print(result)
    for i in range(len(_matrix)):
        for j in range(len(_matrix[0])):
            print(j, i, '--', i, j)
            result[j][i] = _matrix[i][j]
    print('------------')
    for r in result:
        print(r)


# transpose(matrix)


# using list comprehension
# print(matrix)
# print([[r[col] for r in matrix] for col in range(len(matrix[0]))])

# using map and zip
# _map = map(list, zip(*matrix))
# print(list(_map))


def mytranspose(_matrix):
    result = _matrix[:][:]
    for row_index in range(len(_matrix)):
        for col_index in range(len(_matrix[0])):
            result[col_index][row_index] = _matrix[row_index][col_index]

    for row in result:
        print(row)

mytranspose(matrix)