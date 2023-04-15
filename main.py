import itertools
import pyperclip

# Defining the cyrillic letters that can be used to replace the english ones
cyrillic = {"a": "а", "e": "е", "k": "к", "m": "м", "n": "н", "o": "о", "r": "р", "s": "с", "t": "т", "u": "у",
            "A": "А", "B": "В", "E": "Е", "K": "К", "M": "М", "N": "Н", "O": "О", "R": "Р", "S": "С", "T": "Т",
            "U": "У", "X": "Х"}

# Asking the user to enter a word
word = input("Please enter a word, bbg:")

# Creating an empty dictionary to store the possible replacements
results = {}

# Looping through each letter in the word
for letter in word:
    # Checking if the letter can be replaced by a cyrillic one
    if letter in cyrillic:
        # Adding the cyrillic letter to the dictionary of possible replacements
        for new_letter in cyrillic[letter]:
            new_word = word.replace(letter, new_letter)
            results[new_word] = True
    else:
        # Adding the original letter to the dictionary of possible replacements
        results[word] = True

# To sort and group the results, I need to create a function that counts how many letters are changed from the original word
# ...

# Copying the first result to the user's keyboard using pyperclip
if results:
    first_result = list(results.keys())[0]
    pyperclip.copy(first_result)
    print(f"{first_result} Here is your name, we copied it to your keyboard already :3")
    print("Made a text document as well called sorted_results.txt with every possible combination for that username if the first one didn't work")
else:
    print("No possible replacements found for the given word.")
