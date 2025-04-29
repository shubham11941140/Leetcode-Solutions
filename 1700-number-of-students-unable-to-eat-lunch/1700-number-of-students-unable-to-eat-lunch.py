class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Index 0 for circular sandwiches, index 1 for square sandwiches
        preferences = [0, 0]
        for preference in students:
            preferences[preference] += 1
        for sandwich in sandwiches:
            if preferences[sandwich] == 0:
                return sum(preferences)
            preferences[sandwich] -= 1
        return 0
