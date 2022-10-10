import math, os, pickle, re
from typing import Tuple, List, Dict
class BayesClassifier:
    """A simple BayesClassifier implementation
    Attributes:
        pos_freqs - dictionary of frequencies of positive words
        neg_freqs - dictionary of frequencies of negative words
        pos_filename - name of positive dictionary cache file
        neg_filename - name of positive dictionary cache file
        training_data_directory - relative path to training directory
        neg_file_prefix - prefix of negative reviews
        pos_file_prefix - prefix of positive reviews
    """
    def __init__(self):
        """Constructor initializes and trains the Naive Bayes Sentiment Classifier.
If a
        cache of a trained classifier is stored in the current folder it is loaded,
        otherwise the system will proceed through training.  Once constructed the
        classifier is ready to classify input text."""
        # initialize attributes
        self.pos_freqs: Dict[str, int] = {}
        self.neg_freqs: Dict[str, int] = {}
        self.pos_filename: str = "pos.dat"
        self.neg_filename: str = "neg.dat"
        self.training_data_directory: str = "movie_reviews/"
        self.neg_file_prefix: str = "movies-1"
        self.pos_file_prefix: str = "movies-5"
        # check if both cached classifiers exist within the current directory
        if os.path.isfile(self.pos_filename) and os.path.isfile(self.neg_filename):
            print("Data files found - loading to use cached values...")
            self.pos_freqs = self.load_dict(self.pos_filename)
            self.neg_freqs = self.load_dict(self.neg_filename)
        else:
            print("Data files not found - running training...")
            self.train()
    def train(self) -> None:
        """Trains the Naive Bayes Sentiment Classifier
        Train here means generates `pos_freq/neg_freq` dictionaries with frequencies of
        words in corresponding positive/negative reviews
        """
        # get the list of file names from the training data directory
        # os.walk returns a generator (feel free to Google "python generators" if you're
        # curious to learn more, next gets the first value from this generator or the
        # provided default `(None, None, [])` if the generator has no values)
        _, __, files = next(os.walk(self.training_data_directory), (None, None, []))
        if not files:
            raise RuntimeError(f"Couldn't find path {self.training_data_directory}")
        #print(files)
        # the 'files' variable now holds a list of the filenames
        # self.training_data_directory holds the folder name where these files are
        #   located/stored
        
        # here is how you would load a file with filename given by `fName`
        # `text` here will be the literal text of the file (i.e. what you would see
        # if you opened the file in a text editor)
        for filename in files:
            if not filename.startswith("."):
                #print(f"File: '{filename}'")
                text = self.load_file(os.path.join(self.training_data_directory, filename))
                #print(f"Text of file: '{text}'")
                #deciding whether or not its a positive or negative review
                if self.pos_file_prefix in filename:
                    self.update_dict(self.tokenize(text), self.pos_freqs)
                if self.neg_file_prefix in filename:
                    self.update_dict(self.tokenize(text), self.neg_freqs)
        #print(f"Positive dictionary: \n{self.pos_freqs}")
        #print(f"Negative dictionary: \n{self.neg_freqs}")
        # *Tip:* training can take a while, to make it more transparent, we can usethe
        # enumerate function, which loops over something and has an automatic counter.
        # write something like this to track progress
        #for index, filename in enumerate(files, 1):
        #     print(f"Training on file {index} of {len(files)}")
        
        #     <the rest of your code for updating frequencies here>
        # Try enumerate at the interpreter first so that you can see how it works. 
        # we want to fill pos_freqs and neg_freqs with the correct counts of words from
        # their respective reviews
        
        # for each file, if it is a negative file, update (see the Updating frequencies
        # set of comments for what we mean by update) the frequencies in the negative
        # frequency dictionary. If it is a positive file, update (again see the Updating
        # frequencies set of comments for what we mean by update) the frequencies in the
        # positive frequency dictionary. If it is neither a postive or negative file,
        # ignore it and move to the next file (this is more just to be safe; we won't
        # test your code with neutral reviews)
        
        # Updating frequences: to update the frequencies for each file, you need toget
        # the text of the file, tokenize it, then update the appropriate dictionaryfor
        # those tokens. We've asked you to write a function `update_dict` that willmake
        # your life easier here. Write that function first then pass it your list of
        # tokens from the file and the appropriate dictionary
        
        # for debugging purposes, it might be useful to print out the tokens and their
        # frequencies for both the positive and negative dictionaries
        
        # once you have gone through all the files, save the frequency dictionariesto
        # avoid extra work in the future (using the save_dict method). The objects you
        # are saving are self.pos_freqs and self.neg_freqs and the filepaths to save to
        # are self.pos_filename and self.neg_filename
        self.save_dict(self.pos_freqs, self.pos_filename)
        self.save_dict(self.neg_freqs, self.neg_filename)
        
    def classify(self, text: str) -> str:
        """Classifies given text as positive, negative or neutral from calculating the
        most likely document class to which the target string belongs
        Args:
            text - text to classify
        Returns:
            classification, either positive, negative or neutral
        """
        # TODO: fill me out
        
        # get a list of the individual tokens that occur in text
        print("text to classify: {text}")
        tokenized_text = self.tokenize(text)
        neg_prob = 0
        pos_prob = 0
        neg_freqs_size = 0
        pos_freqs_size = 0
        for word in self.neg_freqs:
            neg_freqs_size += self.neg_freqs[word]
        #print(f"The size of the negative dictionary is : {neg_freqs_size}")
        for word in self.pos_freqs:
            pos_freqs_size += self.pos_freqs[word]
        #print(f"The size of the positive dictionary is : {pos_freqs_size}")
        for word in tokenized_text:
            try:
                neg_prob += math.log((self.neg_freqs[word] + 1)/neg_freqs_size)
                pos_prob += math.log((self.pos_freqs[word] + 1)/pos_freqs_size)
            except:
                neg_prob += math.log(1/neg_freqs_size)
                pos_prob += math.log(1/pos_freqs_size)
            #print(f"the neg prob is: {neg_prob}")
            #print(f"the pos prob is: {pos_prob}")
        if neg_prob > pos_prob:
            #print("This review is negative")
            return "negative"
        if pos_prob > neg_prob:
            #print("This review is positive")
            return "positive"
        if neg_prob == pos_prob:
            #print("This review is positive")
            return "positive"
##            print(f"File: '{filename}'")
##            text = self.load_file(os.path.join(self.training_data_directory, filename))
##            print(f"text of file: '(text)'")
##            if self.pos_file_prefix in filename:
##                self.update_dict(self.tokenize(text), self.pos_freqs)
##            if self.neg_file_prefix in filename:
##                self.update_dict(self.tokenize(text), self.neg_freqs)
        # create some variables to store the positive and negative probability. since
        # we will be adding logs of probabilities, the initial values for the positive
        # and negative probabilities are set to 0
        
        # get the sum of all of the frequencies of the features in each document class
        # (i.e. how many words occurred in all documents for the given class) - this
        # will be used in calculating the probability of each document class given each
        # individual feature
        
        # for each token in the text, calculate the probability of it occurring given a
        # postive document and given a negative document and add the logs of those to the
        # running sums. when calculating the probabilities, always add 1 to the numerator
        # of each probability for add one smoothing (so that we never have a probability
        # of 0)
        
        # determine whether positive or negative was more probable (i.e. which one was
        # larger)
        # if they are equal, assume "positive"
        
        # return a string of "positive" or "negative"
    def load_file(self, filepath: str) -> str:
        """Loads text of given file
        Args:
            filepath - relative path to file to load
        Returns:
            text of the given file
        """
        with open(filepath, "r", encoding='utf8') as f:
            return f.read()
    def save_dict(self, dict: Dict, filepath: str) -> None:
        """Pickles given dictionary to a file with the given name
        Args:
            dict - a dictionary to pickle
            filepath - relative path to file to save
        """
        print(f"Dictionary saved to file: {filepath}")
        with open(filepath, "wb") as f:
            pickle.Pickler(f).dump(dict)
    def load_dict(self, filepath: str) -> Dict:
        """Loads pickled dictionary stored in given file
        Args:
            filepath - relative path to file to load
        Returns:
            dictionary stored in given file
        """
        print(f"Loading dictionary from file: {filepath}")
        with open(filepath, "rb") as f:
            return pickle.Unpickler(f).load()
    def tokenize(self, text: str) -> List[str]:
        """Splits given text into a list of the individual tokens in order
        Args:
            text - text to tokenize
        Returns:
            tokens of given text in order
        """
        tokens = []
        token = ""
        for c in text:
            if (
                re.match("[a-zA-Z0-9]", str(c)) != None
                or c == "'"
                or c == "_"
                or c == "-"
            ):
                token += c
            else:
                if token != "":
                    tokens.append(token.lower())
                    token = ""
                if c.strip() != "":
                    tokens.append(str(c.strip()))
        if token != "":
            tokens.append(token.lower())
        return tokens
    def update_dict(self, words: List[str], freqs: Dict[str, int]) -> None:
        """Updates given (word -> frequency) dictionary with given words list
        By updating we mean increment the count of each word in words in the dictionary.
        If any word in words is not currently in the dictionary add it with a count of 1.
        (if a word is in words multiple times you'll increment it as many times
        as it appears)
        Args:
            words - list of tokens to update frequencies of
            freqs - dictionary of frequencies to update
        """
        #print(words)
        #sort the list of words into the dictionaries
        #for each word seperate it into the dictionary and each time it appears 
