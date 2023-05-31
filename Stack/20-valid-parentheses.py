class Solution(object):
    def isValid(self, s):
        
        stack = []
        hashTable = {'{' : '}', '[' : ']', '(' : ')'}

        if len(s) <= 1:
            return False
         
        for c in (s):
            if (stack != [] and c == hashTable.get(stack[-1]) ):
                stack.pop()
            else:
                stack.append(c)
            if(stack == [] and c == s[-1]):
                return True
                
        return False