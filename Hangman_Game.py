import random
import word_file, hint_file  # type: ignore

def play_hangman():
    index = random.randint(0, len(word_file.words) - 1)
    word_to_guess = word_file.words[index]
    hint = hint_file.hints[index]

    guessed_letters = []
    guessed_word = ["_"] * len(word_to_guess)
    attempts_left = 6


# Rules and Introduction of the game...
    print("\n🎮 Welcome to HANGMAN GAME!")
    print(f"""
📜 Rules:
- Guess one letter at a time.
- You have 6 incorrect guesses.
- The word has {len(word_to_guess)} letters.
(●'◡'●) Hint: {hint}
- Let's begin!
""")

# The Hangman Game Biginnes...
    while attempts_left > 0 and "_" in guessed_word:
        print("Word:", " ".join(guessed_word))
        print("Guessed letters:", " ".join(guessed_letters))
        print("Lives left:", attempts_left)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_word[i] = guess
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts_left -= 1
            print(f"Sorry, '{guess}' is not in the word. You lose a life.")

        print()

# Aftre the write Answer and Wrong Answer...
    if "_" not in guessed_word and attempts_left > 0:
        print(" YOU WIN THE GAME..")
        print("🎉Congratulations!")
        print("You guessed the word:", word_to_guess)
    else:
        print("BETTER LUCK NEXT TIME!")
        print("The word was:", word_to_guess)
    print("Thanks for playing this round!\n")


# For asking the user to play again...
def main():
    while True:
        play_hangman()
        while True:
            replay = input("Do you want to play again? (yes/no): ").strip().lower()
            if replay in ['yes', 'y']:
                break  # play again, break inner loop
            elif replay in ['no', 'n']:
                print("Thanks for playing! Goodbye.")
                return  # exit the main loop and program
            else:
                print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
    
# //////////////////////////////END OF THE GAME/////////////////////////////////////