count the amount of times
        for word in words:
            if word in freqs:
                freqs[word] += 1
                #print(f"Frequency updated for {word}, frequency is now 
{freqs[word]}")
            else:
                freqs[word] = 1
                #print(f"Frequency not found for {word}, created at 1")
if __name__ == "__main__":
##    print("something happening")
##    # uncomment the below lines once you've implemented `update_dict` and `train`
##    b = BayesClassifier()
##
##    a_list_of_words = ["I", "really", "like", "this", "movie", ".", "I", "hope", \
##                       "you", "like", "it", "too"]
##    a_dictionary = {}
##    b.update_dict(a_list_of_words, a_dictionary)
##    assert a_dictionary["I"] == 2, "update_dict test 1"
##    assert a_dictionary["like"] == 2, "update_dict test 2"
##    assert a_dictionary["really"] == 1, "update_dict test 3"
##    assert a_dictionary["too"] == 1, "update_dict test 4"
##    print("update_dict tests passed.")
##
##    pos_denominator = sum(b.pos_freqs.values())
##    neg_denominator = sum(b.neg_freqs.values())
##
##    print("\nThese are the sums of values in the positive and negative dicitionaries.")
##    print(f"sum of positive word counts is: {pos_denominator}")
##    print(f"sum of negative word counts is: {neg_denominator}")
##
##    print("\nHere are some sample word counts in the positive and negative dicitionaries.")
##    print(f"count for the word 'love' in positive dictionary {b.pos_freqs['love']}")
##    print(f"count for the word 'love' in negative dictionary {b.neg_freqs['love']}")
##    print(f"count for the word 'terrible' in positive dictionary {b.pos_freqs['terrible']}")
##    print(f"count for the word 'terrible' in negative dictionary {b.neg_freqs['terrible']}")
##    print(f"count for the word 'computer' in positive dictionary {b.pos_freqs['computer']}")
##    print(f"count for the word 'computer' in negative dictionary {b.neg_freqs['computer']}")
##    print(f"count for the word 'science' in positive dictionary {b.pos_freqs['science']}")
##    print(f"count for the word 'science' in negative dictionary {b.neg_freqs['science']}")
##    print(f"count for the word 'i' in positive dictionary {b.pos_freqs['i']}")
##    print(f"count for the word 'i' in negative dictionary {b.neg_freqs['i']}")
##    print(f"count for the word 'is' in positive dictionary {b.pos_freqs['is']}")
##    print(f"count for the word 'is' in negative dictionary {b.neg_freqs['is']}")
##    print(f"count for the word 'the' in positive dictionary {b.pos_freqs['the']}")
##    print(f"count for the word 'the' in negative dictionary {b.neg_freqs['the']}")
##
##    print("\nHere are some sample probabilities.")
##    print(f"P('love'| pos) {(b.pos_freqs['love']+1)/pos_denominator}")
##    print(f"P('love'| neg) {(b.neg_freqs['love']+1)/neg_denominator}")
##    print(f"P('terrible'| pos) {(b.pos_freqs['terrible']+1)/pos_denominator}")
##    print(f"P('terrible'| neg) {(b.neg_freqs['terrible']+1)/neg_denominator}")
####
####    # uncomment the below lines once you've implemented `classify`
##    print("\nThe following should all be positive.")
##    print(b.classify('I love computer science'))
##    print(b.classify('this movie is fantastic'))
##    print("\nThe following should all be negative.")
##    print(b.classify('rainy days are the worst'))
##    print(b.classify('computer science is terrible'))
##
    pass
