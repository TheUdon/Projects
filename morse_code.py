alpha_morse_dict = {"A": ".-",
                  "B": "-...",
                  "C": "-.-.",
                  "D": "-..",
                  "E": ".",
                  "F": "..-.",
                  "G": "--.",
                  "H": "....",
                  "I": "..",
                  "J": ".---",
                  "K": "-.-",
                  "L": ".-..",
                  "M": "--",
                  "N": "-.",
                  "O": "---",
                  "P": ".--.",
                  "Q": "--.-",
                  "R": ".-.",
                  "S": "...",
                  "T": "-",
                  "U": "..-",
                  "V": "...-",
                  "W": ".--",
                  "X": "-..-",
                  "Y": "-.--",
                  "Z": "--..",
                  "1": ".----",
                  "2": "..---",
                  "3": "...--",
                  "4": "....-",
                  "5": ".....",
                  "6": "-....",
                  "7": "--...",
                  "8": "---..",
                  "9": "----.",
                  "0": "-----",
                  ".": ".-.-.-",
                  ",": "--..--",
                  "?": "..--..",
                  " ": "/"}

key_list = list(alpha_morse_dict.keys())
val_list = list(alpha_morse_dict.values())

command = input("Type Decode to decode morse code or type Encode to encode text to morse code: ")

while command.upper() != "ENCODE" and command.upper() != "DECODE":
    command = input("Invalid command. Please type either 'Decode' or 'Encode': ")


if command.upper() == "ENCODE":
    message = input("What word or phrase would you like to encode? ").upper()
    morse_code = []
    for x in message:
        morse_code.append(f"{alpha_morse_dict[x]} ")
    print(f"Here is your encoded message:\n{''.join(morse_code)}")

elif command.upper() == "DECODE":
    message = input("Input the morse code you would like to decode? ")
    decoded_message = []
    letter = []
    count = 0
    print(len(message))
    for x in message:
        count += 1
        letter.append(x)
        print(count)
        if count == len(message):
            if x == " ":
                letter = letter[:-1]
            position = val_list.index("".join(letter))
            decoded_message.append(key_list[position])
            print(f"Here is your decoded message:\n{''.join(decoded_message)}")
        if x == " ":
            print(letter)
            letter = letter[:-1]
            morse_letter = "".join(letter)
            position = val_list.index(morse_letter)
            decoded_message.append(key_list[position])
            letter = []