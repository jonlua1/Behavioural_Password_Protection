import os
import sqlite3
from browser import Browser
from check_running_process import check_running_process

class Opera(Browser):
    def __init__(self):
        super().__init__()

    #to get Opera History file
    #returns string of path of Opera History file
    #if file doesnt exist return None
    def locate_history(self):
        opera_path = os.path.join(os.getenv('APPDATA'), r'Opera Software\Opera Stable')
        opera_history = os.path.join(opera_path, "History")
        if(os.path.isfile(opera_history)):
            self._history_path = opera_history
            return opera_history
        else: 
            return None

    #to get last visit_time from opera log file
    def get_visit_time_from_file(self):
        #opera log file path
        opera_log_file = os.path.expanduser('~\Documents\ezPass\Logs\opera_logs.txt')

        #ezPass logs folder path
        folder_path = os.path.expanduser('~\Documents\ezPass\Logs')
        os.chdir(folder_path)

        visit_time = None
        #check if opera log file is available
        #get visit_time value from log file
        if(os.path.isfile(opera_log_file)):
            with open('opera_logs.txt', "r") as f:
                for line in f:
                    if 'VISIT_TIME' in line:
                        try:
                            visit_time = int(line.split(':')[1])
                        except ValueError:
                            pass
        
        if(visit_time != None):
            self._visit_time = visit_time

    #write the latest visit_time to opera log file
    def write_visit_time(self):
        #checks if opera process is running    
        if(check_running_process('opera')):
            print("Please exit all opera processes and retry again")    #NEED TO OUTPUT THIS
            return
        else:
            #connect to opera history db
            conn = sqlite3.connect(self._history_path)
            c = conn.cursor()
            #get search term results
            c.execute("""SELECT MAX(visit_time) FROM visits""")
            rows = c.fetchall()

            visit_time = rows[0][0]
            conn.commit()
            conn.close()        #close opera history db

            #opera log file path
            opera_log_file = os.path.expanduser('~\Documents\ezPass\Logs\opera_logs.txt')

            #ezPass logs folder path
            folder_path = os.path.expanduser('~\Documents\ezPass\Logs')
            os.chdir(folder_path)

            str1 = "VISIT_TIME:" + str(visit_time) +"\n"

            with open('opera_logs.txt', "w") as f:
                f.write(str1)

    #get words from keyword_search_terms table in history file
    def get_keyword_search_terms(self):
        #checks if opera process is running    
        if(check_running_process('opera')):
            print("Please exit all opera processes and retry again")    #NEED TO OUTPUT THIS
            return
        else:
            #connect to opera history db
            conn = sqlite3.connect(self._history_path)
            c = conn.cursor()
            #get search term results
            c.execute("""SELECT normalized_term FROM keyword_search_terms WHERE url_id IN 
                            (SELECT url from visits WHERE visit_time > ?)""", (self._visit_time,))
            words = c.fetchall()

            str1 = ""
            for tup in words:
                word = tup[0]
                str1 += word + ' '

            self._keywords.append(str1)

            conn.commit()
            conn.close()        #close opera history db

            
    #get words from urls table in history file
    def get_title(self):
        #checks if opera process is running    
        if(check_running_process('opera')):
            print("Please exit all opera processes and retry again")
            return
        else:
            conn = sqlite3.connect(self._history_path)
            c = conn.cursor()
            c.execute("""SELECT title FROM urls WHERE id IN 
                            (SELECT url from visits WHERE visit_time > ?)""", (self._visit_time,))
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
        #opera keyword file path
        opera_keyword_file = os.path.expanduser('~\Documents\ezPass\Keywords\opera_keywords.txt')

        #ezPass keywords folder path
        folder_path = os.path.expanduser('~\Documents\ezPass\Keywords')
        os.chdir(folder_path)

        past_keywords = []
        #check if opera keywords file is available
        #get keywords list from keywords file
        if(os.path.isfile(opera_keyword_file)):
            with open('opera_keywords.txt', "r") as f:
                past_keywords = f.readlines()
                past_keywords = [x.strip() for x in past_keywords]      #remove whitespace characters

        self._past_keywords = past_keywords

    #write the keywords list and frequency to file for future uses
    def write_keyword_freq_to_file(self, sorted_dict):
        #opera keyword file path
        opera_keyword_file = os.path.expanduser('~\Documents\ezPass\Keywords\opera_keywords.txt')

        #ezPass keywords folder path
        folder_path = os.path.expanduser('~\Documents\ezPass\Keywords')
        os.chdir(folder_path)

        str1 = ""
        for tup in sorted_dict:
            str1 += str(tup) + "\n"

        with open('opera_keywords.txt', "w") as f:
            f.write(str1)

    #generate keywords list from keyword search terms and titles
    def generate_keywords(self):
        history_file_path = self.locate_history()
        #if Opera history file does not exist
        if(history_file_path == None):
            print("Opera file not found!")      #NEED TO OUTPUT THIS
            return None

        self.get_visit_time_from_file()
        self.get_keyword_search_terms()
        self.get_title()
        self.write_visit_time()
        self.process_keywords()

        #obtain past keywords and freq list
        self.get_keywords_from_file()

        freq_dict = self.keywords_to_freq_dict(self._keywords)
        updated_dict = self.add_keywords_to_dict(self._past_keywords, freq_dict)

        sorted_dict = self.sort_freq_dict(updated_dict)

        #update opera keywords file with updated keywords and freq list
        self.write_keyword_freq_to_file(sorted_dict)

        keywords_for_password = []
        for tup in sorted_dict:
            if tup[0] != 1:
                keywords_for_password.append(tup[1])
        
        return keywords_for_password