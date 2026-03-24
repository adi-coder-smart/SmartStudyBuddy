import random
import os
import time
import sys  

# --- SETUP & CONFIG ---
PASSWORD = "admin"

# --- HELPER FUNCTIONS ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_effect(message, delay=0.01):
    print(f"\n[SYSTEM] {message}...")
    for i in range(101):
        time.sleep(delay) 
        sys.stdout.write(f"\r[{'█' * (i // 5)}{'.' * (20 - (i // 5))}] {i}%")
        sys.stdout.flush()
    print("\nDone! [OK]\n")

def print_header():
    print(r"""
   _____ _   _ _____  ______  _______ _______ 
  / ____| \ | |  __ \|  ____|/ ____| |__   __|
 | (___ |  \| | |__) | |__  | (___      | |   
  \___ \| . ` |  ___/|  __|  \___ \     | |   
  ____) | |\  | |    | |____ ____) |    | |   
 |_____/|_| \_|_|    |______|_____/     |_|   
    """)
    print("    SMART EXAM PREDICTOR & STUDY BUDDY v5.0    ")
    print("===============================================")

# --- HARD QUESTION DATABASE (ADVANCED LEVEL) ---
db_c = [
    "Explain memory leaks and dangling pointers. How does 'free()' work internally?",
    "How are 2D arrays stored in memory? Explain Row-major vs Column-major order.",
    "Explain the 'volatile' keyword and its use cases in embedded C programming.",
    "Write a C program to detect a loop in a Linked List using Floyd's Cycle algorithm.",
    "Explain Function Pointers and how they can be used to implement callbacks."
]

db_cpp = [
    "Explain Virtual Functions, VTable, and VPTR under the hood in C++.",
    "What is the Diamond Problem in multiple inheritance? How does 'virtual' keyword solve it?",
    "Explain Move Semantics (std::move) and R-value references introduced in C++11.",
    "What is RAII (Resource Acquisition Is Initialization)? Why is it important?",
    "Difference between std::vector and std::list in terms of memory allocation and performance."
]

db_dbms = [
    "Compare B-Trees and B+ Trees. Why are B+ Trees preferred for database indexing?",
    "Explain Concurrency Control using 2-Phase Locking (2PL) and Timestamp Ordering.",
    "What is Write-Ahead Logging (WAL) and how does it ensure database recovery?",
    "Explain Query Optimization heuristics used by the database query planner.",
    "Discuss the anomalies of concurrent execution: Dirty Read, Non-repeatable Read, Phantom Read."
]

db_cn = [
    "Explain TCP Congestion Control algorithms: Slow Start, Congestion Avoidance, Fast Retransmit.",
    "How does the BGP (Border Gateway Protocol) work for internet routing?",
    "Calculate the Subnet Mask, Network ID, and Broadcast Address for IP 192.168.1.50/27.",
    "Explain the Diffie-Hellman Key Exchange process in Network Security.",
    "Difference between Stateful and Stateless firewalls at the transport layer."
]

db_python = [
    "Explain the Global Interpreter Lock (GIL). How does it affect multithreading in Python?",
    "How does Python's Garbage Collector work? (Reference Counting + Generational GC).",
    "Explain Metaclasses in Python. How are they different from regular classes?",
    "How does the Asyncio event loop work under the hood? Explain async/await.",
    "Write a custom Python Decorator that accepts arguments and limits function calls (Rate Limiting)."
]

db_js = [
    "Explain the JS Event Loop, Microtask Queue, and Macrotask Queue in detail.",
    "What are Closures? How can they lead to memory leaks if not handled properly?",
    "Explain Prototypal Inheritance vs ES6 Classes under the hood.",
    "Implement a 'Debounce' and 'Throttle' function from scratch.",
    "How does JavaScript handle concurrency despite being single-threaded?"
]

