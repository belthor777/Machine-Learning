import math

class MotionModel(object):
	def __init__(self, x0=0, y0=0, theta0=0, v=0, w=0):
		self.x = float(x0)
		self.y = float(y0)
		self.theta = float(theta0)
		self.v = float(v)
		self.w = float(w)

	def __str__(self):
		return 'x=%.4f, y=%.4f, theta=%.4f' % (self.x, self.y, self.theta)

	def move(self, delta_t):
		new_x = self.x + self.v * delta_t * math.cos(self.theta)
		new_y = self.y + self.v * delta_t * math.sin(self.theta)
		new_theta = self.theta + self.w * delta_t

		self.x, self.y, self.theta = new_x, new_y, new_theta

	def move_times(self, delta_t, times):
		for i in xrange(times):
			self.move(delta_t)
			print "time=%d, pos=%s" % (delta_t+i*delta_t, str(self))

