class solution(object):
    def groupAnagrams(self, strs):
        
        hashMap = {}
        for s in strs: 
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            hashMap[count].append(s)

        return hashMap.keys()
    
    # O(n*m)