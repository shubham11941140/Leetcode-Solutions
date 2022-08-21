class Solution:

    def capitalizeTitle(self, title: str) -> str:
        a = title.split()
        ans = []
        for i in a:
            if len(i) < 3:
                ans.append(i.lower())
            else:
                ans.append(i[0].upper() + i[1:].lower())
        return " ".join(ans)
