"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Finding random words from dictionary
    >>> wf = WordFinder("/Users/student/words.txt")
        3 words read

    >>> wf.random()
        'cat'

    >>> wf.random()
       'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
       'dog'

    """

    def __init__(self,path):

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self,dict_file):
        """Parse dictionary file to list of words
        strip(): return the string without any spaces at the 
        beginning or the end.

        """

        return [words.strip() for words in dict_file]

    def random(self):
        """Return random word of self.words"""

        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
        >>> swf = SpecialWordFinder("complex.txt")
             3 words read

         >>> swf.random() in ["pear", "carrot", "kale"]
             True

         >>> swf.random() in ["pear", "carrot", "kale"]
             True

        >>> swf.random() in ["pear", "carrot", "kale"]
         True
    """
    def parse(self,dict_file):

        return[words.strip() for words in dict_file
                if words.strip() and not words.startswith("#")]

     