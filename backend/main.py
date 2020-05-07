from generator import generate_password
def main():
    #requires input from user

    #list to store user's selection of browser
    #eg chrome, firefox, opera, edge
    # browsers_selected = ['chrome', 'firefox', 'opera', 'edge']
    browsers_selected = ['chrome', 'opera', 'edge', 'firefox']

    #length of browser
    #e.g length is 4
    passphrase_length = 4

    #preferences of alphabets, numbers and symbols
    #eg a, &, 1
    preferences = ['x', 'y', 'z', 'w', '1', '2','#','%']

    #when user clicks generate password button
    #requires which browser is selected and 
    #length of passphrase and
    #preferences of alphabets, numbers and symbols
    generate_password(browsers_selected, passphrase_length, preferences)

main()