# Made By Ricky L.
def dot_product(a,b):
	total = 0

	for i in range(len(a)):
		total += a[i] * b[i]

	return total


def mult_scalar(matrix, scale):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			matrix[i][j] = scale * matrix[i][j]

	return matrix


def mult_matrix(a, b):
	result = []

	for i in range(len(a)):
		row = []
		for j in range(len(b[0])):
			column = []
			for k in range(len(b)):
				column.append(b[k][j])
			row.append(dot_product(a[i], column))
		result.append(row)

	return result
	
def euclidean_dist(a,b):
	dist = 0

	for i in range(len(a)):
		for j in range(len(a[i])):
			dist += ((a[i][j] - b[i][j])) ** 2
	
	return dist ** 0.5
