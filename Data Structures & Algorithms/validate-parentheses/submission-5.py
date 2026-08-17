class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        stack = []
        for bracket in s:
            if bracket in '({[':
                stack.append(bracket)
            else:
                    if stack:
                        top = stack.pop()
                    else: return False
                    if bracket== ")" and top != "(":
                        return False
                    elif bracket== "}" and top != "{":
                        return False
                    elif bracket== "]" and top != "[":
                        return False
        
        if stack:
            return False
        else: 
            return True


        