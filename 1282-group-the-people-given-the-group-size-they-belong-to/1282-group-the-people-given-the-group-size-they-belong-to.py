class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
        result = []
        for size, members in groups.items():
            result += [members[i:i + size] for i in range(0, len(members), size)]
                
        return result     