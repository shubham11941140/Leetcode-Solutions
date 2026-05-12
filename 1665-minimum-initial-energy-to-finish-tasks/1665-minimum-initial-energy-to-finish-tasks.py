class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:        
        current_energy = 0
        total_needed = 0        
        for actual, minimum in sorted(tasks, key = lambda x: x[1] - x[0], reverse=True):
            if current_energy < minimum:
                total_needed += (minimum - current_energy)
                current_energy = minimum
            current_energy -= actual            
        return total_needed                