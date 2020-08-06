code = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

def encode(message:str):
    for vowel, number in code.items():
        message = message.replace(vowel, str(number))
    return message

def decode(message:str):
    for vowel, number in code.items():
        message = message.replace(str(number), vowel)
    return message

#Method encode and decode following requirements of replacing vowels by numbers indicated in the dictionary
#Two tests methods verify the functions work as expected
#Install pytest -> pip3 install pytest 
#run tests by running 'pytest' in root directory or message.py and test_message.py
#Assumptions made are input message parameter is a string and encoding dictionary is hard-coded