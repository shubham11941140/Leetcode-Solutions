class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}  # Dictionary to store groups

        for i, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = []  # Create an empty group for this size

            groups[size].append(i)  # Add person to the corresponding group

        result = []

        for size, members in groups.items():
            for i in range(0, len(members), size):
                result.append(members[i:i+size])

        return result     