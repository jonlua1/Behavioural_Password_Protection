import os
from random import shuffle

from backend.chrome import Chrome
from backend.firefox import Firefox
from backend.edge import Edge
from backend.opera import Opera

from backend.wordlist_generator import Wordlist_Generator
from backend.dice import Dice

class Password_Generator():
    #initialise ezPass folder if it does not exist
    def init_folder(self):
        #ezPass folder path
        folder_path = os.path.expanduser('~\Documents\ezPass')
        logs_folder_path = os.path.expanduser('~\Documents\ezPass\Logs')
        keywords_folder_path = os.path.expanduser('~\Documents\ezPass\Keywords')

        #check if ezPass folder has been created
        if(not os.path.isdir(folder_path)):
            #create ezPass folder
            os.mkdir(folder_path)
            #change directory to folder path
            os.chdir(folder_path)
            #create logs folder
            os.mkdir(".\Logs")
            #create keywords folder
            os.mkdir(".\Keywords")

        #check if logs folder has been created
        if(not os.path.isdir(logs_folder_path)):
            #change directory to folder path
            os.chdir(folder_path)
            #create logs folder
            os.mkdir(".\Logs")
        
        #check if keywords folder has been created
        if(not os.path.isdir(keywords_folder_path)):
            #change directory to folder path
            os.chdir(folder_path)
            #create keywords folder
            os.mkdir(".\Keywords")  
        
    #generate possible passphrase based on alphabets given
    def generate_passphrase(self, wordlist, passphrase_length, alphabets = []):
        passphrase_list = []
        alpha_index = 0

        dice = Dice()
        #get words with the given alphabets
        while len(passphrase_list) < len(alphabets):
            roll = dice.dice_roll()
            word = wordlist[str(roll)]
            if word[0] == alphabets[alpha_index]:
                passphrase_list.append(word)
                alpha_index += 1
        
        #get words randomly
        while len(passphrase_list) < passphrase_length:
            roll = dice.dice_roll()
            word = wordlist[str(roll)]
            passphrase_list.append(word)

        #shuffle the words placement
        shuffle(passphrase_list)
        
        #form the passphrase string
        passphrase = ""
        for i in range(passphrase_length):
            passphrase += passphrase_list[i] + " "

        return passphrase
    
    #generate passphrase with preferences 
    #input: browser is selected and 
    #length of passphrase and
    #preferences of alphabets, numbers and symbols
    def generate_password(self, browsers_selected = [], passphrase_length = 4, preferences = []):
        self.init_folder()

        browsers_list = []

        for browser in browsers_selected:
            if browser == "Google Chrome": 
                chrome = Chrome()
                browsers_list.append(chrome)

            if browser == "Firefox": 
                firefox = Firefox()
                browsers_list.append(firefox)

            if browser == "Opera": 
                opera = Opera()
                browsers_list.append(opera)

            if browser == "Microsoft Edge": 
                edge = Edge()
                browsers_list.append(edge)

        #get all keywords generated from all browsers
        keywords = []
        for browser in browsers_list:
            browserKeyword = browser.generate_keywords()

            if browserKeyword is not None:
                keywords.extend(browserKeyword)
        
        #remove duplicate words in the keywords list
        keywords = list(dict.fromkeys(keywords))

        wordlist_gen = Wordlist_Generator()
        generated_wordlist = wordlist_gen.generate_wordlist(keywords)

        #from preferences list get alphabets
        alphabets = []
        for preference in preferences:
            if preference.isalpha():
                alphabets.append(preference)
                
        #preferences without alphabets(only symbols and numbers)
        sym_and_num = []
        sym_and_num = [item for item in preferences if item not in alphabets]

        #generate passphrase from given alphabets
        passphrase = self.generate_passphrase(generated_wordlist, passphrase_length, alphabets)

        #add in symbols and number preferences into passphrase
        for i in range(len(sym_and_num)):
            passphrase = passphrase.split(" ", 1)
            passphrase = str(passphrase[0]) + str(sym_and_num[i]) + str(passphrase[1])

        return passphrase

