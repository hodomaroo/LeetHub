#Play Baseball With Strange Rules
#There're several Rounds --> scores of fast affect future scores
from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        #string List Ops
        #Using Stack

        stack = []
        for s in ops:
            if s == "+":
                stack.append(stack[-1] + stack[-2])
            elif s == "C":
                stack.pop()
            elif s == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(s))
        return sum(stack)
        #print(sum(stack))


