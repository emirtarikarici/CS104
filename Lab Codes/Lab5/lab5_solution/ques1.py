
def isPalindrome(inp):
    inp = inp.lower()
    # Run loop from 0 to len/2
    for i in range(0, int(len(inp)/2)):
        if inp[i] != inp[len(inp)-i-1]:
            return False
    return True

def testIsPalindrome():
    print('Try dogGod')
    print(isPalindrome('dogGod'))
    print('Try doGood')
    print(isPalindrome('doGood'))

testIsPalindrome()
