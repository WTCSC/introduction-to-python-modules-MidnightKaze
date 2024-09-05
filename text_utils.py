def count_chars(text):
    
    return (len(text)) #returns the length of the string as the total number of characters


def count_words(text):
    
    sentence = text.split() #splits the sentence into a list

    num_words = len(sentence) #denotes that the number of words is the length of the list

    return(num_words) #returns the number of words from above


def count_sentences(text):
    
    num_sentence = 0 #starts a count

    for char in text: #check the characters in the input text
        if char in ".?!": #if a charcter is equal to . or ? or ! (aka the end of a sentence)
            num_sentence += 1 #add one to the count

    return(num_sentence) #returns the number of sentences from above