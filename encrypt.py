from math import floor

Cipher = {
    "a" : 1,
    "A" : 2,
    "b" : 3,
    "B" : 4,
    "c" : 5,
    "C" : 6,
    "d" : 7,
    "D" : 8,
    "e" : 9,
    "E" : 10,
    "f" : 11,
    "F" : 12,
    "g" : 13,
    "G" : 14,
    "h" : 15,
    "H" : 16,
    "i" : 17,
    "I" : 18,
    "j" : 19,
    "J" : 20,
    "k" : 21,
    "K" : 22,
    "l" : 23,
    "L" : 24,
    "m" : 25,
    "M" : 26,
    "n" : 27,
    "N" : 28,
    "o" : 29,
    "O" : 30,
    "p" : 31,
    "P" : 32,
    "q" : 33,
    "Q" : 34,
    "r" : 35,
    "R" : 36,
    "s" : 37,
    "S" : 38,
    "t" : 39,
    "T" : 40,
    "u" : 41,
    "U" : 42,
    "v" : 43,
    "V" : 44,
    "w" : 45,
    "W" : 46,
    "x" : 47,
    "X" : 48,
    "y" : 49,
    "Y" : 50,
    "z" : 51,
    "Z" : 52,
    "0" : 53,
    "1" : 54,
    "2" : 55,
    "3" : 56,
    "4" : 57,
    "5" : 58,
    "6" : 59,
    "7" : 60,
    "8" : 61,
    "9" : 62,
    "#" : 63
}

def get_key_by_value(dictionary, target_value): # function to retrieve the key by value
    for key, value in dictionary.items():  # Iterate through key-value pairs
        if value == target_value:  # If the value matches the target value
            return key
    return "Key not found"  # If no key with the target value is found

# --- Encryption ---
def CreateCleanedStr(Text: str, doPrintSplitStr: bool = False):
    Spaced = Text.split(' ')
    Exploded = []

    for str in Spaced:

        if "?" in str:
            Exploded.append(str.removesuffix("?"))
            for letter in str:
                if "?" == letter:
                    Exploded.append('#Q') #QUESTIONMARK
        elif "!" in str:
            Exploded.append(str.removesuffix("!"))
            for letter in str:
                if "!" == letter:
                    Exploded.append('#E') #EXCLAMATIONPOINT
        elif ":" in str:
            Exploded.append(str.removesuffix(":"))
            for letter in str:
                if ":" == letter:
                    Exploded.append('#COL') #COLON
        elif "." in str:
            Exploded.append(str.removesuffix("."))
            for letter in str:
                if "." == letter:
                    Exploded.append('#DO') #DOT
        elif "," in str:
            Exploded.append(str.removesuffix(","))
            for letter in str:
                if "," == letter:
                    Exploded.append('#COM') #COMMA
        elif "'" in str:
            Exploded.append(str.removesuffix("'"))
            for letter in str:
                if "'" == letter:
                    Exploded.append('#S') #SINGLEQUATMARKS
        elif "’" in str:
            Exploded.append(str.removesuffix("’"))
            for letter in str:
                if "’" == letter:
                    Exploded.append('#A') #APOSTROPHY 
        elif "-" in str:
            Exploded.append(str.removesuffix("-"))
            for letter in str:
                if "-" == letter:
                    Exploded.append('#DE') #DESH
        elif "—" in str:
            Exploded.append(str.removesuffix("—"))
            for letter in str:
                if "—" == letter:
                    Exploded.append('#LDE') #LONGDESH
        elif "%" in str:
            Exploded.append(str.removesuffix("%"))
            for letter in str:
                if "%" == letter:
                    Exploded.append('#P') #PRECENT
        else :
            Exploded.append(str)

    chars_to_remove = ["!", "?", ":", ".", "-", "'", ",", "—", "’", "%"] # Characters you want to remove
    # Iterate over each word in the list and remove unwanted characters
    for i in range(len(Exploded)):
        new_word = ''.join([ch for ch in Exploded[i] if ch not in chars_to_remove])  # Rebuild word without specific chars
        Exploded[i] = new_word  # Replace word in the list with the cleaned one

    if doPrintSplitStr : print("\n", Exploded)

    Joined = " ".join(Exploded)
    # print("\n", Joined)
    return Joined


def CreateStrSizedPass(SplitStr: str, Pass: str):
    Exploded_Text = SplitStr.split(" ")
    StrShapedPassword = []
    password_letter_counter = 0

    for i in range(0, len(Exploded_Text)): # look through words in list
        reconstruncted_word = []
        for j in range(0, len(Exploded_Text[i])): # look throudh letters in word
            if j == len(Exploded_Text)-1: break

            reconstruncted_word.append(Pass[password_letter_counter])

            if password_letter_counter == len(Pass)-1:
                password_letter_counter = 0
            else :
                password_letter_counter += 1

        StrShapedPassword.append(reconstruncted_word)

    subLists = []
    for lists in StrShapedPassword:
        subLists.append("".join(lists))

    Joined = " ".join(subLists)
    # print("\n", Joined)
    return Joined

def CreateEncryptedText(Clean: str, StrSizedPass: str):
    Encrypted = ""
    Exp_Clean = Clean.split(' ')
    Exp_Pass = StrSizedPass.split(' ')
    encrypted_reconstruction = []

    for i in range(0, len(Exp_Clean)):
        subList = []
        for j in range(0, len(Exp_Clean[i])):
            if j == len(Exp_Clean)-1: break

            if Exp_Clean[i][j] == "#":
                encrypted_reconstruction.append(Exp_Clean[i][j]+Exp_Clean[i][j+1])
                break
            else :
                clean_letter_val = Cipher[Exp_Clean[i][j]]
                pass_letter_val  = Cipher[Exp_Pass[i][j]]

                encrypted_letter_val = floor((clean_letter_val + pass_letter_val) / 2)
                subList.append(get_key_by_value(Cipher, encrypted_letter_val))

        encrypted_reconstruction.append("".join(subList))

    for i in range(0, len(encrypted_reconstruction)):
        if i == len(encrypted_reconstruction)-1: break

        if len(encrypted_reconstruction[i]) < 1:
            encrypted_reconstruction.pop(i)

    for word in encrypted_reconstruction:
        Encrypted += word+" "

    return Encrypted

def Encrypt():    
    Input = input("Text >>> ")
    Password = input("Password >>> ")

    CleanStr = CreateCleanedStr(Input)
    StrSizedPass = CreateStrSizedPass(CleanStr, Password)
    Enc = CreateEncryptedText(CleanStr, StrSizedPass)

    return Enc

print(Encrypt())
