import requests

paraula = requests.get("https://clientes.api.greenborn.com.ar/public-random-word").text.split("\"")[1]


def get_random_word():
    response = requests.get("https://clientes.api.greenborn.com.ar/public-random-word")
    word = response.text.split("\"")[1]
    return word

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def get_user_guess():
    guess = input("Introduce una letra o intenta adivinar la palabra: ")
    return guess

def update_word(word, guess, guessed_letters):
    if len(guess) == 1:
        guessed_letters.append(guess)
    return display_word(word, guessed_letters)

def play_game():
    word = get_random_word()
    guessed_letters = []
    attempts = 10
    game_over = False

    print("¡Bienvenido al juego del ahorcado!")
    print(display_word(word, guessed_letters))

    while not game_over:
        guess = get_user_guess()
        if len(guess) > 1:
            if guess == word:
                print("¡Has adivinado la palabra!")
                game_over = True
            else:
                attempts -= 1
                print(f"Incorrecto. Te quedan {attempts} intentos.")
        else:
            if guess in word:
                print("¡Correcto!")
                print(update_word(word, guess, guessed_letters))
                if '_' not in update_word(word, guess, guessed_letters):
                    print("¡Has ganado!")
                    game_over = True
            else:
                attempts -= 1
                print(f"Incorrecto. Te quedan {attempts} intentos.")
        if attempts == 0:
            print("Has perdido. La palabra era: " + word)
            game_over = True