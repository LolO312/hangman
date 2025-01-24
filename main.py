def get_word(words):
    return words[0]

def list_to_string_convert(strings):
    strr = ""
    for i in strings:
        strr += str(i)
        strr += ""
    return strr

def start_template(word):
    return len(word) * ["_"]

def game():
    progress = True
    word = ["orange"]
    lifes = 3
    word_in_play = get_word(word)
    template =start_template(word_in_play)
    a = list_to_string_convert(template)
    print(a)

game()
print("Добро пожаловать в игру Hangman")
