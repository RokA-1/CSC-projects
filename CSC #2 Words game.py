#importing random library to use it
import random

#defining the function which will choice the fruit
def choose_fruit():
    fruits = ['apple', 'banana', 'cherry', 'orange', 'grape', 'kiwi', 'melon', 'pear']
    return random.choice(fruits)

#defining the function which will dislay the word for the player
def the_displayed_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

#defining the main function which will check if the player is a winner or a loser
def main():
    #defining main variables
    word = choose_fruit()
    guessed_letters = []
    attempts = 6

    #print welcome msg
    print("Welcome to the Word Guessing Game!")
    print("Our game is about fruits! the game will choice a random fruit and you have to guess its letters.You have 6 attemps <GOOD LUCK!>")

    print(the_displayed_word(word, guessed_letters))
    
    #looping until the player wins or loses
    while attempts > 0:
        guess = input("Guess a letter: ")
        guess= guess.lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        if guess in word:
            print("Correct guess :)")
            guessed_letters.append(guess)
        else:
            attempts -= 1
            print(f"Incorrect :( You have {attempts} attempts left.")

        display = the_displayed_word(word, guessed_letters)
        print(display)
        
        if '_' not in display:
          print("Congratulations! You guessed the word.")
          break
            

    if "_" in display:
        print(f"Out of attempts! The word was: {word}")
            

if __name__ == "__main__":
    main()
