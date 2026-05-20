class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        prefix_common = []
        # Initialize sets to track elements in the prefix
        set_A = set()
        set_B = set()
        for i in range(len(A)):
            # Add current elements to sets
            set_A.add(A[i])
            set_B.add(B[i])
            prefix_common.append(len(set_A.intersection(set_B)))
        return prefix_common      