import os

#from a list of words, return a dictionary of word-frequency pairs
def keywords_to_freq_dict(keywords):
    wordfreq = {}
    for word in keywords:
        if(word in wordfreq):
            wordfreq[word] += 1
        else:
            wordfreq[word] = 1
    return wordfreq

#add keywords and freq list into the dict
def add_keywords_to_dict(keywords, dictionary):
    for word in keywords:
        word = word.replace('(', '').replace(')', '').replace("'", '')
        freq, keyword = word.split(', ')
        if keyword in dictionary:
            dictionary[keyword] += int(freq)
        else:
            dictionary[keyword] = int(freq)
    return dictionary

#sort a dict of word-freq pairs in order of descending freq
def sort_freq_dict(freqdict):
    sorted_dict = [(freqdict[key], key) for key in freqdict]
    sorted_dict.sort()
    sorted_dict.reverse()
    return sorted_dict

#initialise ezPsass folder if it does not exist
def init_folder():
    #ezPass folder path
    folder_path = os.path.expanduser('~\Documents\ezPass')
    
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
    else:
        print("FOLDER CREATED")

#generate passphrase 
#input: browser is selected and 
#length of passphrase and
#preferences of alphabets, numbers and symbols
def generate_password(browsers_selected = [], passphrase_length = 4, preferences = []):
    init_folder()
    



# generate_password()