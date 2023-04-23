#to make a dictionary password generator that replace the similar char in each word with a special char
#example: alphalionmidget ->@lphal1onmidg3t or alphalionmidget ->@lphal!onmidg3t
#password must be unique and cannot generate the same password twice
#password format is word1 + random special char + word2 + random special char + word3 + random special char + word4



import random
import Oxford English Dictionary.txt

with open("Oxford English Dictionary.txt", "r") as f:
    words = [word.strip() for word in f.readlines()]

nr_words = int(input("Enter the number of words to include in the password: "))

password_list = []

for i in range(nr_words):
    password_list.append(random.choice(words))

password = " ".join(password_list)

dictionary_password = {
    "words": password
}

print(dictionary_password)