class Solution:

    def binary_search(self, arr, low, high, x):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x)
            else:
                return self.binary_search(arr, mid + 1, high, x)        
        return -1        
        
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        cz = changed.count(0)
        if cz % 2:
            return []
        ans = [0 for i in range(cz // 2)]
        changed = [i for i in changed if i]
        even = sorted([i for i in changed if i % 2 == 0])
        odd = [i for i in changed if i % 2]
        for i in odd:
            bs = self.binary_search(even, 0, len(even) - 1, 2 * i)
            if bs != -1:
                ans.append(i)
                del even[bs]
            else:
                return []
        if len(ans) < len(odd):
            return []
        else:
            if len(even) % 2:
                return []
            else:
                while even:
                    m = even[0]
                    bs = self.binary_search(even, 0, len(even) - 1, 2 * m)
                    if bs != -1:
                        ans.append(m)
                        del even[bs]
                        del even[0]
                    else:
                        return []
        return ans
            
                