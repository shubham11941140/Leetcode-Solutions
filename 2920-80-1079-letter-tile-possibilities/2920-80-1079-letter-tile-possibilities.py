class Solution:

    def numTilePossibilities(self, tiles: str) -> int:

        def backtrack(tiles, path, used, result):
            if path:
                result.add(path)
            for i in range(len(tiles)):
                if used[i]:
                    continue
                used[i] = True
                backtrack(tiles, path + tiles[i], used, result)
                used[i] = False

        result = set()
        backtrack(tiles, "", [False] * len(tiles), result)
        return len(result)
