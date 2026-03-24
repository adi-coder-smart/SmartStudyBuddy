import random
import os
import time

# --- HELPER FUNCTIONS ---

def clear_screen():
    """Console ko clear karne ke liye function."""
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_effect(message):
    """Loading effect text ke sath."""
    print(f"\n[WAIT] {message}...", end="", flush=True)
    time.sleep(1)
    print(" Done! [OK]\n")

# --- MODULE 1: SMART STUDY BUDDY ---

def study_python():
    questions = [
        {"q": "What is Python?", "a": "Python is a high-level, interpreted programming language."},
        {"q": "Difference between List and Tuple?", "a": "Lists are mutable (changeable), Tuples are immutable."},
        {"q": "What is a Loop?", "a": "Loops allow code to be executed repeatedly."}
    ]
    
    print("\n--- [ PYTHON FLASHCARDS ] ---")
    for i, item in enumerate(questions, 1):
        print(f"\n(Q{i}) {item['q']}")
        input("   >> Press Enter for Answer...")
        print(f"   [ANS]: {item['a']}")
    
    print("\n[NOTE] Code is like humor. When you have to explain it, it is bad.")
    input("\n>> Press Enter to return...")

def study_dbms():
    print("\n--- [ DBMS CONCEPTS ] ---")
    print("1. DBMS: Software to manage databases.")
    print("2. Normalization: Process to reduce redundancy.")
    print("3. Primary Key: Unique identifier for a record.")
    print("\n[NOTE] Data is the new oil!")
    input("\n>> Press Enter to return...")

def study_os():
    print("\n--- [ OS NOTES ] ---")
    print("1. OS: Interface between user and hardware.")
    print("2. Types: Batch, Time-sharing, Real-time.")
    print("3. Deadlock: Processes blocking each other.")
    print("\n[NOTE] Consistency is key!")
    input("\n>> Press Enter to return...")

def smart_study_buddy():
    while True:
        clear_screen()
        print("=================================")
        print("       SMART STUDY BUDDY         ")
        print("=================================")
        print("1. Python Study")
        print("2. DBMS Study")
        print("3. Operating System")
        print("4. Back to Main Menu")
        print("=================================")

        choice = input("Select Subject (1-4): ")

        if choice == "1":
            study_python()
        elif choice == "2":
            study_dbms()
        elif choice == "3":
            study_os()
        elif choice == "4":
            break
        else:
            input("Invalid choice! Press Enter to try again.")

# --- MODULE 2: MINI GAME HUB ---

def number_guessing_game():
    clear_screen()
    print("\n--- [ NUMBER GUESSING GAME ] ---")
    target = random.randint(1, 10)
    attempts = 3
    
    print(f"Guess a number between 1 and 10. You have {attempts} chances!")

    while attempts > 0:
        try:
            guess = int(input(f"\nYour Guess ({attempts} left): "))
            
            if guess == target:
                print(f"*** AMAZING! You guessed {target} correctly! ***")
                break
            elif guess < target:
                print("Go Higher! (+)")
            else:
                print("Go Lower! (-)")
            
            attempts -= 1
        except ValueError:
            print("Please enter a number only!")

    if attempts == 0:
        print(f"\n[GAME OVER] The number was {target}.")
    
    input("\n>> Press Enter to continue...")

def rock_paper_scissors():
    clear_screen()
    print("\n--- [ ROCK PAPER SCISSORS ] ---")
    options = ["rock", "paper", "scissors"]
    
    while True:
        computer = random.choice(options)
        user = input("\nChoose (rock/paper/scissors) or 'exit': ").lower()

        if user == 'exit':
            break
        
        if user not in options:
            print("Invalid choice! Check spelling.")
            continue

        loading_effect("Computer is thinking")
        print(f"Computer chose: {computer.upper()}")
        
        if user == computer:
            print("It's a Tie! (=)")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("*** YOU WIN! ***")
        else:
            print("Computer Wins! (x)")

def mini_game_hub():
    while True:
        clear_screen()
        print("=================================")
        print("        MINI GAME HUB            ")
        print("=================================")
        print("1. Number Guessing")
        print("2. Rock Paper Scissors")
        print("3. Back to Main Menu")
        print("=================================")

        choice = input("Select Game (1-3): ")

        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            break
        else:
            input("Invalid choice! Press Enter to try again.")

# --- MAIN APP ---

if __name__ == "__main__":
    while True:
        clear_screen()
        print("*********************************")
        print("    STUDENT ALL-IN-ONE APP       ")
        print("*********************************")
        print("1. Smart Study Buddy")
        print("2. Mini Game Hub")
        print("3. Exit App")
        print("*********************************")

        main_choice = input("Enter Choice (1-3): ")

        if main_choice == "1":
            loading_effect("Opening Study Mode")
            smart_study_buddy()
        elif main_choice == "2":
            loading_effect("Loading Games")
            mini_game_hub()
        elif main_choice == "3":
            print("\nThank you for using our App. Good luck!")
            break
        else:
            input("Invalid Input! Press Enter to try again.")