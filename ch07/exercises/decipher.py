def caesar_cipher(text, shift):
    """
  decrypts a message using the Caesar cipher technique.

    args:
        text:str = the message to encrypt or decrypt
        shift:int = the number of positions to shift each letter
    return:
        :str = the encrypted or decrypted message
    """

    result = ""
    for char in text:
        if char.isalpha():
            # Determine the case of the character
            start = ord('A') if char.isupper() else ord('a')
            # Calculate the new position of the character after the shift
            new_pos = (ord(char) - start + shift) % 26
            # Convert the new position back to a character
            char = chr(start + new_pos)
        result += char
    return result

# def text():
#     text = "cipher.txt"
#     cipher = open(text, "r").read()
   
    

def main():
    text = open("encription.txt","r").read()
    decripted = caesar_cipher(text, -8)
    code_write = open("decrypted.txt", "w")
    code_write.write(decripted)
    code_write.close()
main()