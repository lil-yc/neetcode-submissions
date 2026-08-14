class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right: # stop when pointers pass over
            total = numbers[left] + numbers[right] # sum

            if total == target: # found indices
                return [left + 1, right + 1]
            elif total > target: # sum too large
                right -= 1 # decrease right value
            else: # sum too small
                left += 1 # increase left value