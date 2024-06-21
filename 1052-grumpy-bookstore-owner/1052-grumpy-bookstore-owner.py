class Solution:

    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        # Calculate the initial sum of satisfied customers
        initial_satisfaction = sum(c * (1 - g) for c, g in zip(customers, grumpy))

        # Initialize variables for the sliding window
        max_extra_satisfaction = 0
        extra_satisfaction = 0
        left = 0

        # Iterate through the array
        for right in range(len(customers)):
            # Update extra_satisfaction for the current window
            extra_satisfaction += customers[right] * grumpy[right]

            # Shrink the window if it exceeds x
            if right - left >= minutes:
                extra_satisfaction -= customers[left] * grumpy[left]
                left += 1

            # Update max_extra_satisfaction
            max_extra_satisfaction = max(max_extra_satisfaction, extra_satisfaction)

        # Add the maximum extra satisfaction to the initial satisfaction
        return initial_satisfaction + max_extra_satisfaction
