"""
A module for the value iteration algorithm for ai-class.com.
The simple Grid World is easily handled. How about other worlds?
"""

import random
import math



# Convenience hack for using 'a3', 'c2' notation instead of x, y coordinates.
ROW_LETTERS="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def letterToIndex(x):
	""" Converts the lowercase row letter to a 0 based index. 
		>>> letterToIndex('a')
		0
		>>> letterToIndex('aa')
		52
		>>> letterToIndex('b')
		1
		>>> letterToIndex('bb')
		53
		>>> letterToIndex('A')
		26
	"""
	len_x = len(x)
	num_letters = len(ROW_LETTERS)
	index = -1
	for i in xrange(num_letters):
		if ROW_LETTERS[i] == x[0]:
			index = i
			break
	if index == -1:
		raise KeyError(x)

	return (num_letters * (len_x-1) + index)

def indexToLetter(x):
	""" Converts the zero-based index to a row letter. 
		>>> indexToLetter(0)
		'a'
		>>> indexToLetter(52)
		'aa'
		>>> indexToLetter(1)
		'b'
		>>> indexToLetter(53)
		'bb'
		>>> indexToLetter(26)
		'A'
	"""
	size = len(ROW_LETTERS)
	times = x / size + 1
	return ROW_LETTERS[x % size] * times

def parseKey(key):
	"""
		Returns a tuple of two indexes 
		representing row and column, respectively.
		
		The key can be a string formated as 'a3'
		a tuple or list, such as (0,1) or [3,3],
		or ('a', 5).

		The key can also be a State instance (or
		anything with an 'x' and 'y' attribute.

		When any variant of the alphanumeric
		version is used, the column value is
		assumed to be indexed from 1.

		>>> parseKey('a1')
		(0, 0)

		>>> parseKey(['b', '2'])
		(1, 1)

		>>> parseKey([3, 6])
		(3, 6)

		>>> parseKey(['bb', 6])
		(53, 5)

		>>> parseKey(State(0,1))
		a2

		>>> parseKey(State('b',1))
		b1

		>>> parseKey(State('b1'))
		b1
	"""
	if isinstance(key, State):
		return key
	if isinstance(key, (basestring, str)):
		x = letterToIndex(key[0:1])
		y = int(key[1:])-1
	elif len(key) == 2:
		x, y = key
		if isinstance(x, (basestring, str)):
			x = letterToIndex(x)
			y = int(y) - 1
	else:
		raise TypeError

	return x, y


class StochasticAction(object):
	def __init__(self, symbol, outcomes):
		self._outcomes = outcomes
		self.action = outcomes[0][0]
		self.symbol = symbol

	def __str__(self):
		return self.symbol

	def __repr__(self):
		return 'StochasticAction('+repr(self.symbol)+','+repr(self._outcomes)+')'
	
	def move(self, world, state):
		return self.action.move(world, state)

	def outcomes(self, world, state):
		return self.combine_outcomes( [Outcome(a.move(world, state), p) 
			for (a, p) in self._outcomes])

	def combine_outcomes(self, uncombined):
		# split the outcomes into buckets based on the state of the outcome;
		# outcomes with the same state can then be combined
		stateMap = dict()
		for o in uncombined:
			s = str(o.state)
			if s in stateMap:
				stateMap[s].append(o)
			else:
				stateMap[s] = [o]

		result = []
		for outcomes in stateMap.values():
			o = outcomes[0]
			for i in xrange(1,len(outcomes)):
				o = (o + outcomes[i])
			result.append(o)

		return result

class Action(object):
	def __init__(self, symbol, xStep=0, yStep=0):
		self.xStep = xStep
		self.yStep = yStep
		self.symbol = symbol
	
	def __str__(self):
		return self.symbol

	def __repr__(self):
		return 'Action('+repr(self.symbol)+','+repr(self.xStep)+','+repr(self.yStep)+')'

	def outcomes(self, world, state):
		return [Outcome(self.move(world, state), 1.0)]
	
	def move(self, world, state):
		newState = (state.x + self.xStep), (state.y + self.yStep)
		if newState in world and not world.isImpasse(newState):
			return world.state(newState)
		else:
			return state

class Outcome(object):
	""" An outcome for a particular action. The resultant 
		state and probability are contained here. """
	def __init__(self, state, probability):
		self.state = state
		self.p = probability
	
	def combinesWith(self, other):
		return self.state == other.state

	def combine(self, other):
		assert self.combinesWith(other)

		return Outcome(self.state, self.p + other.p)

	def __add__(self, other):
		return self.combine(other)

	def __repr__(self):
		return "Outcome["+str(self.state)+", probability="+str(self.p)+"]"

class AbsorbingValue(object):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return'%+d' % self.value
	def __repr__(self):
		'AbsorbingValue('+repr(self.value)+')'

class Obstacle(object):
	def __init__(self,symbol):
		self.symbol = symbol
	def __repr__(self):
		return 'Obstacle('+repr(self.symbol)+')'
	def __str__(self):
		return str(self.symbol)

