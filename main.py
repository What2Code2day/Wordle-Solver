# grabs the words from the word list
def load_dict(file_name):
    file = open(file_name)
    words = file.readlines()
    file.close()
    return [word[:5] for word in words]


words = load_dict("words.txt")
final_word = False
while final_word == False:
    # asks the user for there guess
    guess_letter = input('Input your letter: ')
    if guess_letter == "done":
        exit()
    guess_color = input('What is the color(Y,G,B): ')
    # filters for grey letters
    if guess_color == "b" or guess_color == 'B':
        words = list(filter(lambda s: guess_letter.strip() not in s, words))
        print(', '.join(words))
        print('-------------------------------------------------------------------------')
        continue
    letter_pos = int(input('what pos: '))
    # filters for green letters
    if guess_color == "G" or guess_color == "g":
        words = list(
            filter(lambda s: s[letter_pos-1] == guess_letter.strip() in s, words))
        print(", ".join(words))
        print('-------------------------------------------------------------------------')
        continue
    # filters for yellow letters
    elif guess_color == "y" or guess_color == "Y":
        words = list(filter(lambda s: guess_letter.strip() in s, words))
        words = [
            word
            for word in words
            if word[letter_pos-1] != guess_letter
        ]
        print(', '.join(words))
        print('-------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------')
