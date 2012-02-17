from BayesFilter import BayesFilter

## Example data taken from Stanford AI video class (Unit 5 Machine Learning)
## http://www.ai-class.org

filter = BayesFilter()

## Add some messages we flagged as spam
filter.addDoc("offer is secret", "spam")
filter.addDoc("click secret link", "spam")
filter.addDoc("secret sports link", "spam")

## Add some messages we did not flag
filter.addDoc("play sports today", None)
filter.addDoc("went play sports", None)
filter.addDoc("secret sports event", None)
filter.addDoc("sports is today", None)
filter.addDoc("sports costs money", None)

filter.db.info()

print "Probability of spam, given message 'today is secret' = %s" % filter.predict("spam", "today is secret")

