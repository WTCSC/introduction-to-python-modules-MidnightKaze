"""
Import the text_utils module you created and calculate the average number of
words per line in a given text file. The text file that will be used to test
this is the text file called "sample.txt" (located in the same directory as
this exercise). The average number of words per line should be rounded down to
the nearest integer.

Print the average number (FLOORED) of words per line in the text file in the following
format:

"Average words per line: [average]"
"""
import text_utils

text = open('sample.txt', 'r') #opens the file in read mode

total = 0

lines = text.readlines()

#num_lines = len(text.readlines()) #uses the length of the list generate to get the number of lines

for line in lines:

    total += text_utils.count_words(line)

average = int(total / len(lines))

print (f"Average words per line: {average}")