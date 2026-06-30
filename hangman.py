import random

# List of 5 predefined words
words = ["python", "apple", "school", "friend", "planet"]

# Select a random word
word = random.choice(words)

guessed = []
wrong_attempts = 0
max_attempts = 6

print("===== HANGMAN GAME =====")

while wrong_attempts < max_attempts:

    # Display the word
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if the word is guessed
    if "_" not in display:
        print("🎉 Congratulations! You guessed the word.")
        break

    # Take input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)

    # Check the guess
    if guess in word:
        print("Correct!")
    else:
        wrong_attempts += 1
        print("Wrong guess!")
        print("Attempts left:", max_attempts - wrong_attempts)

# If player loses
if wrong_attempts == max_attempts:
    print("\nGame Over!")
    print("The word was:", word)
