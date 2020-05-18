import re
from nltk.tokenize import word_tokenize
from backend.stopwords import remove_stopwords

#filter keywords list and 
#extract possible keywords from keywords list
#returns keywords list containing possible keywords
def clean_text(keywords):
    whitelist = set('abcdefghijklmnopqrstuvwxyz')

    #combine all strings in list into single string
    str1 = ""
    for ele in keywords:
        str1 += ele
    
    #change all chars to lowercase
    str1 = str1.lower()

    #removes all words containing numbers
    str1 = re.sub(r'\w*\d\w*', '', str1).strip()

    #remove stopwords from string
    str1 = remove_stopwords(str1)

    tokens = word_tokenize(str1)
    #remove all tokens that are not alphabetic
    words = [word for word in tokens if word.isalpha()]
    str1 = (" ").join(words)

    str2 = ""
    #removes everything except lowercase alphabets (to clear up words from other languages)
    for word in str1.split():
        word = ''.join(filter(whitelist.__contains__, word))
        str2 += word + ' '

    #remove words of length lesser than 4 and greater than 10
    str2 = re.sub(r'\b\w{1,3}\b', '', str2)
    str2 = re.sub(r'\b\w{10,}\b', '', str2)

    #removes excess whitespaces
    result = re.sub(r"\s+"," ",str2, flags = re.I)

    words = result.split()
    keywords = []
    for word in words:
        keywords.append(word)

    return keywords