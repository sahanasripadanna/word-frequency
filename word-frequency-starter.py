#set up a regular expression that can detect any punctuation
import re
punctuation_regex = re.compile('[\W]')

#open a story that's in this folder, read each line, and split each line into words
#that we add to our list of storyWords
storyFile = open('short-story.txt', 'r') #replace 'short-story.txt' with 'long-story.txt' if you want!
storyWords = []
for line in storyFile:
    lineWords = line.split(' ')     #separate out each word by breaking the line at each space " "
    for word in lineWords:
        cleanedWord = word.strip().lower()      #strip off leading and trailing whitespace, and lowercase it
        cleanedWord = punctuation_regex.sub('', cleanedWord)    #remove all the punctuation
                                                                #(literally, replace all punctuation with nothing)
        storyWords.append(cleanedWord)          #add this clean word to our list

#set up an empty dictionary to hold words and their frequencies
#keys in this dictionary are words
#the value that goes with each key is the number of times that word appears in the dictionary
#Example: a key might be 'cat', and frequency_table['cat'] might be 5 if the word 'cat'
#appears 5 times in the storyWords list
frequency_table = {}
