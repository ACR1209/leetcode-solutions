class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i in range(n):
            # Pop all indices from the stack for which the current temperature is higher
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)

        return answer