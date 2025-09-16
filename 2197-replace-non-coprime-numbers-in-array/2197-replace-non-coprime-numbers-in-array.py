class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            while stack and math.gcd(stack[-1], num) > 1:
                top = stack.pop()
                num = (top * num) // gcd(top, num)
            stack.append(num)
        return stack        