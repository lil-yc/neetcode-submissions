class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # map freq list -> string

        for s in strs: # for every string
            count = [0] * 26 # frequency list, index corresponds to letter

            for c in s: # populate the freq list
                count[ord(c) - ord('a')] += 1 

            res[tuple(count)].append(s) # use count tuple (freq list) as key

        return list(res.values())