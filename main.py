def welcome_speech(line):
    print(f"""Добро пожаловать в игру Hangman
    Ваша задача угадать загаданное слово за несколько попыток,
    иначе вас ждет расплата!
    Загаданное слово состоит из {len(line)} букв {line} """)

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
    template = start_template(word_in_play)
    a = list_to_string_convert(template)
    welcome_speech(list_to_string_convert(template))

game()

