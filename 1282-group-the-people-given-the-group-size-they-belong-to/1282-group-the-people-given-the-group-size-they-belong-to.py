class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)

        for i, size in enumerate(groupSizes):
            groups[size].append(i)

        result = []

        for size, members in groups.items():
            for i in range(0, len(members), size):
                result.append(members[i:i + size])
        return result     