class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # freq map 
        for num in nums: # populate freq map
            count[num] = 1 + count.get(num, 0)

        heap = [] # min heap
        for num in count.keys():
            heapq.heappush(heap, (count[num], num)) # sorted by count
            if len(heap) > k: # remove exceeding k
                heapq.heappop(heap) # removes smallest elem

        res = []
        for i in range(k): # put top k elems from min heap
            res.append(heapq.heappop(heap)[1])
        return res