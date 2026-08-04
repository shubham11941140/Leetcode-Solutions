class Solution:

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        return [
            *map(
                lambda d: max(d.values()) - d[-1] + 1,
                accumulate(
                    reversed(range(len(nums))),
                    lambda d, i: d
                    | {q: i
                       for q in range(32) if nums[i] & 1 << q}
                    | {-1: i},
                    initial={-1: 0},
                ),
            )
        ][:0:-1]