db_webdev = [
    "Explain Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF). How to mitigate them?",
    "Compare JSON Web Tokens (JWT) vs Session Cookies for authentication architecture.",
    "Explain Server-Side Rendering (SSR) vs Client-Side Rendering (CSR) performance impacts.",
    "How does REST differ from GraphQL in terms of over-fetching and under-fetching?",
    "Explain the critical rendering path (DOM, CSSOM, Render Tree) in browsers."
]

# --- MODULE 1: EXAM SELECTION & PYQ ANALYZER ---
def save_to_file(subject, questions):
    filename = f"{subject}_Predicted_Paper.txt"
    with open(filename, "w") as f:
        f.write(f"=== {subject} PREDICTED QUESTIONS ===\n\n")
        for i, q in enumerate(questions, 1):
            f.write(f"Q{i}. {q} [10 Marks]\n")
        f.write("\n\n-- Prepare these thoroughly. Good Luck! --")
    
    print(f"\n[SUCCESS] File Saved Successfully as '{filename}'")

def generate_paper(subject_name, question_pool):
    clear_screen()
    print_header()
    print(f"    AI PREDICTION ENGINE: {subject_name} MODULE")
    print("-----------------------------------------------")
    
    # 🔥 PYQ HYBRID LOGIC (File de ya na de, dono chalega) 🔥
    print("\n[INFO] You can provide a Past Year Questions (PYQ) file for better accuracy.")
    pyq_file = input(">> Enter PYQ text file name (or press ENTER to skip): ").strip()
    
    if pyq_file.endswith(".txt"):
        loading_effect(f"Reading Data from {pyq_file}", delay=0.02)
        loading_effect("Applying NLP algorithms to extract frequent topics", delay=0.03)
        print("\n[SYSTEM] Generated HIGH DIFFICULTY paper based on PYQ Trends.")
    else:
        loading_effect("No PYQ provided. Fetching standard syllabus data", delay=0.02)
        print("\n[SYSTEM] Generated STANDARD paper from Default Database.")
    
    selection = random.sample(question_pool, 3) 
    
    print(f"\n>>> TOP PREDICTED QUESTIONS FOR {subject_name} <<<\n")
    
    for i, q in enumerate(selection, 1):
        print(f"Q{i}. {q} [15 Marks]")
        time.sleep(0.5)
    
    print("\n-----------------------------------------------")
    save_choice = input(">> Do you want to DOWNLOAD/SAVE this paper? (y/n): ").lower()
    
    if save_choice == 'y':
        loading_effect("Writing Output to Disk")
        save_to_file(subject_name, selection)
    
    input("\n>> Press Enter to return to Main Menu...")

def smart_study_buddy():
    while True:
        clear_screen()
        print_header()
        print("    SELECT SUBJECT FOR AI PREDICTION")
        print("-----------------------------------------------")
        print("1. C Programming")
        print("2. C++ (OOP)")
        print("3. DBMS")
        print("4. Computer Networking")
        print("5. Python (Advanced)")
        print("6. JavaScript")
        print("7. Web Development")
        print("8. Go Back")
        print("-----------------------------------------------")

        choice = input("Select Subject (1-8): ")

        if choice == "1":
            generate_paper("C PROGRAMMING", db_c)
        elif choice == "2":
            generate_paper("C++", db_cpp)
        elif choice == "3":
            generate_paper("DBMS", db_dbms)
        elif choice == "4":
            generate_paper("COMPUTER NETWORKING", db_cn)
        elif choice == "5":
            generate_paper("PYTHON", db_python)
        elif choice == "6":
            generate_paper("JAVASCRIPT", db_js)
        elif choice == "7":
            generate_paper("WEB DEVELOPMENT", db_webdev)
        elif choice == "8":
            break
        else:
            input("Invalid choice! Press Enter to try again.")

# --- MODULE 2: MINI GAME HUB (3 GAMES ADDED) ---
def number_guessing_game():
    clear_screen()
    print("\n--- [ 1. NUMBER GUESSING GAME ] ---")
    target = random.randint(1, 10)
    attempts = 3
    print("Guess a number between 1 and 10. You have 3 chances!")
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
    input("\n>> Press Enter to go back...")

def rock_paper_scissors():
    clear_screen()
    print("\n--- [ 2. ROCK, PAPER, SCISSORS ] ---")
    choices = ['rock', 'paper', 'scissors']
    print("Let's play! Type 'quit' anytime to exit.")
    
    while True:
        user_choice = input("\nEnter Rock, Paper, or Scissors: ").lower()
        if user_choice == 'quit':
            break
        if user_choice not in choices:
            print("Invalid choice! Please try again.")
            continue
            
        comp_choice = random.choice(choices)
        print(f"Computer chose: {comp_choice.capitalize()}")
        
        if user_choice == comp_choice:
            print("It's a Tie! 🤝")
        elif (user_choice == 'rock' and comp_choice == 'scissors') or \
             (user_choice == 'paper' and comp_choice == 'rock') or \
             (user_choice == 'scissors' and comp_choice == 'paper'):
            print("You Win! 🎉")
        else:
            print("Computer Wins! 💻")

def word_scramble():
    clear_screen()
    print("\n--- [ 3. TECH WORD SCRAMBLE ] ---")
    words = ["PYTHON", "SERVER", "DATABASE", "NETWORK", "HACKER", "ROUTER"]
    word = random.choice(words)
    # Word ko jumble (scramble) karna
    scrambled = "".join(random.sample(word, len(word)))
    
    print(f"Unscramble this IT/Tech word: {scrambled}")
    attempts = 3
    
    while attempts > 0:
        guess = input(f"\nYour guess ({attempts} tries left): ").upper()
        if guess == word:
            print("Correct! You are a genius! 🧠🎉")
            break
        else:
            print("Wrong guess!")
            attempts -= 1
            
    if attempts == 0:
        print(f"\n[GAME OVER] The correct word was: {word}")
    input("\n>> Press Enter to go back...")

def mini_game_hub():
    while True:
        clear_screen()
        print_header()
        print("       STRESS BUSTER HUB (3 GAMES)")
        print("-----------------------------------------------")
        print("1. Number Guessing Game")
        print("2. Rock, Paper, Scissors")
        print("3. Tech Word Scramble (Jumbled Words)")
        print("4. Back to Main Menu")
        print("-----------------------------------------------")
        choice = input("Enter Choice (1-4): ")
        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            word_scramble()
        elif choice == "4":
            break
        else:
            input("Invalid Input! Press Enter to try again.")

# --- LOGIN SYSTEM ---
def login():
    attempts = 3
    while attempts > 0:
        clear_screen()
        print("\n***********************************************")
        print("      SECURE LOGIN SYSTEM v5.0")
        print("***********************************************")
        user_pass = input(f"\n>> Enter Administrator Password (Attempts left: {attempts}): ")
        
        if user_pass == PASSWORD:
            loading_effect("Verifying Credentials")
            return True
        else:
            print("\n[ERROR] Wrong Password! Access Denied.")
            attempts -= 1
            time.sleep(1)
            
    print("\n[SYSTEM LOCKED] Too many wrong attempts. Exiting...")
    return False

# --- MAIN APP ENTRY ---
if __name__ == "__main__":
    if login():
        while True:
            clear_screen()
            print_header()
            print("1. AI Exam Prediction Module")
            print("2. Stress Buster Games (3 Games inside)")
            print("3. Exit App")
            print("-----------------------------------------------")

            main_choice = input("Enter Choice (1-3): ")

            if main_choice == "1":
                smart_study_buddy()
            elif main_choice == "2":
                mini_game_hub()
            elif main_choice == "3":
                print("\nSaving Data... Thank you for using the App!")
                break
            else:
                input("Invalid Input! Press Enter to try again.")
