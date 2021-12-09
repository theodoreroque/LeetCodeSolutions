class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hMap = {}
        
        for i in range(len(nums)):
            if target - nums[i] in hMap:
                return (i, hMap[target - nums[i]])
            else:
                hMap[nums[i]] = i
