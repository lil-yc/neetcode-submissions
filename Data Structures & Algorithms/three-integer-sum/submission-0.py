class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)): 
            if i > 0 and nums[i] == nums[i-1]:
                continue # if curr is dupe of prev, skip
            
            j = i + 1 # next elem
            k = len(nums) - 1 # end elem

            while j < k: # two pointer with j & k
                total = nums[i] + nums[j] + nums[k]

                if total > 0: # total too large
                    k -= 1
                elif total < 0: # total too small
                    j += 1
                else: # found triplet
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1  

                    while nums[j] == nums[j-1] and j < k:
                        j += 1 # skip dupes
        
        return res