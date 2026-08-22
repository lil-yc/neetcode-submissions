class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1 # check first and last lines
        water = 0
        while i < j:
            water = max(water, (j - i) * min(heights[i], heights[j]))
            if heights[i] < heights[j]: # remove the smaller line from consideration
                i += 1
            else:
                j -= 1
        return water
        