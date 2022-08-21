class Solution:

    def __init__(self):
        self.a = [
            1,
            4,
            9,
            121,
            484,
            10201,
            12321,
            14641,
            40804,
            44944,
            1002001,
            1234321,
            4008004,
            100020001,
            102030201,
            104060401,
            121242121,
            123454321,
            125686521,
            400080004,
            404090404,
            10000200001,
            10221412201,
            12102420121,
            12345654321,
            40000800004,
            1000002000001,
            1002003002001,
            1004006004001,
            1020304030201,
            1022325232201,
            1024348434201,
            1210024200121,
            1212225222121,
            1214428244121,
            1232346432321,
            1234567654321,
            4000008000004,
            4004009004004,
            100000020000001,
            100220141022001,
            102012040210201,
            102234363432201,
            121000242000121,
            121242363242121,
            123212464212321,
            123456787654321,
            400000080000004,
            10000000200000001,
            10002000300020001,
            10004000600040001,
            10020210401202001,
            10022212521222001,
            10024214841242001,
            10201020402010201,
            10203040504030201,
            10205060806050201,
            10221432623412201,
            10223454745432201,
            12100002420000121,
            12102202520220121,
            12104402820440121,
            12122232623222121,
            12124434743442121,
            12321024642012321,
            12323244744232321,
            12343456865434321,
            12345678987654321,
            40000000800000004,
            40004000900040004,
        ]

    def superpalindromesInRange(self, left: str, right: str) -> int:
        l = int(left)
        r = int(right)
        c = 0
        for i in self.a:
            if i > r:
                break
            if l <= i <= r:
                c += 1
        return c
