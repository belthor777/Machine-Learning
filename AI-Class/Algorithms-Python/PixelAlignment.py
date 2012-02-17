"""Attempt to implement pixel correspondence from scan lines
as described in Unit 17-26.
"""

# Convenience constants for making examples
black = 'B'
blue = 'U'
red = 'R'
b = black
r = red

def align(left, right, \
		bad_match_cost, occlusion_cost, good_match_cost=0):
	""" Print the pixel correspondence 
		between left and right camera scan lines
		(that is, align the scan lines)

	Quiz from Unit 17-16 (note: there are multiple correct answers for 
	this as explained in the aiqus forums):
	>>> left = [b,b,r,r,r,b]
	>>> right = [b,r,r,r,r,b]
	>>> a = align(left, right, 20, 5)
	>>> print_align(a)
	1 2 3 4 5 6 
	B B R R R B 
	|  / / /  | 
	B R R R R B 
	cost=10

	Unit 17-17 (this works):
	>>> left = [b,r,b,b,b,b]
	>>> right = [b,b,b,b,r,b]
	>>> a = align(left, right, bad_match_cost=20, occlusion_cost=10)
	>>> print_align(a)
	1 2 3 4 5 6 
	B R B B B B 
	|  / / /  | 
	B B B B R B 
	cost=20

	Other examples (just made up):
	>>> left = [b,b,b,b,b,r,r]
	>>> right = [r,r,b,b,b,b,r]
	>>> a = align(left, right, 20, 10)
	>>> a
	((40, [('bad_match', (0, 0), 20), ('right_occl', (0, 1), 30), ('good_match', (1, 2), 30), ('good_match', (2, 3), 30), ('good_match', (3, 4), 30), ('good_match', (4, 5), 30), ('good_match', (5, 6), 30), ('left_occl', (6, 6), 40)]), ['B', 'B', 'B', 'B', 'B', 'R', 'R'], ['R', 'R', 'B', 'B', 'B', 'B', 'R'])
	>>> print_align(a)
	1 2 3 4 5 6 7 
	B B B B B R R 
	|  \ \ \ \ \  
	R R B B B B R 
	cost=40

	>>> left = [b,b,blue,r,r,r,b,b]
	>>> right = [b,b,r,r,r,blue,b,b]
	>>> a = align(left, right, 20, 10)
	>>> print_align(a)
	1 2 3 4 5 6 7 8 
	B B U R R R B B 
	| |  / / /  | | 
	B B R R R U B B 
	cost=20
	"""
	def match(i, j):
		if left[i] == right[j]:
			return good_match_cost, 'good_match'
		return bad_match_cost, 'bad_match'

	def ismatch(action):
		return action == 'good_match' or action == 'bad_match'

	def best_tuple(value_path_action_tuples):
		best_tuple = None
		for t in value_path_action_tuples:
			val, path, action = t
			if best_tuple is None:
				best_tuple = t
			else:
				best_val, best_path, best_action = best_tuple
				if val < best_val:
					best_tuple = t
				elif val == best_val:
					path_action, path_coords, path_val = path[0]
					if ismatch(path_action):
						best_tuple = t
		return best_tuple

	cache = dict()

	def value(i, j):
		if (i, j) in cache:
			return cache[(i, j)]

		tuples = []
		if i >= 0 and j >= 0:
			match_val, match_path = value(i-1, j-1)
			match_cost = match(i, j)
			match_val += match_cost[0]
			tuples.append( (match_val, match_path, match_cost[1]) )
		if i >= 0:
			horiz_occl_val, horiz_occl_path = value(i-1, j)
			horiz_occl_val += occlusion_cost
			tuples.append( (horiz_occl_val, horiz_occl_path,'left_occl') )
		if j >= 0:
			vert_occl_val, vert_occl_path = value(i, j-1)
			vert_occl_val += occlusion_cost
			tuples.append( (vert_occl_val, vert_occl_path, 'right_occl') )

		if tuples:
			best_val, best_path, best_action = best_tuple(tuples)
			my_path = list(best_path)

			# mlake sure to append our best to the existing path
			my_path.append( (best_action, (i, j), best_val) )
			result = best_val, my_path
		else:
			result = 0, []

		cache[(i, j)] = result
		return result

	n = len(left)-1

	return value(n, n), left, right

def print_align(alignment):
	"""
	Pretty-prints the results of the align() function.

	Ex.
	B B U R R R B B
  | |  / / /  | |
	B B R R R U B B
	"""
	cost, path = alignment[0]
	left, right = alignment[1:]
	n = len(left)

	result = []
	for i in xrange(n):
		result.append( '%d ' % (i+1) )
	result.append('\n')
	for p in left:
		result.append( '%s ' % p )
	result.append('\n')
	for action, coord, cost in path:
		if action == 'right_occl' or action == 'left_occl':
			result.append( ' ' )
		elif action == 'good_match' or action == 'bad_match':
			i, j = coord
			if i == j:
				result.append('| ')
			elif i > j:
				result.append('/ ')
			else:
				result.append('\\ ')
	result.append('\n')

	for p in right:
		result.append( '%s ' % p )
	result.append('\n')
	result.append('cost=%d' % cost)
	
	print ''.join(result)

if __name__ == '__main__':
	import doctest
	doctest.testmod()

