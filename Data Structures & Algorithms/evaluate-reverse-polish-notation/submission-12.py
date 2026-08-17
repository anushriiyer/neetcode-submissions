class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        
        if len(tokens)==1:
            return int(tokens[0])

        for token in tokens:
            if token in "+-*/":
                second = stack.pop()
                first = stack.pop()
                
                if token == "+":
                    stack.append(first+second)
                elif token == "-":
                    stack.append(first-second)
                elif token == "/":
                    stack.append(int(float(first) / second))
                elif token =="*":
                    stack.append(first*second)
            else:
                stack.append(int(token))
        
        return stack.pop()
        