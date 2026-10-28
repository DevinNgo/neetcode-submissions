class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0

        for ops in operations:
            if ops == "+":
                sum += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif ops == "D":
                sum += (stack[-1] * 2)
                stack.append(stack[-1] * 2)
            elif ops == "C":
                sum -= stack.pop()
            else:
                sum += int(ops)
                stack.append(int(ops))

        return sum
            

            
