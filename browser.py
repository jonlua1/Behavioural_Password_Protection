from abc import ABC, abstractmethod
from text_processing import clean_text

class Browser(ABC):
    def __init__(self):
        self._history_path = "";
        self._keywords = []

    @property
    def history_path(self):
        return self._history_path

    @property
    def keywords(self):
        return self._keywords
    
    @abstractmethod
    def locate_history(self):
        pass
    
    def process_keywords(self):
        self._keywords = clean_text(self._keywords)