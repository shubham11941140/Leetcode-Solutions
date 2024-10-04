class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Sort the list of skills in ascending order
        skill.sort()        
        # Calculate the target skill sum for each team
        target = skill[0] + skill[-1]        
        # Initialize pointers and the total chemistry sum
        i, j = 0, len(skill) - 1
        total_chemistry = 0        
        while i < j:
            # If the sum of the current pair does not match the target, return -1
            if skill[i] + skill[j] != target:
                return -1
            # Add the product of the current pair to the total chemistry
            total_chemistry += skill[i] * skill[j]
            # Move the pointers inward
            i += 1
            j -= 1        
        return total_chemistry        