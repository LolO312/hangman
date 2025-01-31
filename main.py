def welcome_speech(line):
    print(f"""Добро пожаловать в игру Hangman
    Ваша задача угадать загаданное слово за несколько попыток,
    иначе вас ждет расплата!
    Загаданное слово состоит из {len(line)} букв {line} """)

def get_word(words):
    return words[0]

def list_to_string_convert(strings):
    # string = ""
    # for i in strings:
    #     string += i
    # return string
    return ''.join(strings)

def start_template(word):
    return len(word) * ["_"]

def build_template(symbols, word, letter):
    for i in range(len(word)):
        if word[i] == letter:
            symbols[i] = letter
    return symbols

def game():
    progress = True
    word = ["orange"]
    lifes = 3
    word_in_play = get_word(word)
    template = start_template(word_in_play)
    a = list_to_string_convert(template)
    welcome_speech(list_to_string_convert(template))

    while progress:
        user_guess = input("Введите букву: ")
        template = build_template(template, word_in_play, user_guess)
        guessed = list_to_string_convert(template)
        print(f"Результат: {guessed}")
        # progress = check_win(guessed)
        #
        # if not check_mistake(word_in_play, user_guess):
        #     print(f"Осталось {lifes} попытки")
        #     lifes = check_attempt(lifes)
        #
        # if lifes == 0:
        #     lose_speech()
        #     break
        #
        # if not progress:
        #     win_speach()

game()

