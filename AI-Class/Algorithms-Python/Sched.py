"""
Scheduling as covered in Unit 15-3

>>> tn = TaskNetwork(['S',('a',30),('b',30),('c',10),('x',60),('y',15),('z',10),'F'], {'S':['a','x'], 'a':['b'], 'b':['c'], 'c':['F'], 'x':['y'], 'y':['z'], 'z':['F']})

>>> tn.next_tasks('a')
['b']

>>> tn.prev_tasks('a')
set(['S'])

>>> tn.next_tasks('F')
set([])

>>> tn.next_tasks('x')
['y']

>>> tn.prev_tasks('F')
set(['c', 'z'])

>>> tn.duration('x')
60

>>> tn.duration('c')
10

>>> tn.duration('z')
10

>>> tn.duration('b')
30

>>> tn.schedule()
[('a', 0, 15), ('c', 60, 75), ('b', 30, 45), ('F', 85, 85), ('S', 0, 0), ('y', 60, 60), ('x', 0, 0), ('z', 75, 75)]

"""

class TaskNetwork(object):
	r"""A simple task network, e.g.,

         a - b - c
        /          \
     start        finish
		    \          /
		     d - e - f
	
	    durations:
				a = 30 min
				b = 30 min
				c = 10 min
				d = 60 min
				e = 15 min
				f = 10 min

			with functions ES and LS, earliest start time
			and latest start time, respectively, given by:

			ES(start) = 0
			ES(B) = max a->b ES(A) + Duration(A)
			LS(finish) = ES(finish)
			LS(A) = min b<-a LS(B) - Duration(A)

			A schedule for the task network is defined
			as the set [ (x, ES(x), LS(x)) for all tasks x ]
	"""
	def __init__(self,tasks,links):
		"""
			tasks
				[start, (task1, duration1), (task2, duration2), ... , (task3, duration3), finish]
			links
				{ start: [task, task, ...], task1:[task, task, ...] }
		"""

		duration_map = dict()
		size = len(tasks)
		self.tasks = set()
		for i in xrange(size):
			t = tasks[i]
			if i == 0:
				self.start = t
				self.tasks.add(t)
			elif i == (size-1):
				self.finish = t
				self.tasks.add(t)
			else:
				label, duration = t
				assert label not in duration_map, 'duplicate task: ' + label
				duration_map[label] = duration
				self.tasks.add(label)

		self.duration_map = duration_map

		self.links = links

	def __repr__(self):
		return ''.join(['< ',self.__class__.__name__,' links=',repr(self.links),', duration_map=',repr(self.duration_map),', tasks=',repr(self.tasks),' >'])

	def duration(self, a):
		"""the duration of task a"""
		if a == self.start or a == self.finish:
			return 0
		return self.duration_map[a]

	def next_tasks(self, a):
		"""the tasks that immediately follow a"""
		if a in self.links:
			return self.links[a]
		return set()

	def prev_tasks(self, a):
		"""the tasks that immediately precede a"""
		result = set()
		for t in self.tasks:
			if t != a and a in self.next_tasks(t):
				result.add(t)
		return result

	def es(self, b):
		"""The earliest start time for task b"""
		if b == self.start:
			return 0

		return max([ (self.es(a) + self.duration(a)) 
			for a in self.prev_tasks(b) ])

	def ls(self, a):
		"""The latest start time for task a"""
		if a == self.finish:
			return self.es(a)

		return min([ (self.ls(b)-self.duration(a)) 
			for b in self.next_tasks(a) ])

	def schedule(self):
		"""A schedule for this task network"""
		sched = []
		for t in self.tasks:
			sched.append( (t, self.es(t), self.ls(t) ) )
		return sched

if __name__ == '__main__':
	import doctest
	doctest.testmod()


