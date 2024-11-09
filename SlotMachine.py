import random
import os
import time

#When you write a variable in all caps it becomes a global constant variable 
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "🦞" : 3,
    "🍒" : 5,
    "🔔" : 6,
    "🍋" : 9
    }

symbol_value = {
    "🦞" : 5,
    "🍒" : 4,
    "🔔" : 3,
    "🍋" : 2
    }

#Checks the list to see if you have 3 of the same symbols in a row
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines

            

def get_slots_machine_spin(rows, cols, symbols):
    #puts all the symbols in a symbol list to be used to create the slot machine
    all_symbols = []
    for symbols, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbols)

    #creates the slot machine which is printed in the list columns
    columns = []
    for _ in range(cols):
        colum = []
        for _ in range(rows):
            symbol = random.choice(all_symbols)
            colum.append(symbol)
            all_symbols.remove(symbol)
        columns.append(colum)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")   
        print()

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter thr number of lines to bet on (1 - {MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:    
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Insufficient balance for bet. Balance: ${balance}")
        else: 
            break    
    print(f"\nYou are betting ${bet} on {lines} line(s). \nTotal bet is equal to ${total_bet}\n")

    slots = get_slots_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    if winnings == 0 :
       print("\nNo winnings") 
    else:
        print(f"\nYou won ${winnings}.\nYou won on lines:", *winnings_lines) 
    time.sleep(5)
    return winnings - total_bet

def main(balance):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
        while True:
            if balance != 0:
                break

            add_bal = input("Would you like to deposit more? y/n: ").lower()
            if add_bal not in ("y", "n"):
                print("Invalid, type either y/n.")
            elif add_bal != "y":
                break 
            else:
                balance += deposit()    

        if balance == 0:
            break
    print(f"You left with ${balance}")    



if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    balance = deposit()
    main(balance)    