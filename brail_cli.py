#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys

# Define Braille patterns
braille_dict = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..',
    'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 
    'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 
    'y': 'OO.OOO', 'z': 'O..OOO', 'cap': '.....O', ' ': '......', 'num': '.O.OOO', 
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', 
    '9': '.OO...', '0': '.OOO..'
}

# Reverse the Braille dictionary for easy look-up in Braille-to-English translation
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

# Function to translate English to Braille
def english_to_braille(text):
    braille_output = []
    number_mode = False

    for char in text:
        if char.isupper():
            braille_output.append(braille_dict['cap'])
            char = char.lower()
        if char.isdigit():
            if not number_mode:
                braille_output.append(braille_dict['num'])
                number_mode = True
            braille_output.append(braille_dict[char])
        elif char.isalpha():
            number_mode = False
            braille_output.append(braille_dict[char])
        elif char == ' ':
            number_mode = False
            braille_output.append(braille_dict[' '])

    return ''.join(braille_output)

# Function to translate Braille to English
def braille_to_english(braille_input):
    english_output = []
    i = 0
    length = len(braille_input)
    number_mode = False
    cap_mode = False

    while i < length:
        char = braille_input[i:i+6]
        if char == braille_dict['cap']:
            cap_mode = True
        elif char == braille_dict['num']:
            number_mode = True
        else:
            if number_mode:
                english_output.append(reverse_braille_dict[char])
                number_mode = False
            elif cap_mode:
                english_output.append(reverse_braille_dict[char].upper())
                cap_mode = False
            else:
                english_output.append(reverse_braille_dict[char])
        i += 6

    return ''.join(english_output)

# Determine whether input is Braille or English based on characters
def detect_input_type(input_str):
    if all(c in 'O.' for c in input_str):  # If input contains only O and .
        return 'braille'
    else:
        return 'english'

# Main translation function
def translate(input_str):
    input_type = detect_input_type(input_str)
    if input_type == 'english':
        return english_to_braille(input_str)
    else:
        return braille_to_english(input_str)

# Command-line execution
if __name__ == "__main__":
    input_str = sys.argv[1]
    result = translate(input_str)
    print(result)


# In[ ]:




