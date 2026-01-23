import random

def get_user_choice():
    
    print("  MATH MASTER GAME ")
    
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Mix Mode (?)")
    print("Q. Quit Game")
    return input("\nChoose a mode (1-5 or Q): ").lower()

def play_round(mode):
    
    if mode == '5':
        op = random.choice(['1', '2', '3', '4'])
    else:
        op = mode

 
    if op == '1':  
        n1 = random.randint(1, 20)
        n2 = random.randint(1, 20)
        symbol = "+"
        answer = n1 + n2

    elif op == '2':  
        n1 = random.randint(10, 30)
        n2 = random.randint(1, 10)
        if n2 > n1: n1, n2 = n2, n1  
        symbol = "-"
        answer = n1 - n2

    elif op == '3': 
        n1 = random.randint(1, 12)
        n2 = random.randint(1, 12)
        symbol = "×"
        answer = n1 * n2

    elif op == '4':
        n2 = random.randint(2, 10)
        answer = random.randint(2, 12) 
        n1 = n2 * answer               
        symbol = "÷"
    
    else:
        return 

    print(f"\nSolve:  {n1} {symbol} {n2} = ?")
    
    try:
        user_input = int(input("Your Answer: "))
        
        if user_input == answer:
            print("Correct! Awesome job!")
        else:
            print(f"Oops! The correct answer was {answer}")
            
    except ValueError:
        print("Please enter a valid number only.")

while True:
    choice = get_user_choice()
    
    if choice == 'q':
        print("\nThanks for playing! Goodbye.")
        break
        
    if choice in ['1', '2', '3', '4', '5']:
        play_round(choice)
        input("\nPress Enter to continue...")
    else:
        print("Invalid choice, please try again.")