class State(object):
	""" A location in the Grid World. It should be immutable (x and y not changed).
		It's value can change, but that state is owned by the World object, not the 
		State.
	"""
	def __init__(self, x, y=None):

		if y is None:
			self.x, self.y = parseKey(x)
		else:
			self.x, self.y = parseKey((x, y))

	def __eq__(self, other):
		return isinstance(other, State) \
				and self.x == other.x \
				and self.y == other.y

	def __hash__(self):
		return 13*hash(self.x) + 17*hash(self.y)

	def __repr__(self):
		return indexToLetter(self.x) + str(self.y+1) 

	def __len__(self):
		""" The number of coordinates - always 2 (row and column) """
		return 2

	def __getitem__(self, key):
		""" You can access the row index using self[0] notation 
			and the column with self[1] """
		if key == 0:
			return self.x
		elif key == 1:
			return self.y
		else:
			raise IndexError

GOAL = AbsorbingValue(100)
TRAP = AbsorbingValue(-100)
BLOCK = Obstacle('[___]')

class World(object):
	""" A simple Grid world """

	N = Action('N', -1, 0)
	S = Action('S', 1, 0)
	E = Action('E', 0, 1)
	W = Action('W', 0, -1)

	NE = Action('NE', -1, 1)
	NW = Action('NW', -1, -1)
	SE = Action('SE', 1, 1)
	SW = Action('SE', 1, -1)

	NORTH = StochasticAction('N*', [ (N, .8), (E, .1), (W, .1)])
	SOUTH = StochasticAction('S*', [ (S, .8), (E, .1), (W, .1) ])
	EAST = StochasticAction('E*', [ (E, .8), (N, .1), (S, .1) ])
	WEST = StochasticAction('W*', [ (W, .8), (N, .1), (S, .1) ])

	# Example of using non-cardinal directions:
	# NORTH = StochasticAction('NORTH', [ (N, .6), (E, .1), (W, .1), (NE, .1), (NW, .1) ])

	def __init__(self,numRows=3, numCols=4, colWidth=7,numFmt='%.0f', actions=None, motionCost=-3,defaultValues=None):
		self.w = [[0]*numCols for i in xrange(numRows)]
		self.numCols = numCols
		self.numRows = numRows
		self.colWidth = colWidth
		self.numFmt = numFmt
		self.actions = actions \
				if actions is not None \
				else [World.NORTH, World.SOUTH, World.EAST, World.WEST]
		self.motionCost = motionCost

		if defaultValues:
			for key, value in defaultValues:
				self[key] = value

	def __repr__(self):
		return '<' + repr(self.w) + '>'

	def __str__(self):
		def formatValue(value, x, y):
			if isinstance(value, (Obstacle, AbsorbingValue)):
				v = str(value)
			else:
				v = (self.numFmt % value)
			return v

		return self.formatGrid(formatValue)

	def formatGrid(self,formatValue):
		colWidth = self.colWidth
		numCols = self.numCols
		numRows = self.numRows
		numFmt = self.numFmt
		w = self.w
		colfmt = '{0:^' + str(colWidth) + 's}'

		buf = []
		buf.append(colfmt.format(''))

		# column numbers
		for i in xrange(numCols):
			buf.append(colfmt.format(str(i+1)))
		buf.append('\n')

		buf.append('-' * ((numCols+1)*colWidth))
		buf.append('\n')

		for j in xrange(numRows):
			# row number
			buf.append(colfmt.format(str(indexToLetter(j)+' |')))
			r = w[j]

			# column values
			for i in xrange(numCols):
				buf.append( colfmt.format( formatValue(r[i], j, i) ) )
			buf.append('\n')

		return ''.join(buf)

	def state(self, x, y = None):
		if y is None:
			if isinstance(x, State):
				return x
			newX, newY = parseKey(x)
			return State(newX, newY)
		else:
			return State(x, y)

	def __getitem__(self, key):
		x, y = parseKey(key)
		return self.w[x][y]

	def __setitem__(self, key, value):
		x, y = parseKey(key)
		self.w[x][y] = (value)
	
	def __contains__(self, key):
		x, y = parseKey(key)
		return (x >= 0 and x < self.numRows) \
				and (y >= 0 and y < self.numCols)
	
	def isAbsorbing(self, key):
		return isinstance(self[key], AbsorbingValue)

	def isImpasse(self, key):
		return isinstance(self[key], Obstacle)

	def value(self, key):
		v = self[key]
		if isinstance(v, AbsorbingValue):
			return v.value
		return v

	def V(self, state, gamma=1.0):
		return max([ (gamma * sum( ( o.p * self.value(o.state) ) 
			for o in a.outcomes(self, state)) ) 
			for a in self.actions]) + self.R(state)	

	def R(self, state):
		if self.isAbsorbing(state):
			return self[state].value
		return self.motionCost

	def possible_moves(self, state):
		world = self
		actions = world.actions
		return [s for s in [a.move(world, state) for a in actions] if s != state]

	def action_values(self, state):
		assert not self.isAbsorbing(state) \
				and not self.isImpasse(state), \
				'state is absorbing or impasse: ' + str(state)
		return [(a, sum( [o.p * self.value(o.state) for o in a.outcomes(self,state)]))  for a in self.actions]

	def best_action(self, state):
		best_action = None
		best_value = None
		for action, value in self.action_values(state):
			if best_action is None or value > best_value:
				best_action, best_value = action, value
		return (best_action, best_value)

	def print_policy(self):
		def formatValue(value, i, j):
			if isinstance(value, (Obstacle, AbsorbingValue)):
				v = str(value)
			else:
				v = str(self.best_action(State(i,j))[0])
			return v


		print self.formatGrid(formatValue)


	def states_reachable_from(self,initial):
		"""Returns all of the states reachable from initial in the 
			world (using tree-search algorithm / breadth-first)"""

		assert not (self.isImpasse(initial) or self.isAbsorbing(initial)), \
				'initial state is not occupyable: ' + initial

		frontier = []
		explored = []
		frontier.append(self.state(initial))
		
		while frontier:
			s = self.state(frontier.pop(0))
			for f in self.possible_moves(s):
				if not self.isAbsorbing(f) \
						and f not in explored \
						and f not in frontier:
					frontier.append(f)
			explored.append(s)
		return explored
	
	def value_iter(self, initial, delta = 0):
		""" Performs the value iteration routine until convergence.
			The delta parameter controls how little difference implies convergence
			(the default value is 0).

			The initial parameter is the starting position (should be next to the goal)
		"""
		states = self.states_reachable_from(initial)

		iterations = 0
		while True:
			iterations += 1
			last_val = self[initial]
			for s in states:
				self[s] = self.V(s)
			if abs(self[initial] - last_val) <= delta:
				break # converged
		return iterations

	def randomize(world, p_goal=.01, p_pit=.01, p_block=.01):
		""" Randomize the world using the probabilities. """
		rows = world.numRows
		cols = world.numCols

		a = p_goal
		b = p_goal + p_pit
		c = p_goal + p_pit + p_block

		for x in xrange(rows):
			for y in xrange(cols):
				n = random.random()
				s = (x, y)
				if n >= 0 and n < a:
					world[s] = GOAL 
				elif n >= a and n < b:
					world[s] = TRAP 
				elif n >= b and n < c:
					world[s] = BLOCK
				else:
					world[s] = 0

	def set_range(self, val, row_range, col_range):
		""" Make each (i,j) where i is in row_range and j is in col_range equal to val.
			For example, set_range(BLOCK,xrange(0,5), xrange(3,6)) would make the squares
			in the ranges BLOCKs).
		"""
		for i in row_range:
			for j in col_range:
				self[(i,j)] = val

