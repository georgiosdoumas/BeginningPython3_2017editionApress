#!/usr/bin/python3
from string import punctuation

def clearText(rawtext):
    cleared_text = rawtext.replace(' ', '').lower()
    #for mark in [',','!','?','.',"'"]:    # or I can import the string module and use
    for mark in punctuation:
        cleared_text = cleared_text.replace(mark, '')
    return cleared_text

def is_palindrome(rawtext):
    text = clearText(rawtext)
    #print("   Checking ", text)
    n = len(text)
    for i in range(len(text) // 2):
        if text[i] != text[n-i-1]:
            return False
    return True

if __name__ == '__main__':
    while True:
        input_text = input("Enter your word/phrase, to see if it is palindrome (type q when you want to stop):\n")
        if input_text == 'q':
            break
        elif is_palindrome(input_text):
            print("It is! You can read it backwards")
        else:
            print("Sorry, it is not a palindrome")
        
