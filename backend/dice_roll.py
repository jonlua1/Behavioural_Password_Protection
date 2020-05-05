import secrets

#generate dice roll numbers consisting of 5 numbers
def dice_roll():
    #Getting systemRandom class instance out of secrets module
    secretsGenerator = secrets.SystemRandom()

    dice_number = ""

    #random integer number uisng secrets
    for i in range(5):
        randomNumber = secretsGenerator.randint(1,6)
        dice_number += str(randomNumber)

    return int(dice_number)
