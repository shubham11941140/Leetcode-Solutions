class Solution:

    def binary_search(self, arr, low, high, x):

        # Check base case
        if high >= low:

            mid = (high + low) // 2

            # If element is present at the middle itself
            if arr[mid] == x:
                return mid

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x)

            # Else the element can only be present in right subarray
            else:
                return self.binary_search(arr, mid + 1, high, x)

        else:
            # Element is not present in the array
            return -1

    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # Remove all zeros before
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
                # even.remove(2 * i)
            else:
                return []
        if len(ans) < len(odd):
            return []
        else:  # Equal
            if len(even) % 2:
                return []
            else:
                # Check if split exists
                while even:
                    # Remove smallest
                    # m = min(even)
                    m = even[0]
                    bs = self.binary_search(even, 0, len(even) - 1, 2 * m)
                    if bs != -1:
                        ans.append(m)
                        del even[bs]
                        del even[0]
                        # even.remove(m)
                        # even.remove(2 * m)
                    else:
                        return []
        print(ans)
        return ans
