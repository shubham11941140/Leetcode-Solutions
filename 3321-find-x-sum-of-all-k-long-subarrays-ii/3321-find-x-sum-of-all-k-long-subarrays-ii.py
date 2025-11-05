class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        numCount = defaultdict(int)
        top = SortedList(key=lambda p: (-p[0], -p[1]))      
        bottom = SortedList(key=lambda p: (-p[0], -p[1]))   
        result = []
        running_sum = 0

        for i, num in enumerate(nums):
            count = numCount[num]

            # Remove old count entry
            if count > 0:
                if (count, num) in top:
                    top.remove((count, num))
                    running_sum -= count * num
                else:
                    bottom.discard((count, num))

            count += 1
            numCount[num] = count
            top.add((count, num))
            running_sum += count * num

            if len(top) > x:
                smallest = top[-1]
                running_sum -= smallest[0] * smallest[1]
                bottom.add(smallest)
                top.remove(smallest)

            if i >= k:
                old_num = nums[i - k]
                old_count = numCount[old_num]
                if (old_count, old_num) in top:
                    running_sum -= old_count * old_num
                    top.remove((old_count, old_num))
                else:
                    bottom.discard((old_count, old_num))

                old_count -= 1
                numCount[old_num] = old_count
                if old_count > 0:
                    bottom.add((old_count, old_num))

                if len(top) < x and len(bottom) > 0:
                    best = bottom[0]
                    running_sum += best[0] * best[1]
                    top.add(best)
                    bottom.remove(best)

            if i + 1 >= k:
                result.append(running_sum)

        return result        