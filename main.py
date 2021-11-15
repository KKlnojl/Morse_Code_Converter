# Add a ASCⅡ ART
# https://ascii.co.uk/art

cover = '''

888b     d888                                          .d8888b.                888                .d8888b.                                  
8888b   d8888                                         d88P  Y88b               888               d88P  Y88b                                 
88888b.d88888                                         888    888               888               888    888                                 
888Y88888P888  .d88b.  888d888 .d8888b   .d88b.       888         .d88b.   .d88888  .d88b.       888         8888b.  88888b.d88b.   .d88b.  
888 Y888P 888 d88""88b 888P"   88K      d8P  Y8b      888        d88""88b d88" 888 d8P  Y8b      888  88888     "88b 888 "888 "88b d8P  Y8b 
888  Y8P  888 888  888 888     "Y8888b. 88888888      888    888 888  888 888  888 88888888      888    888 .d888888 888  888  888 88888888 
888   "   888 Y88..88P 888          X88 Y8b.          Y88b  d88P Y88..88P Y88b 888 Y8b.          Y88b  d88P 888  888 888  888  888 Y8b.     
888       888  "Y88P"  888      88888P'  "Y8888        "Y8888P"   "Y88P"   "Y88888  "Y8888        "Y8888P88 "Y888888 888  888  888  "Y8888                                                                                                                                              
                                                                                                                                                                                                    
'''

print(cover)

# Create a dictionary with international morse code
# 建立一個儲有基本重要的國際通用摩斯密碼的字典
morse_dict = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
              "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--",
              "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...",
              "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
              "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
              "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
              ".": ".-.-.-", ":": "---...", ",": "--..--", ";": "-.-.-.", "?": "..--..",
              "=": "-...-", "'": ".----.", "/": "-..-.", "!": "-.-.--", "-": "-....-",
              "_": "..--.-", '"': ".-..-.", "(": "-.--.", ")": "-.--.-", "$": "...-..-",
              "&": ".-...", "@": ".--.-.", "+": ".-.-.", " ": "/"}

''' --------------------------------------- Define Functions -------------------------------------'''


# Create a function to add/change a morse code
# 建立一個新增摩斯密碼對照表的function
def morse_add(enter, output):
    # Double check if user wants to change the international morse code
    if enter in morse_dict.keys():
        a1 = input("Are you going to change the international morse code to your own morse code? (Y/N)\n").upper()
        if a1 == "Y":
            morse_dict[enter] = output
        elif a1 == "N":
            pass
        else:
            print("Please enter 'Y' or 'N'.")
            morse_add(enter, output)
    # Double check if user wants to add a customized morse code
    else:
        a2 = input("Do you really want to add this new morse code? (Y/N)\n").upper()
        if a2 == "Y":
            morse_dict[enter] = output
        elif a2 == "N":
            pass
        else:
            print("Please enter 'Y' or 'N'.")
            morse_add(enter, output)


# Create an input box
def say():
    sentences = input("Please enter anything that you want to convert to morse codes:\n").upper()
    for letter in sentences:
        if letter in morse_dict.keys():
            pass
        else:
            print(f"Sorry {letter} hasn't been defined in the dictionary of morse codes, Please enter again.")
            sentences = say()
    return sentences


# Create a morse code converter
def morse_converter(says):
    converted = list()
    for letter in says:
        if letter in morse_dict.keys():
            converted.append(morse_dict[letter])
    return " ".join(converted)


# Create an inquiry to ask user about the word they want to add.
def inquiry():
    word = input("Please enter what the words/letters you want to set for a morse code : \n").upper()
    code = input("Then, please enter your customized code to convert the word above to a morse code : \n").upper()
    return word, code


# Create a encode function:
def encode():
    choice = input("If you want to customize your morse codes, please enter 'Y'.\n"
                   "If you enter other letters, you're going to use a list of simple"
                   "international morse code to convert your sentences.\n").upper()
    # Enter a new word or letter to customize a morse code.
    # Then ask for entering statements that user wants to convert, and show the results.
    if_end = False
    if choice == "Y":
        while not if_end:
            words, codes = inquiry()
            morse_add(words, codes)
            check_if_end = input("Have you done with customizing your morse code? (Y/N)\n").upper()
            if check_if_end == "Y":
                if_end = True
        saying = say()
        converted_sentences = morse_converter(saying)
        print(f"Here's the morse code: {converted_sentences}")
    else:
        saying = say()
        converted_sentences = morse_converter(saying)
        print(f"Here's the morse code: \n{converted_sentences}")


# Create a encode function:
def decode():
    lst = []
    sentences = []
    morse_code = input("Please type your Morse Codes: \n").upper()
    # 拆出各letters
    sentence = morse_code.split(" ")
    # 取出各values對應的keys
    try:
        for morse in sentence:
            lst.append(morse)
            l = [key for key, value in morse_dict.items() if value == morse]
            sentences.append(l[0])
        sentences = "".join(sentences)
        print(f"This is the Sentences: \n{sentences}")
    except IndexError:
        print("Sorry, what you typed might not be a correct morse code. Please try again")
        decode()


# Create a encode or decode input box:
def task():
    mission = input("Please type '1' to encode the sentences to convert it to Morse codes\n"
                    "Please type '2' to decode the morse to the sentences.\n")
    if mission == "1":
        encode()
    elif mission == "2":
        decode()
    else:
        print("Wrong typing.")
        task()


''' --------------------------------------- Start the Game -------------------------------------'''
# Start from asking user if they want to customize their own morse codes.
print("Hi, welcome to Morse Code Game. Here you can use either international codes or customized codes to convert "
      "sentences to morse codes.\n")
print("++++++++++++++++++++++++++++++++++++++++++++++ Let's Get started ++++++++++++++++++++++++++++++++++++++++++++\n")

task()
