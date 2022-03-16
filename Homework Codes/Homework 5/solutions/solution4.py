phrase = '''John-Michael and, friends from town drink wine.
I eat bread!
For 5 years, we bring red wine from town, from Mary.'''

alphabet = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"

english_to_french_dictionary = {"bread": "pain", "wine": "vin", "bring": "apporter", "I": "Je", "eat": "mange",
                                "drink": "bois", "John-Michael": "Jean-Michel", "friends": "amis", "and": "et",
                                "of": "du", "red": "rouge", "from": "de", "town": "ville", "we": "nous",
                                "Mary": "Marie", "For": "Pour", "years": "ans"}

for line in phrase.split("\n"):
    translated_phrase = ''''''
    for word in line.split():
        if set(digits) & set(word.lower()) == set(word.lower()):
            print(word, end=" ")
        elif set(alphabet) & set(word.lower()) != set(word.lower()) and word[-1] not in alphabet:
            print(english_to_french_dictionary[word[:-1]], end="")
            print(word[-1], end=" ")
        else:
            print(english_to_french_dictionary[word], end=" ")
    print()

# print(translated_phrase)
