class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        nge=[None]*len(temperatures)
        for i in reversed(range(len(temperatures))):
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
            nge[i]=stack[-1] - i if stack else 0
            stack.append(i)
        return nge