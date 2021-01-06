import json
from difflib import get_close_matches

# imported json file to load data for the dictionary

data = json.load(open("data.json"))


# loaded dictionary data

# function logic to search for data
def translate(word):
    # checks if the word exists
    word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    # checking for close words
    elif len(get_close_matches(word, data.keys())) > 0:
        correct_word = get_close_matches(word, data.keys())[0]
        print("Is this the correct word {}: ".format(correct_word))
        next_step = input("Press \"Y\" to continue or \"N\" to stop ")
        if next_step == "Y":
            return data[correct_word]
        elif next_step == "N":
            print("This word does not exist")
        else:
            print("Press \"Y\" to continue or \"N\" to stop ")


    else:
        print("This word does not exist")


# accepting input for word from user
word = input("Enter a word to search: ")
# passing it to the function
output = translate(word)
# giving output for searched word

# Checking if word has multiple meanings
if type(output) == list:
    # printing out each meaning in a new line
    for item in output:
        print(item)
else:
    print(output)
