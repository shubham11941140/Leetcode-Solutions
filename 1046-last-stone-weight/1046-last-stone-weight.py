class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x = stones[-2]
            y = stones[-1]
            if x == y:
                # Remove the last 2 entries
                stones.pop()
                stones.pop()
            elif x < y:
                stones.pop()
                stones.pop()
                stones.append(y - x)
            print(stones)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0
        