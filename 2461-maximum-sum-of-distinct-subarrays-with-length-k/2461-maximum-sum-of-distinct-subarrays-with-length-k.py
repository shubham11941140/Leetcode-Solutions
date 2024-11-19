class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        arr = nums
        if len(arr) < k:
            return 0

        max_sum = 0
        window_sum = 0
        element_count = {}

        for i in range(len(arr)):
            # Add the current element to the window
            if arr[i] in element_count:
                element_count[arr[i]] += 1
            else:
                element_count[arr[i]] = 1
            window_sum += arr[i]

            # If the window size exceeds k, remove the leftmost element
            if i >= k:
                left_elem = arr[i - k]
                window_sum -= left_elem
                if element_count[left_elem] == 1:
                    del element_count[left_elem]
                else:
                    element_count[left_elem] -= 1

            # Update max_sum if current window has k distinct elements
            if len(element_count) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum        