class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp = []
        for c in tokens:
            if c not in "/*-+":
                temp.append(c)
            else:
                if c == "*":
                    temp[-2] = int(int(temp[-2]) * int(temp[-1]))
                    temp.pop()
                elif c == "/":
                    temp[-2] = int(float(temp[-2]) / float(temp[-1]))
                    temp.pop()
                elif c == "+":
                    temp[-2] = int(temp[-2]) + int(temp[-1])
                    temp.pop()
                elif c == "-":
                    temp[-2] = int(temp[-2]) - int(temp[-1])
                    temp.pop()
        return int(temp[-1])