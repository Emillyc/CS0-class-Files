def hangmanGame():
    import random 
    artList =  ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']
    lettersGuessed = []
    strikes = []
    hint = []
    def loadWord():
        
        ''' Populate each list with at least 10 different items.  Create a variable called secretWord that is assigned a random word from one of the lists. 
        
        return a tuple in the following format:  (secretWord, list the secretWord is from)   
        
        Hint:  You will need to randomly choose one of the lists, and THEN choose a random word from that list.
        '''
        persons = ['bob', 'joe', 'emilly', 'kayla', 'max', 'matt', 'josh', 'nicole', 'andy', 'nick']
        places = ['ocala', 'trinity', 'mall', 'home', 'store', 'pharmacy','field', 'restuarant', 'computer lab', 'church']
        things = ['phone', 'computer', 'cup', 'rope', 'food', 'jacket', 'ipad', 'book', 'headphones', 'board']
        list1 = [persons, places, things]
    
        secretWord = random.choice(random.choice(list1))
        if secretWord in persons:
            print "It's a person"
            
        elif secretWord in places:
            print "It's a place"
            
        else:
            print "It's a thing"
            
        return secretWord
    
    def isWordGuessed(secretWord, lettersGuessed):
        '''
        secretWord: string, the word the user is guessing
        lettersGuessed: list, what letters have been guessed so far
        returns: boolean, True if all the letters of secretWord are in lettersGuessed;
        False otherwise
        '''
        
        
    
    
    
    def getGuessedWord(secretWord, lettersGuessed):
        
        printedWord = ''
        for letter in secretWord:
            if letter in lettersGuessed:
                printedWord += letter + ' '
            else:
                printedWord += '_'
        return printedWord
        
    
    def isWin():
        count = len(secretWord)
        for letter in lettersGuessed:
            if letter in secretWord:
                count2 = secretWord.count(letter) 
                count -= count2
            if count == 0:
                return True 
    def isLose():
        if strikes.count('STRIKE!') == 6:
            return True
    def getArt(artList):
        count = strikes.count('STRIKE!')
        print artList[count]
    def getAvailableLetters(lettersGuessed):
        '''
        lettersGuessed: list, what letters have been guessed so far
        returns: string, comprised of letters that represents what letters have not
        yet been guessed.
        '''
        if len(lettersGuessed) > 0:
            print ("You've guessed %s") %lettersGuessed
        guess = raw_input('What letter would you like to guess? ').lower()
        if guess in lettersGuessed:
            print "You've already guessed that!"
            getAvailableLetters(lettersGuessed)
        elif len(guess) != 1:
            print "Only one character"
            getAvailableLetters(lettersGuessed)
        elif guess.isalpha() == False:
            print "Only letters in Alphabet"
            getAvailableLetters(lettersGuessed)
        else:
            if guess in lettersGuessed:
                print "You've guessed that, please guess again!"
            elif guess in secretWord:
                print "Correct"
                lettersGuessed.append(guess)
            elif guess not in secretWord:
                print "Incorrect choice"
                strikes.append('STRIKE!')
                lettersGuessed.append(guess)
                
        
        
    
    def hangman(secretWord):
        print getGuessedWord(secretWord, lettersGuessed)
        getArt(artList)
        getAvailableLetters(lettersGuessed)
        if isLose() == True:
            print 'You Lose!' 
            hangmanGame()
        if isWin() == True:
            print 'You Win!'
            hangmanGame() 
        hangman(secretWord) 
            
        
    
    
    
    
    secretWord = loadWord()
    
    
    hangman(secretWord)
hangmanGame()