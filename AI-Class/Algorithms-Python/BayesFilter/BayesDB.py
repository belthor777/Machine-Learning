class BayesDB:

    ## **************
    ## *** Fields ***
    ## **************

    ## Frequency tables and related book-keeping
    wordToTotalFreq       = None
    labelToWordToFreq     = None
    labelToTotalWordCount = None
    uniqueWords           = None
    totalWordCount        = None
    uniqueWordCount       = None

    ## Docs/Labels DB
    allDocs = None
    labelToDocs = None

    ## **********************
    ## *** Public Methods ***
    ## **********************

    def addDoc(self, doc, label):
        """
        Adds a doc (just a string) to the DB.  Label is optional (if this
        doc is not labelled then just pass None).  Calling this method will
        update the probabilities according to the words in the document, and
        the presence/absence of a label.
        """
        self.allDocs.append(doc)

        for word in doc.split():
            self.__addWord(word)

        if label:
            self.__labelDoc(label, doc)

    def info(self):
        """
        Prints info on this DB.
        """
        print "Word->Total Freq: %s" % self.wordToTotalFreq
        print "Label->Word->Freq: %s" % self.labelToWordToFreq
        print "Label->Total Word Count: %s" % self.labelToTotalWordCount
        print "Unique Words: %s" % self.uniqueWords
        print "Total Word Count: %s" % self.totalWordCount
        print "Unique Word Count: %s" % self.uniqueWordCount
        print

    ## ***********************
    ## *** Private Methods ***
    ## ***********************

    def __init__(self):
        self.wordToTotalFreq       = {}
        self.labelToWordToFreq     = {}
        self.labelToTotalWordCount = {}
        self.uniqueWords           = set([])
        self.totalWordCount        = 0
        self.uniqueWordCount       = 0

        ## Docs/Labels DB
        self.allDocs = []
        self.labelToDocs = {}

    def __labelDoc(self, label, doc):
        ## Init label->docs if not already seen
        if label not in self.labelToDocs.keys():
            self.labelToDocs[label] = []
        self.labelToDocs[label].append(doc)

        for word in doc.split():
            ## Initialise label->word->freq if not already seen
            if label not in self.labelToWordToFreq.keys():
                self.labelToWordToFreq[label] = {}

            ## Increment word frequency for this label
            if word not in self.labelToWordToFreq[label].keys():
                self.labelToWordToFreq[label][word] = 1
            else:
                self.labelToWordToFreq[label][word] += 1

            ## Increment total word count for this label
            if label not in self.labelToTotalWordCount.keys():
                self.labelToTotalWordCount[label] = 1
            else:
                self.labelToTotalWordCount[label] += 1

    def __addWord(self, word):
        if word not in self.wordToTotalFreq:
            self.wordToTotalFreq[word] = 1
        else:
            self.wordToTotalFreq[word] += 1
            
        self.uniqueWords.add(word)
        self.uniqueWordCount = len(self.uniqueWords)
        self.totalWordCount += 1

