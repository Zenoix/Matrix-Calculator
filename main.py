def get_1_matrix():
    size = list(map(int, input("Enter size of matrix: ").split()))
    print("Enter matrix:")
    matrix = [input().split() for row in range(size[0])]
    return matrix


def get_2_matrices():
    size1 = list(
        map(int,
            input("Enter size of first matrix: ").split()))
    print("Enter first matrix:")
    matrix1 = [input().split() for row in range(size1[0])]

    size2 = list(
        map(int,
            input("Enter size of second matrix: ").split()))
    print("Enter second matrix:")
    matrix2 = [input().split() for row in range(size2[0])]
    return size1, size2, matrix1, matrix2


def add_matrices(size, matrix1, matrix2):
    output = []
    for row in range(int(size[0])):
        current_row = []
        for column in range(int(size[1])):
            current_row.append(
                float(matrix1[row][column]) + float(matrix2[row][column]))
        current_row = map(str, current_row)
        output.append(current_row)
    print("The result is:")
    for row in output:
        print(" ".join(row))


def const_multiply_matrix(matrix, constant):
    output = []
    for row in matrix:
        current_row = []
        for value in row:
            current_row.append(float(value) * constant)
        current_row = map(str, current_row)
        output.append(current_row)
    print("The result is:")
    for row in output:
        print(" ".join(row))


def multiply_matrix(num_rows, num_columns, matrix1, matrix2):

	output = []
	# iterate through rows of X
	for i in range(len(matrix1)):
		current_row = []
	# iterate through columns of Y
		for j in range(len(matrix2[0])):
			current_index = 0
			# iterate through rows of Y
			for k in range(len(matrix2)):
				current_index += float(matrix1[i][k]) * float(matrix2[k][j])
			current_row.append(str(current_index))
		output.append(current_row)

	print("The result is:")
	for row in output:
		print(" ".join(row))
	

if __name__ == "__main__":

    menu = '''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit'''

    while True:
        print(menu)
        selection = int(input("Your choice: "))

        if selection == 1:
            size1, size2, matrix1, matrix2 = get_2_matrices()
            if size1 == size2:
                add_matrices(size1, matrix1, matrix2)
            else:
                print("The operation cannot be performed.")

        elif selection == 2:

            matrix = get_1_matrix()
            constant = float(input("Enter constant: "))
            const_multiply_matrix(matrix, constant)

        elif selection == 3:
            size1, size2, matrix1, matrix2 = get_2_matrices()
            if size1[1] == size2[0]:
                multiply_matrix(size1[0], size2[1], matrix1, matrix2)
            else:
                print("The operation cannot be performed.")
        elif selection == 0:
            quit()

        print("")
		
