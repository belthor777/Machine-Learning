"""
Attempt at implemented the Laplacian smoother
discussed in the AI class
"""

class LaplacianSmoother(object):
	"""
	Suppose we have two labels, 'movie' and 'song' with the following
	titles in each:

	movie              song
	--------           -----------
	a perfect world    a perfect day
	my perfect woman   electric storm
	pretty woman       another rainy day

	To 'vocabulary' consists of the set of words used in both labels:
	vocab := { a, perfect, rainy, woman, electric, another, 
		storm, pretty, world, my, day }
	
	P(x) with Laplacian smoothing parameter k is given by:
		P(X=x) = count(x) + k / ( N + k*|X| ),
	where,
		X is a random variable
		count(x) is the number of times the variable occurs
		N is |vocab|, that is, the number of elements in the vocab set
		|X| is the  number of values the random variable can have

	To compute P(w1,w2,...,wn|label) we use:
		P(w1,w2,...,wn|label) = p(w1|label)*p(w2|label)*...*p(wn|label)
			since each wi is independent of all the other wi's given the label

	For a single word w, P(w|label) is given by:
		P(w|label) = count(w|label) + k / (N + | w|label | )
	
	To compute the reverse, that is, P(label|w1,w2,...,wn), we apply
	Baye's rule as follows:

		P(label|w1,w2,..,wn)=P(w1,w2,..,wn|label)*P(label)/P(w1,w2,..,wn)

	The terms in the numerator are computed as describe earlier. The
	denominator (the marginal likelihood), is computing using
	'Total Probability':

		P(w1,w2,..,wn)=P(w1,w2,..,wn|label_1) + P(w1,w2,..,wn|label_2)
									 ... + P(w1,w2,..,wn|label_m),

		where label_i is one of the labels, and each term in the sum
		is computed as desribed earlier.

	>>> ls = LaplacianSmoother({'movie' : ['a perfect world', 'my perfect woman','pretty woman'], 'song' : ['a perfect day', 'electric storm', 'another rainy day'] })

	>>> '%.4f' % ls.prob_term_given_label('movie','perfect')
	'0.1579'

	>>> '%.4f' % ls.prob_term_given_label('song','perfect')
	'0.1053'

	>>> '%.4f' % ls.prob_term_given_label('movie','storm')
	'0.0526'

	>>> '%.4f' % ls.prob_term_given_label('song','storm')
	'0.1053'

	>>> '%.4f' % ls.prob_label_given_terms('movie', ['perfect','storm'])
	'0.4286'

	Another example (Question 8 on the midterm exam):
	>>> ls = LaplacianSmoother({'old':['top gun','shy people','top hat'],'new':['top gear','gun shy']})

	>>> '%.4f' % ls.prob_label('old')
	'0.5714'

	>>> '%.4f' % ls.prob_label('new')
	'0.4286'

	>>> '%.4f' % ls.prob_term_given_label('old','top')
	'0.2500'

	>>> '%.4f' % ls.prob_label_given_terms('old', ['top'])
	'0.6250'

	>>> '%.4f' % ls.prob_terms(['top'])
	'0.2286'

	>>> '%.4f' % ls.prob_term_given_label('new', 'top')
	'0.2000'

	What about using Laplacian smoothing for a Markov chain?

	Given an input sequence: A B B A A B B A B A B A

	The first step is to break the input string into pairs:
		AB,BB,BA,AA,AB,BB,BA,AB,BA,AB,BA

	Then we should group them according to whether A or B is first:
	
	A              B         0
	---------     -------   --------
	B              B         A
	A              A
	B              B
	B              A
	B              A
	               A
	
	The column headings are the labels or map keys for the LaplacianSmoother.

	To compute the conditional probabilities for the sequence (one of
	the lecture quizzes): 'RSSSS'
	>>> ls = LaplacianSmoother('RSSSS')

	What is the probability that an S will be followed by an R?
	>>> '%.4f' % ls.prob_term_given_label('S', 'R')
	'0.2000'
	
	P(S will be followed by another S)
	>>> '%.4f' % ls.prob_markov_chain('SS')
	'0.8000'

	P(R will be followed by an S)
	>>> '%.4f' % ls.prob_markov_chain('RS')
	'0.6667'

	P(R will be followed by another R)
	>>> '%.4f' % ls.prob_term_given_label('R', 'R')
	'0.3333'

	The initial conditions can also be determined:

	P(initially get an R)
	>>> '%.4f' % ls.prob_markov_chain('R')
	'0.6667'

	P(initially get an S)
	>>> '%.4f' % ls.prob_term_given_label(None, 'S')
	'0.3333'

	Here's an example that uses a maximum likelihood estimate
	for an input sequence: 'RSSSRSR'

	>>> ls = LaplacianSmoother('RSSSRSR',k=0)

	To query initial conditions, use only 1 character:
	>>> '%.4f' % ls.prob_markov_chain('R')
	'1.0000'

	>>> '%.4f' % ls.prob_markov_chain('RR')
	'0.0000'
	
	>>> '%.4f' % ls.prob_markov_chain('RS')
	'1.0000'

	>>> '%.4f' % ls.prob_markov_chain('SS')
	'0.5000'

	>>> '%.4f' % ls.prob_markov_chain('SR')
	'0.5000'

	More maximum likelihood tests:
		>>> ls = LaplacianSmoother( { 'spam' : ['offer is secret','click secret link','secret sports link'], 'ham' : ['play sports today','went play sports','secret sports event','sports is today','sports costs money']},k=0)
		>>> len(ls.vocab())
		12
		>>> '%.4f' % ls.prob_label('spam')
		'0.3750'

		>>> '%.4f' % ls.prob_term_given_label('spam','secret')
		'0.3333'

		>>> '%.4f' % ls.prob_term_given_label('ham','secret')
		'0.0667'

		>>> '%.4f' % ls.prob_label_given_terms('spam',['sports'])
		'0.1667'

		>>> '%.4f' % ls.prob_label_given_terms('spam','secret is secret'.split())
		'0.9615'

		>>> '%.4f' % ls.prob_label_given_terms('spam','today is secret'.split())
		'0.0000'

		Now with Laplacian smoothing ...
		>>> ls.k = 1 # you can change k whenever
		>>> '%.4f' % ls.prob_label('spam')
		'0.4000'
		>>> '%.4f' % ls.prob_label('ham')
		'0.6000'
		>>> '%.4f' % ls.prob_term_given_label('spam','today')
		'0.0476'
		>>> '%.4f' % ls.prob_term_given_label('ham','today')
		'0.1111'
	"""

	def __init__(self, data, k=1):
		"""
			If the parameter data is a string, then it is assume
			to be an input sequence for a Markov chain, such as
			'RSSSS', and will be converted into the representation
			necessary, which for the above example is a the
			following dictionary:
				{'R',['S'],'S':['S','S','S'],None:['R']}

			In general, the format of data is a dictionary where
			the keys represent the labels and the values are the
			training data for those labels (a list of sentences).

			The value of k can be changed if necessary, and if
			set to 0, the probabilities returned degrade to
			the maximum likelihood estimate.
		"""
		self.data = dict()
		self.add_data(data)
		self.k = k
	def __repr__(self):
		return 'LaplacianSmoother('+repr(self.data)+','+repr(self.k)+')'

	def add_data(self, data):
		""" Adds another sample to the data. """
		if isinstance(data, (str,basestring)):
			data_map = dict([(w,[]) for w in set(data)])
			for i in xrange(len(data)-1):
				data_map[data[i]].append(data[i+1])
			data_map[None] = [data[0]] if data else []
		else:
			data_map = data

		for key, value in data_map.iteritems():
			if key in self.data:
				self.data[key].extend(value)
			else:
				self.data[key] = value

	def prob_terms(self, terms):
		p = 0.0
		for label in self.labels():
			p += (self.prob_terms_given_label(label, terms) * self.prob_label(label))
		return p

	def prob(self, count_x, N, x):
		# the smoothing parameter, duh
		k = self.k
		return float((count_x + k))/float(N + k*x)

	def prob_label(self, label):
		assert label in self.data, 'bad label: ' + str(label)

		# the number of labels
		x = float(len(self.data)) 

		# the number of entries for the label 
		count_x = float(len(self.data[label]))

		# the total number of entries (in all labels)
		N = float(sum( [len(self.data[l]) for l in self.labels()] ))

		return self.prob(count_x, N, x)

	def labels(self):
		return self.data.iterkeys()

	def vocab(self):
		result = set()
		for values in self.data.itervalues():
			for line in values:
				for w in self.atoms(line):
					result.add(w)
		return result

	def atoms(self, value):
		"""Break the value into the atomic values that make it up. For example, 
			if the value is a sentence, an array of words would be returned."""
		return value.split()

	def words_in_label(self, label):
		result = []
		for line in self.data[label]:
			for word in self.atoms(line):
				result.append(word)
		return result

	def prob_term_given_label(self, label, term):
		words_in_label = self.words_in_label(label)
		vocab = self.vocab()
		N = len(words_in_label)
		x = len(vocab)
		count_x = sum([1 for w in words_in_label if w == term])

		return self.prob(count_x, N, x)

	def prob_markov_chain(self, query):
		""" Convenience method for computing probabilities
			for Markov-chains, such as P(A followed by B), which
			could be found using prob_markov_chain('AB').
		"""

		size = len(query)
		assert size > 0 and size <= 2 , 'query length must be between 1 and 2: ' + str(query)

		if size == 1:
			return self.prob_term_given_label(None, query[0])
		else:
			return self.prob_term_given_label(query[0], query[1])

	def prob_terms_given_label(self, label, terms):
		p = None
		for t in terms:
			p_t = self.prob_term_given_label(label, t)
			if p is None:
				p = p_t
			else:
				p *= p_t
		return p

	def prob_terms(self, terms):
		p = 0.0
		for l in self.labels():
			# total probability:
			p += (self.prob_terms_given_label(l,terms)*self.prob_label(l))
		return p

	def prob_label_given_terms(self, label, terms):
		"Use Baye's rule to find P(label|t1, t2, ..., tn)"

		prior = self.prob_label(label)
		likelihood = self.prob_terms_given_label(label, terms)
		marginal_likelihood = self.prob_terms(terms)

		return likelihood * prior / marginal_likelihood

def example():
	data = {'movie' : ['a perfect world', 'my perfect woman','pretty woman'],\
		'song' : ['a perfect day', 'electric storm', 'another rainy day'] }
	s = LaplacianSmoother(data=data, k=1)
	return s

if __name__ == '__main__':
	import doctest
	doctest.testmod()
