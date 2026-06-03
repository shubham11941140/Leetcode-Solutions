class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def calculatemin(start1,dur1,start2,dur2):
            
            ans = min([(start1[r] + dur1[r]) for r in range(len(start1))])
            ansfinal = float("inf")

            for r1 in range(len(start2)):
                finish2=max(ans,start2[r1]) + dur2[r1]
                ansfinal=min(ansfinal,finish2)
            return ansfinal

        firstlandsecondwater = calculatemin(landStartTime,landDuration,waterStartTime,waterDuration)
        firstwatersecondland = calculatemin(waterStartTime,waterDuration,landStartTime,landDuration)

        return min(firstlandsecondwater,firstwatersecondland)        