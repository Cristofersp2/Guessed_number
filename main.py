import random

def guesser():
    print("Think a number between 1 and 100.")
    min_num = 1 
    max_num = 100
    tries = 5
    
    for i in range(tries):
        guessed_number = random.randint(min_num, max_num)
        print(f"try {i + 1}: ¿Is {guessed_number} your number?")
        
        answer = input("Answer 'y' if is correct, 'b' if is bigger, 's' if is smaller: " ).lower()
        
        if answer == 'y':
            print(f"You guessed the number on the try {i + 1}!")
            break
        elif answer == 'b':
            min_num = guessed_number + 1
        
        elif answer == 's':
            max_num = guessed_number - 1
        else:
            print("Answer is not valid. Please, answer with 's', 'b', or 's'.")

if __name__ == "__main__":
    guesser()