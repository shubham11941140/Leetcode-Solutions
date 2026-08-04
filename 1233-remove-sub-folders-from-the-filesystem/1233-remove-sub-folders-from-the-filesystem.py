class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        result = []
        for f in sorted(folder):
            if not result or not f.startswith(result[-1] + "/"):
                result.append(f)
        return result
