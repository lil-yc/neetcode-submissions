class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums) # create frequency map

        for key, value in freq.items(): 
            if value != 1: # appears more than once
                return True
        return False