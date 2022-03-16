alphabet = "abcdefghijklmnopqrstuvwxyz"

letters_in_text = dict()
with open("./quotes.txt", "r") as f:
    for line in f:
        for word in line.split():
            for character in word.lower():
                if character not in alphabet:
                    continue
                if character not in letters_in_text:
                    letters_in_text[character] = 1
                else:
                    letters_in_text[character] += 1

with open("./letter_count.dat", "w") as f:
    for letter in alphabet:
        if letter in letters_in_text:
            f.write(letter + " " + str(letters_in_text[letter]) + "\n")
