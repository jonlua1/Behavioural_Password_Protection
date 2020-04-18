from abc import ABC, abstractmethod

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
