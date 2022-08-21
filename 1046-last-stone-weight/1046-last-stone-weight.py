class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            x = stones[-2]
            y = stones[-1]
            stones.pop()
            stones.pop()
            if x < y:
                stones.append(y - x)
        return stones[0] if len(stones) == 1 else 0
        
