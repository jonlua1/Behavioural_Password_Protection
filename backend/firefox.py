import os
import sqlite3
import configparser

from browser import Browser
from check_running_process import check_running_process

class Firefox(Browser):
    def __init__(self):
        super().__init__()

    #to get Mozilla Firefox History file
    #returns string of path of Chrome History file
    #if file doesnt exist return None
    def locate_history(self):
        #to get Mozilla Profile path
        mozilla_profile = os.path.join(os.getenv('APPDATA'), r'Mozilla\Firefox')
        mozilla_profile_ini = os.path.join(mozilla_profile, r'profiles.ini')

        if(os.path.exists(mozilla_profile_ini)):
            profile = configparser.ConfigParser()
            profile.read(mozilla_profile_ini)
            firefox_path = ""
            firefox_path = os.path.normpath(os.path.join(mozilla_profile, profile.get('Profile0', 'Path')))
            #to get Mozilla places file
            firefox_history = os.path.join(firefox_path, "places.sqlite")
            if(os.path.isfile(firefox_history)):
                self._history_path = firefox_history
                return firefox_history
            else: 
                return None
        else:
            return None
    
    #get words from moz_places table in history file
    def get_title(self):
        #checks if firefox process is running    
        if(check_running_process('firefox')):
            print("Please exit all firefox processes and retry again")
            return
        else:
            conn = sqlite3.connect(self._history_path)
            c = conn.cursor()
            c.execute("SELECT title FROM 'moz_places' WHERE title IS NOT NULL")
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
        with open("firefox_words.txt", "w", encoding="utf-8") as f:
            for ele in self._keywords:
                str1 += ele
            f.write(str1)