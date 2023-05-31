class solution(object):
    def topKFrequent(self, nums , k):
        
        hashTable = {}
        outputArr = [[] for in range(len(nums) + 1)]
        # Bucket Sort
        for c in set(nums):
            hashTable[c] = 1 + hashTable.get(c,0)
        for n, c in hashTable.items():
            outputArr[c].append(n)

        res = []
        for i in range(len(outputArr) - 1, 0, -1):
            for n in outputArr[i]:
                res.append(n)
                if len(res) == k:
                    return res
        #O(n)
            
            

        