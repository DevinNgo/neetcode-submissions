class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # I want to check the last element if int, add to sum array and pop
        stack = []

        for ops in operations:
            if ops == "+":
                stack.append(stack[-1] + stack[-2])
            elif ops == "D":
                stack.append(stack[-1]*2)
            elif ops == "C":
                stack.pop()
            else:
                stack.append(int(ops))

        return sum(stack)
            

            
