class Solution:
    def is_valid_parentheses(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False

        return len(stack) == 0

print(Solution().is_valid_parentheses("(){}[]"))
print(Solution().is_valid_parentheses("()[{)}"))
print(Solution().is_valid_parentheses("([])"))
