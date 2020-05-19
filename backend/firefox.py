import os
import sqlite3
import configparser

from backend.browser import Browser
from backend.check_running_process import check_running_process

class Firefox(Browser):
    def __init__(self):
        super().__init__()

    #to get Mozilla Firefox History file
    #returns string of path of Chrome History file
    #if file doesnt exist return None
    def locate_history(self):
        #to get Mozilla Profile path
        mozilla_profile = os.path.join(os.getenv('APPDATA'), r'Mozilla\\Firefox')
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

    #to get last visit_time from firefox log file
    def get_visit_time_from_file(self):
        #firefox log file path
        firefox_log_file = os.path.expanduser('~\Documents\ezPass\Logs\\firefox_logs.txt')

        #ezPass logs folder path
        folder_path = os.path.expanduser('~\Documents\ezPass\Logs')
        os.chdir(folder_path)

        visit_time = None
        #check if firefox log file is available
        #get visit_time value from log file
        if(os.path.isfile(firefox_log_file)):
            with open('firefox_logs.txt', "r") as f:
                for line in f:
                    if 'VISIT_TIME' in line:
                        try:
                            visit_time = int(line.split(':')[1])
                        except ValueError:
                            pass
        
        if(visit_time != None):
            self._visit_time = visit_time
    
    #write the latest visit_time to firefox log file
    def write_visit_time(self):
        #checks if firefox process is running    
        if(check_running_process('firefox')):
            return
        else:
            #connect to firefox history db
            conn = sqlite3.connect(self._history_path)
            c = conn.cursor()
            #get search term results
            c.execute("""SELECT MAX(visit_date) from moz_historyvisits""")
            rows = c.fetchall()

            visit_time = rows[0][0]
            conn.commit()
            conn.close()        #close firefox history db

            #firefox log file path
            firefox_log_file = os.path.expanduser('~\Documents\ezPass\Logs\\firefox_logs.txt')

            #ezPass logs folder path
            folder_path = os.path.expanduser('~\Documents\ezPass\Logs')
            os.chdir(folder_path)

            str1 = "VISIT_TIME:" + str(visit_time) +"\n"

            with open('firefox_logs.txt', "w") as f:
                f.write(str1)

    #get words from urls table in history file
    def get_title(self):
        #checks if firefox process is running    
        if(check_running_process('firefox')):
            return
        else:
            conn = sqlite3.connect(self._history_path)
            c = conn.cursor()
            c.execute("""SELECT title FROM moz_places WHERE id IN  
                            (SELECT place_id from moz_historyvisits WHERE visit_date > ?)
                            AND title IS NOT NULL""", (self._visit_time,))
            words = c.fetchall()

            str1 = ""
            for tup in words:
                word = tup[0]
                str1 += word + ' '
            
            self._keywords.append(str1)

            conn.commit()
            conn.close()

    #get previous keywords data from keywords file if available
    def get_keywords_from_file(self):
        #firefox keyword file path
        firefox_keyword_file = os.path.expanduser('~\Documents\ezPass\Keywords\\firefox_keywords.txt')

        #ezPass keywords folder path
        folder_path = os.path.expanduser('~\Documents\ezPass\Keywords')
        os.chdir(folder_path)

        past_keywords = []
        #check if firefox keywords file is available
        #get keywords list from keywords file
        if(os.path.isfile(firefox_keyword_file)):
            with open('firefox_keywords.txt', "r") as f:
                past_keywords = f.readlines()
                past_keywords = [x.strip() for x in past_keywords]      #remove whitespace characters

        self._past_keywords = past_keywords

    #write the keywords list and frequency to file for future uses
    def write_keyword_freq_to_file(self, sorted_dict):
        #firefox keyword file path
        firefox_keyword_file = os.path.expanduser('~\Documents\ezPass\Keywords\\firefox_keywords.txt')

        #ezPass keywords folder path
        folder_path = os.path.expanduser('~\Documents\ezPass\Keywords')
        os.chdir(folder_path)

        str1 = ""
        for tup in sorted_dict:
            str1 += str(tup) + "\n"

        with open('firefox_keywords.txt', "w") as f:
            f.write(str1)

    #generate keywords list from keyword search terms and titles
    def generate_keywords(self):
        history_file_path = self.locate_history()
        #if firefox history file does not exist
        if(history_file_path == None):
            return None

        self.get_visit_time_from_file()
        self.get_title()
        self.write_visit_time()
        self.process_keywords()

        #obtain past keywords and freq list
        self.get_keywords_from_file()

        freq_dict = self.keywords_to_freq_dict(self._keywords)
        updated_dict = self.add_keywords_to_dict(self._past_keywords, freq_dict)

        sorted_dict = self.sort_freq_dict(updated_dict)

        #update firefox keywords file with updated keywords and freq list
        self.write_keyword_freq_to_file(sorted_dict)

        keywords_for_password = []
        for tup in sorted_dict:
            if tup[0] != 1:
                keywords_for_password.append(tup[1])
        
        return keywords_for_password
