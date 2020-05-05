from abc import ABC, abstractmethod
from text_processing import clean_text

class Browser(ABC):
    def __init__(self):
        self._history_path = ""
        self._keywords = []
        self._visit_time = 0
        self._past_keywords = []

    @property
    def history_path(self):
        return self._history_path

    @property
    def keywords(self):
        return self._keywords

    @property
    def visit_time(self):
        return self._visit_time
    
    @property
    def past_keywords(self):
        return self.past_keywords

    @abstractmethod
    def locate_history(self):
        pass

    @abstractmethod
    def generate_keywords(self):
        pass

    #clean the keywords list generated to get a list of possible keywords
    def process_keywords(self):
        self._keywords = clean_text(self._keywords)

    #from a list of words, return a dictionary of word-frequency pairs
    def keywords_to_freq_dict(self, keywords):
        wordfreq = {}
        for word in keywords:
            if(word in wordfreq):
                wordfreq[word] += 1
            else:
                wordfreq[word] = 1
        return wordfreq

    #add keywords and freq list into the dict
    def add_keywords_to_dict(self, keywords, dictionary):
        for word in keywords:
            word = word.replace('(', '').replace(')', '').replace("'", '')
            freq, keyword = word.split(', ')
            if keyword in dictionary:
                dictionary[keyword] += int(freq)
            else:
                dictionary[keyword] = int(freq)
        return dictionary

    #sort a dict of word-freq pairs in order of descending freq
    def sort_freq_dict(self, freqdict):
        sorted_dict = [(freqdict[key], key) for key in freqdict]
        sorted_dict.sort()
        sorted_dict.reverse()
        return sorted_dict