import random

def guess():
    """Random guessing game
       You should check whether n = number 
       You should use a while loop to keep reading numbers from the user while n!=randnumber
       If the number user enters (n) is smaller than randnumber, you should display too low
       If the number user enters (n) is larger than randnumber, you should display too high
       You should read another number
    """
    rand = random.randint(1,100) # Number is picked randomly

    n = int(input()) # Number you read from the user
    while n != rand:
        if n < rand:
            print("Too low")
        elif n > rand:
            print("Too high")
        n = int(input())

    print("Correct")

guess()

      
