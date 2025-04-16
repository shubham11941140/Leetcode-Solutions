class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = 0
        freq = defaultdict(int)  # To track occurrences of elements
        left = 0
        pair_count = 0
        
        # Sliding window approach
        for right in range(len(nums)):
            # Update frequency and pair count
            pair_count += freq[nums[right]]
            freq[nums[right]] += 1
            
            # Shrink the window if pair count exceeds k
            while pair_count >= k:
                pair_count -= (freq[nums[left]] - 1)
                freq[nums[left]] -= 1
                left += 1
            
            # Count valid subarrays ending at 'right'
            count += left
        
        return count    