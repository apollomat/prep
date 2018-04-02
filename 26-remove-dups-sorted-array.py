class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) <= 1):
            return len(nums) 
        
        # 1 1 2 
        start_index = 1
        size = len(nums) - 1
        for i in range(1, len(nums)):

            if(nums[i] != nums[i-1]):
                nums[start_index] = nums[i]
                start_index += 1
                
                
        return start_index
