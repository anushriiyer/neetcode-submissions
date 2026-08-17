class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        index = 0
        appended = 0
        for word in strs:
            appended = 0
            for key, anagram in hashmap.items():
                if sorted(anagram[0]) == sorted(word) and len(anagram[0]) == len(word):
                    hashmap[key].append(word)
                    appended = 1
            if appended == 0:  # Fixed the equality comparison (was '=' instead of '==')
                hashmap[index] = [word]
                index += 1

        output = list(hashmap.values())
        output_copy = [lst.copy() for lst in output]

        return output_copy
