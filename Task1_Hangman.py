import random

words = ["python", "computer", "programming", "developer", "keyboard"]

word = random.choice(words)
guessed_word = ["_"] * len(word)
wrong_guesses = 0
max_wrong_guesses = 6
guessed_letters = []

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

while wrong_guesses < max_wrong_guesses and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

if "_" not in guessed_word:
    print("\nCongratulations!")
    print("The word was:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)
