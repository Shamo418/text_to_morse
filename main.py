# A simple program that prints input text into Morse code.

# Morse code
letters_morse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'
}

digit_morse = {
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}

space_morse = {
    ' ': '/'
}

text_to_morse = input("Text to change into morse code:\n")

list_from_text = [letter for letter in text_to_morse]

text_in_morse = []
for item in list_from_text:
    upper_letter = item.upper()
    if letters_morse.get(upper_letter) is not None:
        morse_code = letters_morse.get(upper_letter)
    elif digit_morse.get(upper_letter) is not None:
        morse_code = digit_morse.get(upper_letter)
    elif space_morse.get(upper_letter) is not None:
        morse_code = space_morse.get(upper_letter)
    else:
        print(f"Error in text: {item} not used symbol."
              f"Yours morse code will not have this symbol")
    text_in_morse.append(morse_code)


morse_text = ' '.join(text_in_morse)
print(morse_text)
