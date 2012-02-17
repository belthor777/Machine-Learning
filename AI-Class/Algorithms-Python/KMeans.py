from math import pow
from math import sqrt
from math import exp
from math import pi
import random

tau = (2 * pi)

class KMeans:
	"""
	Attempt to implement the KMeans algorithm
	as described in Unit 6 of the AI class.
	"""

	def __init__(self,k,data,max_guess=(100,100),min_guess=(-100,-100)):
		"""
		Construct a K-means with the given parameters.

		'max_guess' and 'min_guess' control the range of values
		used when generating random cluster centers; the author
		has not thought very hard about a way to generate values
		that are always guaranteed to work no matter what data we
		have.
		"""
		self.k = k
		self.data = data
		self.max_guess = max_guess
		self.min_guess = min_guess

	def rand_cluster_center(self):
		x = random.uniform(self.min_guess[0],self.max_guess[0])
		y = random.uniform(self.min_guess[1],self.max_guess[1])
		return x, y

	def dist(self, a, b):
		ax, ay = a[1], a[2]
		bx, by = b[1], b[2]
		return sqrt( pow(by-ay,2)+pow(bx-ax,2) )

	def centers(self):
		centers = []
		for i in xrange(self.k):
			rc = self.rand_cluster_center()
			centers.append([i, rc[0], rc[1]])
		return centers

	def closest_center(self, centers, datum):
			closest = None
			closest_d = None
			for c in centers:
				d = self.dist(c, datum)
				if closest is None or d < closest_d:
					closest = c
					closest_d = d
			return (closest, closest_d)
	
	def mean(self, data_points):
		n = float(len(data_points))
		mean_x = sum( [dp[1] for dp in data_points] ) / n
		mean_y = sum( [dp[2] for dp in data_points] ) / n
		return (mean_x, mean_y)

	def kmeans(self,initial_centers=None,tolerance=0):
		""" Run the K-means algorithm to convergence 
			(or until the difference in an old and new cluster
			center in one iteration is <= tolerance)
		"""
		centers = initial_centers \
				if initial_centers is not None else self.centers()
		
		iterations = 0
		while True:
			iterations = iterations + 1
			clusters = dict([(i,[]) for i in xrange(self.k)])
			for a in self.data:
				cc = self.closest_center(centers, a)
				center = cc[0]
				label = center[0]
				clusters[label].append(a)

			for label, data_points in clusters.iteritems():
				if not data_points:
					centers = self.centers()
					break # restart at random

				center = centers[label]
				old_center_x, old_center_y = center[1], center[2]
				new_center_x, new_center_y = self.mean(data_points)

				if abs(new_center_x - old_center_x) <= tolerance \
						and abs(new_center_y - old_center_y) <= tolerance:
					# converged
					return {
							'iterations' : iterations,
							'clusters' : clusters, \
							'centers' : centers }

				# update center to mean
				center[1] = new_center_x
				center[2] = new_center_y

def mean(v,M):
	return sum( v ) / float(M)

def variance(v,u):
	return mean( ( (pow((x - u),2) for x in v)), len(v) )

def transpose(v, dims):
	"Swap rows and columns"

	numRows = len(v)
	t = dims*[None] 
	for i in range(dims):
		t[i] = numRows* [None]
		for j in range(numRows):
			t[i][j] = v[j][i]
	return t

def matrixMultiply(a, colsA, b, colsB):
	"""Multiply to matrices
	
		Very basic and inefficient implementation; 
		nothing near the sophistication of Strassen's algorithm 
		is used."""
	rowsA = len(a)
	rowsB = len(b)

	# rowsA x colsA  ... rowsB x colsB 
	assert rowsA == colsB, "matrix dimensions not fit for multiplication"

	# result size: rowsA x colsB
	r = rowsA * [None]
	for i in range(rowsA):
		r[i] = colsB * [None]
		for j in range(colsB):
				r[i][j] = sum( a[i][k]* b[k][j] for k in range(colsA))
	return r

def scalarMultiply(a, cols, x):
	""" Multiplies the matrix a by the scalar x."""
	r = len(a) * [None]
	for i in range(len(a)):
		r[i] = cols * [None]
		for j in range(cols):
			r[i][j] = a[i][j] * x
	return r
	

def subtractRows(a, colsA, b):
	""" Subtract the tuple b from each row of matrix a. The length of b must be the dimentions of a.
	
	Ex.:
	3  8                 -2  3
	4  7   -   5   5 =   -1  2
	5  5                  0  0
	"""
	assert colsA == len(b), "incompatible dimensions for subtractRows"
	r = len(a)*[None]
	for i in range(len(a)):
		r[i] = colsA * [None]
		for j in range(colsA):
			r[i][j] = a[i][j] - b[j]
	return r

def printMatrix(a):
	buf = []
	fmt = "%5s"
	for x in a:
		buf.append('[')
		for y in x:
			buf.append(fmt % str(y))
		buf.append(']\n')
	print ''.join(buf)



class Gauss:
	"""
	Gaussian distribution for input vector v:

	mean = 1/ M sum( Xi )
	variance = 1 / M * sum( (Xi - mean)^2 )

	>>> Gauss([3,4,5,6,7]).mean()
	5.0
	
	>>> Gauss([3,4,5,6,7]).variance()
	2.0

	>>> Gauss([3,4,5,6,7]).p(3.456)
	0.1848502338825046
	"""

	def __init__(s, v=None):
		s.v = v if v is not None else [1]

	def mean(s):
		return mean( (x for x in s.v), len(s.v))

	def variance(s):
		return variance(s.v, s.mean())

	def p(s, x):
		mu = s.mean()
		sigma2 = s.variance()
		sigma = sqrt(sigma2)
		return 1/sqrt( tau * sigma ) * exp( -.5 * pow(x - mu, 2) / sigma2 )

class MultiGauss:
	"""
	MultiGauss(2, [(1,2),(3,4),(5,6)])

	Specifiy dimensions and then vector of tuples.

	Example:
	>>> MultiGauss(2, [[3,8],[4,7],[5,5],[6,3],[7,2]]).variances()
	[[2.0, -3.2000000000000002], [-3.2000000000000002, 5.2000000000000002]]

	>>> MultiGauss(2, [[3,8],[4,7],[5,5],[6,3],[7,2]]).means()
	(5.0, 5.0)
	"""
	def __init__(s, dims, v):
		s.dims = dims
		s.v = v

	def means(s):
		"Returns the mean of each dimenion as a tuple"
		return [ mean( (x[i] for x in s.v), len(s.v) ) for i in range(s.dims)]

	def variances(s):
		means = s.means()
		xMinusU = subtractRows(s.v, s.dims, means)
		xMinusU_T = transpose(xMinusU, s.dims)
		r = matrixMultiply(xMinusU_T, len(s.v), xMinusU, s.dims)
		return scalarMultiply(r, s.dims, 1/float(len(s.v)))


def testIt():
	mg = MultiGauss(2, [[3,8],[4,7],[5,5],[6,3],[7,2]])

	print "data:"
	printMatrix(mg.v)

	print "means:"
	printMatrix([mg.means()])

	print "variances:"
	printMatrix(mg.variances())

testIt()
