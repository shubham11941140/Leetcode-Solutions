class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = Counter(hand)
        hand.sort()
        for v in hand:
            if cnt[v] > 0:
                for x in range(v, v + groupSize):
                    if cnt[x] == 0:
                        return False
                    cnt[x] -= 1
        return True        