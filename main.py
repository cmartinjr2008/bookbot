def countLetters(splitBook):
    letterCount = {}

    #for x in range(len(splitBook)):
    for letter in splitBook:
        if letter in letterCount.keys():
            letterCount[letter] += 1
                    
        else:
            letterCount[letter] = 1
                              
    for letter in letterCount:
        print("The", letter, "character was found ", letterCount[letter], "times")
    

with open('books/frankenstein.txt') as f:
    bookFile = f.read()
    wordSplit = []
    lettersplit = []
    numberOfWords = 0
    wordSplit = bookFile.split()
    
    for words in wordSplit:
        if words.isalpha():
            for letter in words:
                lettersplit += letter.lower()
        
        numberOfWords += 1
    
    print("--Analyzing Uploaded Book--")
    print("There are a total of:", numberOfWords, "in this book")
    print("Here is the breakdown of letters: ")
    countLetters(lettersplit)
        
    
    
    
    




