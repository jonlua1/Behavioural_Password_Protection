import os
import configparser
# import filetype

#only works for Windows paths

#to check if path exists
#print(os.path.exists('...'))

#to check if dir exists
#print(os.path.isdir('...'))

#to check if file exists
# print(os.path.isfile('...'))

#to get file name without extension
# print(os.path.splitext('...'))   

# #to find out what type of file 
# try:
#     kind = filetype.guess(chrome_history)
#     if kind is None:
#         print('Cannot guess file type!')
#     else:
#         print('File extension: %s' % kind.extension)
#         print('File MIME type: %s' % kind.mime)
# except:
#     print("Chrome history file not found")


#to get Chrome History file path
#returns string of path of Chrome History file
#if file doesnt exist return None
def locate_chrome():
    chrome_path = os.path.join(os.getenv('LOCALAPPDATA'), r'Google\Chrome\User Data\Default')
    chrome_history = os.path.join(chrome_path, "History")
    if(os.path.isfile(chrome_history)):
            return chrome_history
    else: 
        return None


#to get Mozilla Firefox History file
#returns string of path of Chrome History file
#if file doesnt exist return None
def locate_firefox():
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
            return firefox_history
        else: 
            return None
    else:
        return None


#note: only can work for NEW microsoft edge (v79+)
#to get Microsoft Edge History file
#returns string of path of Edge History file
#if file doesnt exist return None
def locate_edge():
    edge_path = os.path.join(os.getenv('LOCALAPPDATA'), r'Microsoft\Edge\User Data\Default')
    edge_history = os.path.join(edge_path, "History")
    if(os.path.isfile(edge_history)):
        return edge_history
    else: 
        return None


#to get Opera History file
#returns string of path of Opera History file
#if file doesnt exist return None
def locate_opera():
    opera_path = os.path.join(os.getenv('APPDATA'), r'Opera Software\Opera Stable')
    opera_history = os.path.join(opera_path, "History")
    if(os.path.isfile(opera_history)):
        return opera_history
    else: 
        return None