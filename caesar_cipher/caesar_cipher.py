import nltk

"""
ord changes letters to number
chr changes number to letter

A - 65
Z - 90
a - 97
z - 122
' '-32

- encrypt(‘abc’,1) would return ‘bcd’ 
- encrypt(‘abc’, 10) would return ‘klm’
- shifts that exceed 26 should wrap around
  - encrypt(‘abc’,27) would return ‘bcd’

function
- check if key is greater than 25
  - if it is convert key to

  delcare result string
- iterate through each letter


    - declare converted = ord(letter)
    - check for lower or uppercase
    - if LOWERCASE
      (this means converted between 97-122)
      - changed = converted + key
      - if changed is greater than 122
          - find out the difference beween converted and 122
          - modulo that difference 25 or 26
          - add that difference to 97
          - then we have the encrypted letter


    - if uppercase
      (this means converted between 65-90)
      - changed = converted + key
      - if changed is greater than 90
          - find out the differenc between converted and 90
          - modulo that difference
          - add the difference to 65
          - then the the encrypted letter. 

    - if it neither
      just add the character

"""


def encrypt(plaintext, key):
    string = ""

    for char in plaintext:
        converted = ord(char)

        if converted >= 97 and converted <= 122:
            added = converted + key
            if added > 122 or added < 97:
                difference = added - 123
                modulo = difference % 26
                modadd = 97 + modulo
                string += chr(modadd)
            else:
                string += chr(added)

        elif converted >= 65 and converted <= 90:
            added = converted + key
            if added > 90 or added < 65:
                difference = added - 91
                modulo = difference % 26
                modadd = 65 + modulo
                string += chr(modadd)
            else:
                string += chr(added)

        else:
            string += char

    return string


def decrypt(encryptedText, key):
    return encrypt(encryptedText, -key)


if __name__ == "__main__":

    input1 = "ABCD"
    input2 = "abcd"
    input3 = "ABab"
    input4 = "AB ab AB cd dfadf  fasdf"

    input5 = "Hello World. We did it."

    result1 = encrypt(input5, 1453)
    print(result1)

    result2 = decrypt(result1, 1453)
    print(result2)
