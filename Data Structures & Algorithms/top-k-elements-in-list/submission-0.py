class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # frequency map 
        freq = [[] for i in range(len(nums) + 1)] # index: count, value: num

        for num in nums: # populate freq map
            count[num] = 1 + count.get(num, 0)   

        for num, cnt in count.items(): # populate freq list
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1): # start from largest index
            for num in freq[i]: # each freq may have multiple nums
                res.append(num)
                if len(res) == k: # got top k elems
                    return res