import math

class LinearRegression:
	""" Computes the linear regression variables, w0 and w1, 
	using the formula from class:
	
	w1 = M * Sum( Xi * Yi ) - Sum( Xi ) * Sum( Yi ) / 
			( M * Sum( Xi^2 ) - ( Sum( Xi )^2 )

	w0 = 1/M * Sum( Yi ) - w1 /  M * Sum( Xi ) 
		
	Example:
	>>> LinearRegression( [(2, 2), (4, 5), (6, 5), (8, 8)] ).regression()
	(0.5, 0.90000000000000002)
	"""
	def __init__(self,v=[(2, 2), (4, 5), (6, 5), (8, 8)]):
			self.v = v

	def x(self,i):
		"The x coordinate of the element at index i"
		return self.v[i][0]

	def y(self,i):
		"The y coordinate of the element at index i"
		return self.v[i][1]

	def square(self,x):
		"Utility for computing the square of the argument (calls math.pow(x,2))"
		return math.pow(x,2)

	def size(self):
		"Returns the number of elements in the input vector"
		return len(self.v)

	def range(self):
		"The indexes to use in a for-loop (0..M-1)"
		return range(self.size())

	def sum_xy(self):
		"the sum of Xi * Yi"
		return sum( (self.x(i) * self.y(i)) for i in self.range())

	def sum_x(self):
		"the sum of Xi"
		return sum( self.x(i) for i in self.range() )

	def sum_x2(self):
		"the sum of Xi^2"
		return sum( self.square(self.x(i)) for i in self.range() )

	def sum_y(self):
		"the sum of Yi"
		return sum( self.y(i) for i in self.range() )

	def w1(self):
		""" w1 = M * Sum( Xi * Yi ) - Sum( Xi ) * Sum( Yi ) / 
			( M * Sum( Xi^2 ) - ( Sum( Xi )^2 ) """
		m = self.size()
		sxy = self.sum_xy()
		sx = self.sum_x()
		sy = self.sum_y()
		sx2 = self.sum_x2()
		return (m * sxy - sx*sy)/float( m * sx2 - self.square(sx) )

	def w0(self):
		" w0 = 1/M * Sum( Yi ) - w1 /  M * Sum( Xi ) "
		m = self.size()
		sy = self.sum_y()
		sx = self.sum_x()
		return 1/float(m) * sy - self.w1()/float(m) * sx

	def regression(self):
		"""Computes the linear regression variables and returns 
			 the result as a tuple consisting of (w0, w1) """
		return (self.w0(), self.w1())

	def predictY(self,x):
		"""Predicts the y value using the w0 and w1 according to the formula:
			 y = w1 * x + w0
		"""
		reg = self.regression()
		w1=float(reg[1])
		w0=float(reg[0])
		return (x, w1*x + w0)

	def loss(self):
		w0=self.w0()
		w1=self.w1()
		return sum( self.square(float(self.y(i)) - w1*float(self.x(i)) - w0) for i in self.range() )
