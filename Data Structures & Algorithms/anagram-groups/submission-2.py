class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            sort = tuple(sorted(word))
            if sort in hashmap:
                hashmap[sort].append(word)
            else:
                hashmap[sort] = [word]

        output = list(hashmap.values())
        return output
