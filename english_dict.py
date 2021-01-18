import json #library that will help python to understand json file
from difflib import get_close_matches #library for getting close match
data = json.load(open("data.json"))#for loading the meaning
def Dictionary(w):
    w = w.lower() #keys are in lower case
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0: #check if there are multiple similar word
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])#this gives the first item.
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = Dictionary(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
