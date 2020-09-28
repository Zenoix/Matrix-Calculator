def add_matrices(matrix1, matrix2):
	output = []
	for row in range(int(size1[0])):
		current_row = []
		for column in range(int(size1[1])):
			current_row.append(
				int(matrix1[row][column]) + int(matrix2[row][column]))
		current_row = map(str, current_row)
		output.append(current_row)
	for row in output:
		print(" ".join(row))


def const_multiply_matrix(matrix, constant):
	print("Matrix: ", matrix)
	output = []
	for row in matrix:
		current_row = []
		for value in row:
			current_row.append(int(value) * constant)
		current_row = map(str, current_row)
		output.append(current_row)
	for row in output:
			print(" ".join(row))
			
def multiply_matrix():
  pass


if __name__ == "__main__":

	size1 = list(map(int, input().split()))
	matrix1 = [input().split() for row in range(int(size1[0]))]

	size2 = list(map(int, input().split()))
	if len(size2) == 1:
		const_multiply_matrix(matrix1, size2[0])
	else:
		matrix2 = [input().split() for row in range(int(size2[0]))]
		if size1 == size2:
			add_matrices(matrix1, matrix2)
		else:
			print("ERROR")
