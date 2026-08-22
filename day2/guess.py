import random

print("Let's play a number guessing game")
print("If you guess upto 5 numbers correctly, you win.")
ready_prompt = input("Are you ready? (y/n): ").strip().lower()

score = 0
answer = random.randint(1,20)
total_guesses = []
correct_answers = []

while True:
    if ready_prompt == '':
        print("You did not answer the question. Enter Y for yes and N for no")
        ready_prompt = input("Are you ready? (y/n): ").strip().lower()
    elif 'n' in ready_prompt:
        print("Player has quit the game. If you want to play again, please restart the game.")
        break
    elif 'y' in ready_prompt:
        guess = input("Horray! Now guess a number between 1 to 20: ")
        while True:
            if guess == '' or guess.isdigit() is False:
                guess = input("You did not input any numbers. Please input a number between 1 to 20: ")
            elif int(guess) < 1 or int(guess) > 20:
                guess = input("That number is out of reach. Please input a number between 1 to 20: ")
            else:
                break
        if int(guess) >=1 and int(guess) <=20:
            while True:
                guess = int(guess)
                if guess > answer:
                    print('Too High. Try again!')
                    total_guesses.append(guess)
                    guess = input("Enter a number between 1 to 20: ")
                    continue
                elif guess < answer:
                    print('Too low. Try again!')
                    total_guesses.append(guess)
                    guess = input("Enter a number between 1 to 20: ")
                    continue
                elif guess == answer:
                    print("Correct!")
                    score += 1
                    correct_answers.append(guess)
                    total_guesses.append(guess)
                    print(f"Score: {score}/5")
                    if score < 5:
                        print(str(5 - score) + " more to win!")
                        answer = random.randint(1,20)
                        guess = input("Enter a number between 1 to 20: ")
                        continue
                    else:
                        print("You win!")
                        print(f'Total guesses: {total_guesses}')
                        print(f'Correct guesses: {correct_answers}')
                        break        
        break
    else:
        print("You did not answer the question. Enter Y for yes and N for no")
        ready_prompt = input("Are you ready? (y/n): ").strip().lower()
        