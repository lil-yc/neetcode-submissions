class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {} # map value -> index

        for i in range(len(nums)): # 1 pass over nums
            diff = target - nums[i] # difference required to make target
            if diff in nums_map: # efficient hashmap check
                return [nums_map[diff], i] # found the pair
            nums_map[nums[i]] = i # insert current value -> index

        return [] # no pair found