This README file is a duplicate of the following aiqus.com post:
http://www.aiqus.com/questions/31667/source-code-used-for-ai-class

https://bitbucket.org/les2/aiclass/src

There is the source code I used throughout the course. There are the following files:

    PixelAlignment.py - pixel correspondence from scan lines
    KMeans.py - k-means algorithm as well as guassian and multivariate guassian regressions
    Sched.py - task network scheduling
    Smooth.py - Laplacian smoother that also does Markov chains (e.g., 'ABBBAAABA', what's P(A followed by A)
    ValIter.py - value iteration algorithm for MDP / grid world; you can customize the actions allowed (e.g., N/S/E/W or NE/NW/SE/SW) and combine stochastic and deterministic actions; the state space is only two dimensions so it will not handle a heading
    LinearFilter.py - convolve and image with a kernel
    LinearRegression.py - linear regression (find the w0 and w1)

I used these programs for the homeworks / exams, so they work for the examples in class. They're documented to varying degrees and typically includes pydoc tests (unit tests embedded in the documentation).

I'm not a Python expert, so the code is definitely rough around the edges. Some of it is definitely quick-and-dirty. I like to think that the code because more 'pythonic' with time. Python is definitely way better than Java in terms of ease of use (and I say that as a Java expert).

I use Python 2.6.5 in Cygwin, so I know that will work. Your mileage will vary with other versions of Python.

For the Python novices, use python -i {file name} to load one of the files in the Python REPL (read-evaluate-print-loop). That makes it easy to play around with the code.

Let me know if you have problems getting started or if you have suggestions.

===================
  You Might Need
===================
	Python 2.6.5 Reference http://docs.python.org/release/2.6.5/
		Start here if you are new to Python. If there is something in the source code that you don't understand, try
		to find it in the reference. Check out the tutorials!

	Cygwin http://www.cygwin.com/
		You will need this if you are a Microsoft Windows user and want to do serious programming.
		This is probably the EASIEST WAY TO INSTALL PYTHON ON WINDOWS. Cygwin allows you to install Python
		using its installer.

	GVim http://www.vim.org/download.php
		The best text editor on the planet (and possibly in the universe).

