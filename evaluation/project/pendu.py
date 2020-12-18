# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 11:16:06 2020

@author: loicr
"""
import random
words = open("words.txt","r")
lines = words.readlines()
words.close()

##Gernere alphabet
alphabet = []
index = 65
while index <= 90:
    alphabet.append(chr(index))
    index = index+1

## genère mot random
randWord = random.randint(0,len(lines))    
word = lines[randWord] 
print(word)


lives = 6
lenword = len(word)
play = True
findWord= []
i = 0
while i < lenword:
    findWord.append("_")
    i = i + 1

def showWord(findWord) :
    i= 0
    disWord = ""
    while i < len(findWord) - 1:
        disWord = disWord + findWord[i]+" "
        i = i+1
    return disWord

#retourne une liste des lettre troucver dans le mot
trouver = lambda mot, lettre: [i for i, car in enumerate(mot) if car==lettre]

print("Welcome to Hangman!")
text = "Guess your letter: "
while play :
    print(showWord(findWord))
    if "_" in showWord(findWord):
        letter = input(text)
        letter = letter.upper()
        if letter in alphabet:
            text = "Guess your letter: "
            if letter in word:
               posletter = trouver(word,letter)
               i = 0
               while i < len(posletter):
                   findWord[posletter[i]] = letter
                   i = i+ 1
            else:
                lives = lives - 1
                if lives == 0:
                    print("You are a looser the word was : "+ word)
                    play = False
                    break
                else :    
                    print("Incorrect! You have "+ str(lives)+" more guesses...")
                
        else:
            text = "Too long or not a letter, guess your letter: " 
    else :
        print("Well done you win !")
        play = False
        break