import json

# imported json file to load data for the dictionary

data = json.load(open("data.json"))


# loaded dictionary data

# function logic to search for data
def translate(word):
    # checks if the word exists
    if word in data:
        return data[word]
    else:
        print("The word does not exist")


# accepting input for word from user
word = input("Enter a word to search: ")
# passing it to the function
output = translate(word)
# giving output for searched word
print(output)
