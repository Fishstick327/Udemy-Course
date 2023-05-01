alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
  #empty string to store value into the encrypted_text
    encrypted_text = ""
    for char in text:
      #char.isalpha() is to check if the char is from the alphabet and not the special char or number. other wise the scramble can be off since it has to shift those too.
        if char.isalpha():
          #this formula use ord() to get the ASCII code from the letter a = 97. then use the chr() to convert it back into letter. The modulo is wrap into the formula basically continue with the shift as it reach the end. so if z is to shift by 1 then it now be a instead of giving error. 
          #the formula basically subtract 97(a) from the ASCII to get the position in the alphabet, which has 26 char 0-25. Then add the shift ammount and % 26 to make it wrap around the alphabet. then add the 97 back to the shifted char.
          shifted_char = chr((ord(char) - 97 + shift) % 26 + 97)
          encrypted_text += shifted_char
        else:
          encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
  decrypt_text = ""
  for char in text:
    if char.isalpha():
      #the - 97 here is to get the alphabet position of the char. then - the shift ammount. then % 26 to wrap around the alphabet. then add 97 back to get the ASCII code of the char.
      
      shift_char = chr((ord(char) - 97 - shift) % 26 + 97)
      decrypt_text += shift_char
    else:
      decrypt_text += char
  return decrypt_text


  
if direction == "encode":
    encrypted_text = encrypt(text, shift)
    print(f"Here is the encoded result: {encrypted_text}")
elif direction == "decode":
    decrypt_text = decrypt(text, shift)
    print(f"Here is the decoded result: {decrypt_text}")
    
else:
    print("Invalid input. Please try again.")