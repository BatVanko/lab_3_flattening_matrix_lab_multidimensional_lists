rows = int(input())
matrix = [input().split(', ') for _ in range(rows)]
flattened_matrix = [int(x) for row in matrix for x in row]
print(flattened_matrix)