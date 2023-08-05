# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 13:23:48 2023
QUESTION: A2Q1
@author: Haryish Elangumaran
"""
import json #json format on the output is to be generated to promote 

def paragraph_stats(paragraph):
    # Counting vowels, consonants, digits, symbols, and words
    vowels = consonants = digits = symbols = words = 0
    for char in paragraph:
        if char.isalpha():
            if char in 'AEIOUaeiou':
                vowels += 1
            else:
                consonants += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            words += 1
        else:
            symbols += 1
    words += 1
    
    # Counting sentences
    sentences = paragraph.count('.') + paragraph.count('!') + paragraph.count('?')
    
    # Counting frequency of each distinct word
    freq_dict = {}
    for word in paragraph.lower().split():
        word = ''.join(char for char in word if char.isalpha())
        if word:
            freq_dict[word] = freq_dict.get(word, 0) + 1
    
    # Counting palindrome words
    palindrome = 0
    for word in freq_dict:
        if word == word[::-1]:
            palindrome += 1
    
    # Counting anagrams
    anagrams = 0
    words_list = [word for word in freq_dict if len(word) > 1]
    for i in range(len(words_list)):
        for j in range(i+1, len(words_list)):
            if sorted(words_list[i]) == sorted(words_list[j]):
                anagrams += 1
                
    return {'vowels': vowels, 'consonants': consonants, 'digits': digits, 'symbols': symbols, 'words': words,
            'sentences': sentences, 'frequency': freq_dict, 'palindrome': palindrome, 'anagrams': anagrams}

def print_paragraph_stats(dictionary, level=0):
    print("The below entites are the analysis of a given paragraph,")
    i=0
    for i, (key,value) in enumerate(dictionary.items()):
        print("{}.) {}: {}".format(i+1, key,value))

paragraph = "There is no strife, no prejudice, no national conflict in outer space as yet. Its hazards are hostile to us all. Its conquest deserves the best of all mankind, and its opportunity for peaceful cooperation many never come again. But why, some say, the moon? Why choose this as our goal? And they may well ask why climb the highest mountain? Why, 35 years ago, fly the Atlantic? Why does Rice play Texas? We choose to go to the moon. We choose to go to the moon in this decade and do the other things, not because they are easy, but because they are hard, because that goal will serve to organise and measure the best of our energies and skills, because that challenge is one that we are willing to accept, one we are unwilling to postpone, and one which we intend to win, and the others, too. -- John F Kennedy"

stats = paragraph_stats(paragraph)

print_paragraph_stats(stats)
#print(json.dumps(stats, indent=4)+"\n")
#print("Raw data:- \n {}".format(stats))