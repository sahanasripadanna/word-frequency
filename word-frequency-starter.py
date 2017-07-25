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

ignoreWords = ['i', 'a', 'an', 'the', 'this', 'that', 'my', 'me', 'of', 'to',
'and', 'it']
# All code goes here
for word in storyWords:
    #if i haven't seen any words of this type before, add a new entry
    if word not in frequency_table:
        frequency_table[word] = 1
    #if i HAVE seen it before, add 1 to its current count
    else:
        frequency_table[word] = 1 + frequency_table[word]



#this is a function that defines the most frequent word
def find_max_frequency():
    #at the start i haven't seen any words
    #but i want to keep track of the most frequent word i've seen so far
    max_freq = 0
    max_word = ' '
    #look through ALL words in the frequency table
    for word in frequency_table:
        #i can check if it's an ignore word
        # if it is then i want to moooove on girlfriend
        if word in ignoreWords:
            pass
        #if its not an ignore word please consider it
        else:
        #if the words im looking at now has appeared more than any
        #words i've seen so far, update my max
            if frequency_table[word] > max_freq:
                max_freq = frequency_table[word]
                max_word = word
    #at the end of the for loop, we've looked through all the entries
    #and max_word has the most frequent word in it
    return max_word

best_word = find_max_frequency()
print("The most frequent non ignore word is: " + best_word)


# make a function to find the top ten
def give_me_the_top(number):
    #take the most frequent word out of the frequency table 10 times
    for count in range(number):
        top_word = find_max_frequency()
        print(top_word + " appears " + str(frequency_table[top_word]) + " times!")
        del(frequency_table[top_word]) #take that entry out of the table

give_me_the_top(10)
