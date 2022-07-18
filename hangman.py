import random 
import time

print('\nWelcome to Hangman game by MKM\n')
name = input('Enter your name: ')
print("Hello " + name + "! Welcome to Hangman")
time.sleep(2)
print("Here we go!\n Let the game begin!")
time.sleep(3)

def main():
	global count
	global display
	global word
	global already_guessed
	global length
	global play_game
	words_to_guess =
["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_'* length
    already_guessed = []
    play_game = ""


def play_loop():
    global play_game
    play_game = input("Wannna play again? \ny = yes, n = no")
    if play_game == "y":
    	main()
    elif play_game == "n":
    	print("Great! Thanks for playing Hangman!\n")
    	exit()

def hangman():
	global count
	global display
	global word
	global already_guessed
	global play_game
	limit = 5
	guess = input("This is the Hangman word: " + display + "Enter your guess:\n")
	guess = guess.strip()
	if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
		hangman()

	elif guess in word:
		already_guessed.extend([guess])
		index = word.find(guess)
		word = word[:index] + guess + display[index + 1:]
		print(display + "\n")

	elif guess in already_guessed:
		print("Try some other letter.\n")

	else:
		count += 1
		if count == 1:
			time.sleep(1)
			print("  ____ \n"
				  " |     \n"
				  " |     \n"
				  " |     \n"
				  " |     \n"
				  " |     \n"
				  " |     \n"
				  "__|__\n")
			print("Wrong guess." + str(limit - count) + "guesses remaining\n")
		
		elif count == 2:
			time.sleep(1)
			print("  ____ \n"
				  " |     |\n"
				  " |     |\n"
				  " |     \n"
				  " |     \n"
				  " |     \n"
				  " |     \n"
				  "__|__\n")
			print("Wrong guess. " + str(limit-count) + "guesses remaining\n")
		
		elif count == 3:
			time.sleep(1)
			print("  ____ \n"
			 	  " |    |\n"
			      " |    |\n"
			      " |    |\n"
			      " |     \n"
			      " |     \n"
			      " |     \n"
			      "__|__\n")
		    print("Wrong guess. " + str(limit - count) + "last guess remaining\n")

		elif count == 4:
			time.sleep(1)
			print("  ____ \n"
			      " |    |\n"
			      " |    |\n"
		          " |    |\n"
			      " |    o\n"
			      " |     \n"
			      " |     \n"
			      "__|__\n")
		    print("Wrong guess. " + str(limit - count) + "last guess remaining\n")
		    
		    elif count == 5:
		    time.sleep(1)
		    print("  _____ \n"
		    	  " |     |\n"
		    	  " |     |\n"
		    	  " |     |\n"
		    	  " |     o\n"
		    	  " |    /|\n"
		    	  " |    /|\n"
		    	  "__|__\n")
		    print("Wrong guess. You are hanged!!!\n")
		    print("The word was:", already_guessed, word)
		    play_loop()
		if word == '_' * length:
		    print("Congrats! You have guessed the word correctly!")
		    play_loop()

		elif count != limit:
		    hangman()

main()

hangman()	  

   