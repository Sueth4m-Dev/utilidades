import os, sqlite3, time, json, random

COLORS = {
    'reset': '\033[0m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m'
}

# --- DATABASE TOOLS ---
def execute_sql(db_name, command, params=()):
    """
    Executes a SQL command (INSERT, UPDATE, DELETE) and commits
    """
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(command, params)
        conn.commit()

def query_sql(db_name, command, params=()):
    """
    Performs a SELECT and returns the data
    """
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(command, params)
        return cursor.fetchall()
    
# --- JSON TOOLS ---

def save_data(data_to_save, filename='save.json'):
    """
    Saves data to a JSON file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data_to_save, file, indent=4, ensure_ascii=False)

def load_data(filename='save.json'):
    """
    Loads data from a JSON file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
# --- Utilities ---

def erase_screen():
    """
    Clears the terminal screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, speed=0.04):
    """
    Prints text with a certain delay (Speed)
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()

def ERROR(text):
    """
    Prints an error message in red
    """
    erase_screen()
    print(color(text, 'red'))

def print_menu(options_list):
    """
    Prints an enumerated list to the terminal
    """
    for index, item in enumerate(options_list, 1):
        print(f"{index}. {item}")

def read_int(prompt, min_val=None, max_val=None):
    while True:
        print(prompt)
        val = input()
        try:
            res = int(val)
            if (min_val is not None and res < min_val) or (max_val is not None and res > max_val):
                raise ValueError
            return res
        except ValueError:
            erase_screen()
            msg = "Erro! Digite um número válido"
            if min_val is not None and max_val is not None:
                msg += f" entre {min_val} e {max_val}"
            print(color(msg, 'red'))
    
def read_float(prompt, min_val=None, max_val=None):
    while True:
        print(prompt)
        val = input()
        try:
            res = float(val)
            if (min_val is not None and res < min_val) or (max_val is not None and res > max_val):
                raise ValueError
            return res
        except ValueError:
            erase_screen()
            msg = "Erro! Digite um número válido"
            if min_val is not None and max_val is not None:
                msg += f" entre {min_val} e {max_val}"
            print(color(msg, 'red'))
    
def continue_prompt():
    """
    Prints "Press ENTER to continue" in the terminal
    """
    input("\nPress ENTER to continue")

def roll_dice(sides, amount=1, bonus=0):
    """
    Simulates a dice roll
    Ex: roll_dice(20, 1, 5) --> Rolls 1 20-sided die and adds 5 to the total 
    """
    total = bonus
    for _ in range(amount):
        total += random.randint(1, sides)
    return total

def chance(percentage):
    """
    Returns True or False based on a percentage chance
    """
    num = roll_dice(100)
    return num <= percentage

def color(text, color_name):
    """
    Returns colored text
    Colors: 'reset', 'red', 'green', 'yellow', 'blue'
    """
    return f"{COLORS.get(color_name, '')}{text}{COLORS['reset']}"

def pick_random(items_list):
    """
    Receives a list and returns a randomly selected item
    """
    if not items_list:
        return None
    return random.choice(items_list)

def draw_header(text, symbol="=", width=50):
    """
    Creates a centered header.
    """
    print(symbol * width)
    print(text.center(width))
    print(symbol * width)

def draw_line(symbol="=", width=50):
    """
    Draws a simple line.
    """
    print(symbol * width)

def clean_text(text):
    """
    Removes useless spaces and standardizes for searching
    """
    return text.strip().capitalize()

def read_name(prompt, isalpha=True, min_char=3, max_char=15):
    """
    Ensures the name is valid according to length and type
    """
    while True:
        name = input(prompt).strip().capitalize()
        if min_char <= len(name) <= max_char:
            if isalpha and name.isalpha():
                return name
            elif not isalpha:
                return name
            
            erase_screen()
            print(color('Please use only letters for the name.', 'red'))
        else:
            erase_screen()
            print(color(f'Name must be between {min_char} and {max_char} characters.', 'red'))

def progress_bar(current, maximum, width=20, title="Progress", color_name='green'):
    """
    Generates a visual progress bar.
    """
    if maximum <= 0: maximum = 1
    current = max(0, min(current, maximum))

    percentage = current / maximum
    filled = int(width * percentage)
    empty = width - filled

    bar = "█" * filled + "-" * empty
    percent_str = f"{int(percentage * 100)}%"

    colored_bar = f"{COLORS.get(color_name, '')}{bar}{COLORS['reset']}"
    
    print(f"\r{title}: |{colored_bar}| {percent_str} ({current}/{maximum})", end="", flush=True)
    if current == maximum:
        print() 

def yes_no(question):
    """
    Asks the user a question and only accepts 'Y' or 'N'.
    Returns True for Yes and False for No.
    """
    while True:
        resp = input(f"{question} (Y/N): ").strip().lower()
        if resp in ['y', 'n', 'yes', 'no']:
            return resp in ['y', 'yes']
        erase_screen()
        print(color("Invalid response! Please type Y or N.", "red"))

def select_item(items_list, prompt="Choose an option: "):
    """
    Displays an enumerated list and returns the object chosen by the user.
    """
    if not items_list: return None
    
    print_menu(items_list)
    while True:
        choice = read_int(prompt)
        if 1 <= choice <= len(items_list):
            return items_list[choice - 1]
        print(color(f"Error! Choose a number between 1 and {len(items_list)}.", "red"))

def log_event(message, filename="activity.log"):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")