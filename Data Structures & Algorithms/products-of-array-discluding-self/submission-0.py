class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums) # init output array with 1's
        
        left = 1 
        for i in range(len(nums)): # compute left-side product
            output[i] *= left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1): # compute right-side product
            output[i] *= right
            right *= nums[i]
    
        return output 
        