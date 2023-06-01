class Solution(object):
    def isPalindrome(self, s):
        head = 0
        tail = len(s) -1
        while head <= tail:
            if not (self.isAlphaNum(s[head])):
                head =+ 1
            elif not(self.isAlphaNum(s[tail])):
                tail =- 1
            else:
                if (s[head].toLowerCase() != s[tail].toLowerCase()):
                    return False
                head =+1
                tail =-1
            
        return True
                
    def isAlphaNum(self, c):
        if (ord(c) >= 48 and ord(c) <= 57) or (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 65 and ord(c) <= 90):
            return True
        return False