def grid_world():
	""" The Grid World from the video lectures:
		
>>> w = grid_world()
>>> w.value_iter('a3')
28
>>> print w
          1      2      3      4   
-----------------------------------
  a |    85     89     93    +100  
  b |    81    [___]   68    -100  
  c |    77     73     70     47   
<BLANKLINE>
"""
	return World(numRows=3, numCols=4,
			defaultValues=[('b2',BLOCK),('a4',GOAL),('b4',TRAP)])



def crazyWorld(rows=26, cols=26):
	world = World(rows, cols)
	world.randomize()
	return world

def testIt():
	world = grid_world()
	print world

	c1 = world.state(2,0)
	print c1
	print World.NORTH.outcomes(world, c1)

	b3 = world.state(1,2)
	print b3
	print World.WEST.outcomes(world, b3)

	a3 = world.state('a3')
	print "a3 = " + str(a3)
	print "outcomes for E from a3: " + str(World.EAST.outcomes(world, a3))
	print "V(a3) = " + str(world.V(a3))
	print world

	world[a3] = world.V(a3)
	print world

	b3 = world.state('b',3)
	print "V(" + str(b3) + ") = " + str(world.V(b3))

	world[b3] = world.V(b3)
	print world

	print "Value iteration until convergence ..."
	world = grid_world()
	iterations = world.value_iter('a3')
	print "Converged in {0} iterations".format(iterations)
	print world

	N1 = StochasticAction('N', [ (World.N, .8), (World.S, .2) ])
	S1 = StochasticAction('S', [ (World.S, .8), (World.N, .2) ])
	E1 = StochasticAction('E', [ (World.E, .8), (World.W, .2) ])
	W1 = StochasticAction('W', [ (World.W, .8), (World.E, .2) ])

	w = World(numRows=2,numCols=4,actions=[N1,S1,E1,W1],motionCost=-4,defaultValues=[('b4',GOAL),('b1',TRAP)])
	w.value_iter('a4')
	print w
	w.print_policy()	

import doctest
doctest.testmod()

