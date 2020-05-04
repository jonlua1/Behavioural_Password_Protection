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
    
    #clean the keywords list generated to get a list of possible keywords
    def process_keywords(self):
        self._keywords = clean_text(self._keywords)
