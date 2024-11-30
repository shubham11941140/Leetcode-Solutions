class Solution:

    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        for v in arr:
            if counter[v] == 1:
                k -= 1
                if not k:
                    return v
        return ""  # Not enough distinct strings
