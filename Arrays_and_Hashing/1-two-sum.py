class solution(object):
    def twoSum(self, nums, target):
        
        for i in range(len(nums)):
            for c in nums:
                if (nums[i] + nums[c] == target):
                    return True
                
        return False
    
    # o(n2)

    def twoSum(self, nums, target):

        hashNums = {}

        for i, num in enumerate(nums):
            if target - num in hashNums.keys():
                return [hashNums[target-num], i]




