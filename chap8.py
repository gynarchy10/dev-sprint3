# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Jenna Gopilan


def rotate_char(char,shift):
    number = ord(char.upper()) - 65
    newNumber = (number + shift) % 26
    newChar = chr(newNumber + 65)
    return newChar

def rotate_word(string,shift):
    word = ""
    index = 0
    while index < len(string):
        letter = string[index]
        word += rotate_char(letter,shift)
        index += 1
    return word
    

    
print rotate_word("xyzabc", 1)
print rotate_char("a",111)
