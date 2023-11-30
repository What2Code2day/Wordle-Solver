# grabs the words from the word list
def load_dict(file_name):
    with open(file_name) as f:
        words = f.readlines()
    return [word.strip() for word in words]

global words
words = load_dict("Wordle-Solver/words.txt")

# filters for grey letters
def gray_filter(guess_letter):
    global words
    words = [word for word in words if guess_letter.strip().lower() not in word]
    print(', '.join(words))
    print('-------------------------------------------------------------------------')

# filters for green letters
def green_filter(guess_letter):
    global words
    letter_pos = int(input('what position: '))
    words = [word for word in words if word[letter_pos-1] == guess_letter.strip().lower()]
    print(', '.join(words))
    print('-------------------------------------------------------------------------')

# filters for yellow letters
def yellow_filter(guess_letter):
    global words
    letter_pos = int(input('what position: '))
    words = [word for word in words if word[letter_pos-1] != guess_letter.strip().lower()]
    print(', '.join(words))
    print('-------------------------------------------------------------------------')

def check_done():
    global words
    if len(words) <= 1:
        exit()

while True:

    # checks if the user is done
    check_done()

    # asks the user for there guess
    guess_letter = input('Input your letter: ')

    # asks the user for the color of the letter
    guess_color = input('What is the color (Y,G,B): ')

    # filters for grey letters
    if guess_color.lower() == "b":
        gray_filter(guess_letter)
    
    # filters for green letters
    if guess_color.lower()=="g":
        green_filter(guess_letter)

    # filters for yellow letters
    if guess_color.lower()=="y":
        yellow_filter(guess_letter)
    
    # Separates the while loops
    print('-------------------------------------------------------------------------')