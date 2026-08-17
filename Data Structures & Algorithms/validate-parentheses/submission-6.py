class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        pdict = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for c in s:
            if c in pdict:
                if stack:
                    if stack.pop() == pdict[c]:
                        continue
                    else:
                        return False
                else: 
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False


        