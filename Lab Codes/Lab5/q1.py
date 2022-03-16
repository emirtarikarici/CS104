# Write a method named “isPalindrome” 
# which takes as parameter a string 
# and returns True if input string is a palindrome; False otherwise. 
# Capitalization can be ignored by using ‘lower()’ method of a given string.

def isPalindrome():
    word = str(input("Write a word: ")).lower()
    if word == word[::-1]:
        return True
    else:
        return False 

print(isPalindrome())