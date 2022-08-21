class Solution:

    def isint(self, s):
        try:
            val = int(s)
            return True
        except:
            return False

    def isdec(self, s):

        if s in [".", "+.", "-."] or "." not in s or s.count(".") > 1:
            return False
        idx = s.index(".")
        if not s[idx + 1:]:
            s += "1"
        if not s[:idx]:
            s = "1" + s
        print(s)
        try:
            idx = s.index(".")
            print(s[:idx])
            valb = self.isint(s[:idx] + "1")
            print(valb)
            vala = self.isint(s[idx + 1:]) or self.checke(s[idx + 1:])
            print(vala)
            c = s[idx + 1:]
            if c[0] in ["+", "-"]:
                return False
            if valb and vala:
                return True
            return False
        except:
            return False

    def checke(self, s):
        if "e" not in s or s in ["e", "e.", ".e"] or s.count("e") > 1:
            return False
        idx = s.index("e")
        try:
            valb = int(s[:idx])
            vala = int(s[idx + 1:])
            return True
        except:
            return False

    def base(self, s):
        if s.count(".") > 1 or s.count("e") > 1:
            return False
        return True

    def cf(self, s):
        try:
            float(s)
            return True
        except:
            return False

    def isNumber(self, s: str) -> bool:

        # return self.cf(s)
        t = list(s)
        print(t)
        for i in t:
            if i not in ["+", "-", "e", ".", "E"
                         ] + [str(k) for k in list(range(10))]:
                return False
        return self.cf(s)

        for i in ["+-", "--", "++", "--", "+.", "-.", "e."]:
            if i in s:
                return False

        if s[-1] in ["+", "-"]:
            return False

        print(self.base(s))
        if not self.base(s):
            return False
        if ".e" in s and s[-1] != "e" and s.index(".") > 0:
            return True
        return (self.isint(s) or self.isdec(s) or self.checke(s)
                or (self.isdec(s) and self.checke(s)))
