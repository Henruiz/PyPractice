import json
from difflib import get_close_matches


# Contains definitions
data = json.load(open("data.json"))


def translate(word):
    # making them all lower case
    word = word.lower()

    # Best case word matches
    if word in data:
        return data[word]
    # If user enters texas instead of Texas
    elif word.title() in data:
        return data[word.title()]
    # In case user enters acronyms such as USA or NATO
    elif word.upper() in data:
        return data
    # In case they typed in a weird word by mistake and the return value is not empty
    elif len(get_close_matches(word, data.keys())) > 0:
        user_input = input("Did you mean %s instead? \n Enter Y if yes or N if no: " % get_close_matches(word, data.keys())[0])
        # User choice if they meant a different word or not 
        if user_input == "Y" :
            return data[get_close_matches(word, data.keys)[0]]
        elif user_input == "N":
            return "The word does not exist. Please try again! "
        else:
            return "Please enter an English Dictionary Word!"

    else:
        return "The word does not exists. Please try again!"


word = input("Enter a word: ")
output = translate(word)
# If there is a list that gets returned
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)