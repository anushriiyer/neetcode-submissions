class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for string in strs:
            encoded += str(len(string))
            encoded+="#"
            encoded += string
            
        
        return encoded


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            word_start = j+1
            word_end = word_start+length

            word = s[word_start:word_end]
            res.append(word)

            i = word_end
        return res
