class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)

        for i, num in enumerate(nums): 
            ans[i] = ans[i + n] = num # 1 pass set both
        return ans