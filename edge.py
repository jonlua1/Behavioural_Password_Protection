import os
import sqlite3
from browser import Browser
from check_running_process import check_running_process

class Edge(Browser):
    def __init__(self):
        super().__init__()

    #note: only can work for NEW microsoft edge (v79+)
    #to get Microsoft Edge History file
    #returns string of path of Edge History file
    #if file doesnt exist return None
    def locate_history(self):
        edge_path = os.path.join(os.getenv('LOCALAPPDATA'), r'Microsoft\Edge\User Data\Default')
        edge_history = os.path.join(edge_path, "History")
        if(os.path.isfile(edge_history)):
            self._history_path = edge_history
            return edge_history
        else: 
            return None
    
    #get words from keyword_search_terms table in history file
    def get_keyword_search_terms(self):
        #checks if edge process is running    
        if(check_running_process('msedge')):
            print("Please exit all edge processes and retry again")
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
        #checks if edge process is running    
        if(check_running_process('msedge')):
            print("Please exit all edge processes and retry again")
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
        with open("edge_words.txt", "w", encoding="utf-8") as f:
            for ele in self._keywords:
                str1 += ele
            f.write(str1)
