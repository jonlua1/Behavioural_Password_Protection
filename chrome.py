import os
import sqlite3
from browser import Browser
from check_running_process import check_running_process

class Chrome(Browser):
    def __init__(self):
        super().__init__()

    #to get Chrome History file path
    #returns string of path of Chrome History file
    #if file doesnt exist return None
    def locate_history(self):
        chrome_path = os.path.join(os.getenv('LOCALAPPDATA'), r'Google\Chrome\User Data\Default')
        chrome_history = os.path.join(chrome_path, "History")
        if(os.path.isfile(chrome_history)):
            self._history_path = chrome_history
            return chrome_history
        else: 
            return None
    
    #get words from keyword_search_terms table in history file
    def get_keyword_search_terms(self):
        #checks if chrome process is running    
        if(check_running_process('chrome')):
            print("Please exit all chrome processes and retry again")
            return
        else:
            conn = sqlite3.connect(self._history_path)
            c = conn.cursor()
            c.execute("SELECT normalized_term FROM 'keyword_search_terms'")
            words = c.fetchall()

            str1 = ""
            for tup in words:
                word = tup[0]
                str1 += word + ' '

            self._keywords.append(str1)

            conn.commit()
            conn.close()

    #get words from urls table in history file
    def get_title(self):
        #checks if chrome process is running    
        if(check_running_process('chrome')):
            print("Please exit all chrome processes and retry again")
            return
        else:
            conn = sqlite3.connect(self._history_path)
            c = conn.cursor()
            c.execute("SELECT title FROM 'urls'")
            words = c.fetchall()

            str1 = ""
            for tup in words:
                word = tup[0]
                str1 += word + ' '

            self._keywords.append(str1)

            conn.commit()
            conn.close()

    def print_words(self):
        str1 = ""
        with open("chrome_words.txt", "w", encoding="utf-8") as f:
            for ele in self._keywords:
                str1 += ele
            f.write(str1)
