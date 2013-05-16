# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Jenna Gopilan

#9.1
def read_text():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print word
        
        
#read_text()
        
   
#9.2
def has_no_e():
    fin = open('words.txt')
    count = 0
    e_word = 0
    for line in fin:
        word = line.strip()
        if 'e' in word:
            e_word += 1
            pass
        else:
            print word
            count += 1
    percentage = (float(count) / (e_word + count)) * 100 
    print percentage,"%"

#has_no_e()

#9.3

def has_letters(word, badletters):
    lettercount = 0
    for letter in badletters:
        if letter in word:
            lettercount += 1
        else:
            return 0
    return lettercount
     
def avoids():
    badletters = raw_input("Type the letters that are forbidden - don't include any space or commas.\n")
    fin = open('words.txt')
    count = 0
    
    for line in fin:
        word = line.strip()
        lettercount = 0
        check = has_letters(word,badletters)
        if check > 0:
            count += 1
        else:
            pass
    return count
    
#print avoids()

#9.4
def letterused(word, wordletters):
    lettercount = 0
    for i in word:
        if i in wordletters:
            lettercount += 1
        else:
            return 0
    return lettercount

def uses_only(string, wordletters):
    for letter in string:
        check = letterused(string, wordletters)
        if check >= len(wordletters):
            return True
        else:
            return False
        
        
print uses_only('apples', 'aple')
