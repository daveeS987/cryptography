import nltk

"""
ord(char) changes letter -> number
chr(num) changes number -> letter

A - 65
Z - 90
a - 97
z - 122

- encrypt(‘abc’,1) would return ‘bcd’ 
- encrypt(‘abc’, 10) would return ‘klm’
- shifts that exceed 26 should wrap around
  - encrypt(‘abc’,27) would return ‘bcd’

def encrypt function

  declare result string
  iterate through each letter 

    declare int_char = ord(letter)
    check for lower or uppercase
    
    if LOWERCASE
      (this means int_char between 97-122)
      keyed = int_char + key
      if keyed is greater than 122
          find out the difference beween keyed and 122
          modulo that difference by 26
          add that difference to 97
          push the result to result string


    if UPPERCASE
      (this means int_char between 65-90)
      keyed = int_char + key
      if keyed is greater than 90
          find out the difference between keyed and 90
          modulo that difference
          add the difference to 65
          push the result to result string

    if its neither
      just add the character to result string

"""


def encrypt(plaintext, key):
    string = ""

    for char in plaintext:
        int_char = ord(char)

        if int_char >= 97 and int_char <= 122:
            keyed = int_char + key
            if keyed > 122 or keyed < 97:
                difference = keyed - 123
                modulo = difference % 26
                string += chr(97 + modulo)
            else:
                string += chr(keyed)

        elif int_char >= 65 and int_char <= 90:
            keyed = int_char + key
            if keyed > 90 or keyed < 65:
                difference = keyed - 91
                modulo = difference % 26
                string += chr(65 + modulo)
            else:
                string += chr(keyed)

        else:
            string += char

    return string


def decrypt(encryptedText, key):
    return encrypt(encryptedText, -key)


def crack(encrypted_string):
    pass


if __name__ == "__main__":

    input1 = "ABCD"
    input2 = "abcd"
    input3 = "ABab"
    input4 = "AB ab AB cd dfadf  fasdf"
    input5 = "Hello World. We did it."

    result1 = encrypt(input5, 27)
    print(result1)

    result2 = decrypt(result1, 27)
    print(result2)
