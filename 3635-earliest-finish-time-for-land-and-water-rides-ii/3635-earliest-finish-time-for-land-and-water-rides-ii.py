class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def calc(start1, dur1, start2, dur2):            
            ans = min([(start1[r] + dur1[r]) for r in range(len(start1))])
            return min([(max(ans, start2[r1]) + dur2[r1]) for r1 in range(len(start2))])

        f1 = calc(landStartTime, landDuration, waterStartTime, waterDuration)
        f2 = calc(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(f1, f2)