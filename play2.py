import time

# Function to print text slowly with a pause between each character
def slow_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Move to the next line after the text is printed

def start_game():
    slow_print("You wake up in front of a maze. What will you do? Go right (r), left (l), or straight (s)?")

def move_choice():
    choice = input("Enter 'r', 'l', or 's': ").lower()
    
    if choice == 'r':
        slow_print("Dead end! Go back.")
        move_choice()
    elif choice == 'l':
        slow_print("You find a key. Do you open the door (o) or return (r)?")
        key_room()
    elif choice == 's':
        slow_print("The path splits. Left (l) or right (r)?")
        straight_path()
    else:
        slow_print("Invalid choice! Try again.")
        move_choice()

def key_room():
    choice = input("Enter 'o' to open or 'r' to return: ").lower()
    if choice == 'o':
        slow_print("You escaped! You win!")
    elif choice == 'r':
        move_choice()
    else:
        slow_print("Invalid choice! Try again.")
        key_room()

def straight_path():
    choice = input("Enter 'l' for left or 'r' for right: ").lower()
    if choice == 'r':
        slow_print("Dead end! Go back.")
        move_choice()
    elif choice == 'l':
        slow_print("You escaped! You win!")
    else:
        slow_print("Invalid choice! Try again.")
        straight_path()

def main():
    start_game()
    move_choice()

main()
