class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        m = defaultdict(list)  # Dictionary to store indices of equal numbers
        
        # Store indices of each number in the dictionary
        for i, num in enumerate(nums):
            m[num].append(i)
        
        # Iterate over each group of equal numbers
        return sum([sum([1 for i in range(len(a)) for j in range(i + 1, len(a)) if (a[i] * a[j]) % k == 0]) for a in m.values()])    