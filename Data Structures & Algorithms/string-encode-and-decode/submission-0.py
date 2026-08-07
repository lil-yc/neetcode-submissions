class Solution:

    def encode(self, strs: List[str]) -> str:
        res = [] 
        for s in strs: # write length#string
            res.append(str(len(s))) # prefix with length
            res.append("#") # marker between length and content
            res.append(s)
        return "".join(res) # convert list to string


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # i points to start of one segment

        while i < len(s):
            j = i # j points to end of one segment
            while s[j] != '#': 
                j += 1
            length = int(s[i:j]) # get the length

            i = j + 1 # get start of string
            j = i + length # get end of string
            res.append(s[i:j]) # append to list
            i = j # go to next segment

        return res 