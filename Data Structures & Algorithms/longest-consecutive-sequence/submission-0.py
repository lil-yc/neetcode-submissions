class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # allows for O(1) checking if exists
        longest = 0 # the longest sequence length

        for n in num_set: # 1 pass over nums
            if n - 1 not in num_set: # found a starting num
                length = 1 # init curr sequence length

                while n + length in num_set: # the next num exists
                    length += 1
                
                longest = max(longest, length) # update longest
        
        return longest
