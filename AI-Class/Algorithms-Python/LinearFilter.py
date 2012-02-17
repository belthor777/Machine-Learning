"""Computer vision related stuff for Unit 16."""

def dims(matrix):
	if not matrix:
		return (0, 0)
	rows = len(matrix)
	assert rows > 0, "impossible? rows <= 0: " + rows
	return (rows, len(matrix[0]))

def convolve(image, kernel):
	"""Convolves the image with the kernel as shown in Unit 16-19 
	and returns the result, that is, implements the linear filter 
	algorithm from 16-21:

	I'(x,y) = Sum( I(x - v, y - v) * g(u, v) for all u and v )
	where I is the input image, I' is the output, and g is the
	kernel which is applied to I.

	>>> convolve([[255, 212, 7, 1, 3], [211, 237, 3, 9, 0]], [[1, -1]])
	[[43, 205, 6, -2], [-26, 234, -6, 9]]

	>>> convolve([[255,7,3],[212,240,4],[218,216,230]], [[-1, 1]])
	[[-248, -4], [28, -236], [-2, 14]]

	>>> convolve([[12, 18, 6],[2, 1, 7],[100, 140, 130]],[[-1],[1]])
	[[-10, -17, 1], [98, 139, 123]]

	>>> m = [[50, 67, 80],[255, 10, 2],[73, 86, 11]]
	>>> k = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
	>>> convolve(m, k)
	[[538]]
	>>> convolve(k, m)
	[[538]]
	>>> k = [[0, 0, 0, 0, 0],[0, 1, 0, -1, 0], [0, 2, 0, -2, 0], [0, 1, 0, -1, 0], [0, 0, 0, 0, 0]]
	>>> convolve(k, m)
	[[182, 377, -182], [173, 538, -173], [144, 193, -144]]
	
	"""
	l, k = dims(image)
	n, m = dims(kernel)

	num_rows = l - n + 1
	num_cols = k - m + 1
	result = []
	for i in xrange(num_rows):
		row = [None]*(num_cols)
		for j in xrange(num_cols):
			row[j] = sum([ (kernel[u][v]*image[i+u][j+v]) \
					for u in xrange(n) \
						for v in xrange(m) ])
		result.append(row)
	return result

if __name__ == '__main__':
	import doctest
	doctest.testmod()
