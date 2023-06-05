class solution(object):
    def isAnagram(self, s, t):

        countS, countT = {},{}

        if (s.length() == t.length()):
            return False
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)

        for c in countS:
            if countS[c] != countT[c]:
                return False
        return True