class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace("-", "").replace(" ", "")
        res = []
        while len(number) > 4:
            res.append(number[:3])
            number = number[3:]
        if len(number) == 4:
            res.append(number[:2])
            res.append(number[2:])
        else:
            res.append(number)
        return '-'.join(res)          