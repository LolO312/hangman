def get_word(words):
    return words[0]

def start_template(word):
    return len(word) * ["_"]

def game():
    progress = True
    word = ["orange"]
    lifes = 3
    word_in_play = get_word(word)
    template = start_template(word_in_play)

game()
print("Добро пожаловать в игру Hangman")
