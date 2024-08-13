"""In this Task, I will be using Python programming language to create a Hangman Game. 
The game prompts the user to enter an alphabetical character as a guess for the word randomly picked by the program. 
The program checks every entry by the user to determine the provided character
 is available in the word or not and inform the player respectively"""
import random


def getRndWord():
    words = ["apple", "banana", "cherry", "date", "eggplant", "fig", "grape", "honeydew", "jackfruit", "kiwi", "lemon", "mango", "nectarine", "olive", "peach", "pineapple", "plum", "quince", "raspberry", "strawberry", "tangerine", "watermelon", "yam", "zuc"]
    return random.choice(words)

def displayHangman(attempts):
    if(attempts == 0):
        print("  _______     ")
        print(" |/      |    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print()

    elif(attempts == 1):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print()

    elif(attempts == 2):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print()

    elif(attempts == 3):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/    ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print()
    
    elif(attempts== 4):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")
        print("_|___         ")
        print()

    elif(attempts == 5):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
        print(" |            ")
        print("_|___         ")
        print()

    elif(attempts == 6):
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print(" |            ")
        print("_|___         ")
        print()

def play_Hangman():
    word = getRndWord()
    wordLength = "_" * len(word)
    attempts = 0
    guessed = False
    guessedWords = []
    guessedLetters = []

    print("Welcome to Hangman Game!")
    print("-----------------------------------------------")
    print("You have 6 chances to guess the letters wrongly")
    print(displayHangman(attempts))
    print(wordLength)
    print("\n")

    while(attempts != 6 and guessed == False):
        ## Prompt the user to input a letter
        letter = input("Guess a letter: ")

        ## check whether the user entered one alphabetical character 
        if(len(letter) == 1 and letter.isalpha):

            # Check whether the user has already guessed the letter
            if(letter in guessedLetters):
                print("You have already guessed this letter", letter)
            
            ## Check whether the letter is in the word
            elif(letter not in word):
                print("Sorry, the letter", letter, "is not in the word")
                attempts += 1
                guessedLetters.append(letter)
            
            ## If the letter is in the word
            else:
                print("Congratulations, the letter", letter, "is in the word")
                guessedLetters.append(letter)
                wordlist = list(wordLength)
                indices = [i for i, char in enumerate(word) if char == letter]
                for index in indices:
                    wordlist[index] = letter
                wordLength = "".join(wordlist)
                if "_" not in wordLength:
                    guessed = True
        ## Check whether the input length matches the word and if it is alphabetical letters
        elif len(letter) == len(word) and letter.isalpha():
            if(letter in guessedWords):
                ## This is to tell the user that they already entered the letter they just re-entered
                print("You have already guessed this word", letter)
                attempts =+1
            elif(letter != word):
                print("Sorry, the word", letter, "is not in the word")
                attempts += 1
                guessedWords.append(letter)
            else:
                guessed = True
                wordLength = word


        ## Check whether the user input is more than one letter and if it matches the word
        else:
            print("Please enter a single letter or the whole word")
        print(displayHangman(attempts))
        print(wordLength)
        print("\n")


##Upon the last attempt and or the user has guessed the word correctly
    if(guessed == True):
        ##Congratulate the player 
        print("Congratulations, you guessed the word", word)

        ##Ask the player if they want to play again
        playAgain = input("Do you want to play again? (y/n)")
        if(playAgain == "y"):
            play_Hangman()
        else:
            print("Thank you for playing Hangman!")
    else:
        ##Tell the player that they lost and display what the word was instead
        print("Sorry, you ran out of chances. The word was", word)


        ##Ask the player if they want to play again
        playAgain = input("Do you want to play again? (y/n)") 
        if(playAgain == "y"):
            play_Hangman()
        else:
            print("Thank you for playing Hangman!")

play_Hangman()