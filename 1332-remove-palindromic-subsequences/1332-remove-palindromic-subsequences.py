class Solution:

    # Returns LCS X and Y
    def lcs_(self, X, Y):

        m = len(X)
        n = len(Y)

        L = [[0] * (n + 1)] * (m + 1)

        # Following steps build L[m+1][n+1]
        # in bottom up fashion. Note that
        # L[i][j] contains length of LCS of
        # X[0..i-1] and Y[0..j-1]
        for i in range(n + 1):

            for j in range(n + 1):

                if i == 0 or j == 0:
                    L[i][j] = 0
                elif X[i - 1] == Y[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])

        # Following code is used to print LCS
        index = L[m][n]

        # Create a string length index+1 and
        # fill it with \0
        lcs = ["\n "] * (index + 1)

        # Start from the right-most-bottom-most
        # corner and one by one store characters
        # in lcs[]
        i, j = m, n

        while i > 0 and j > 0:

            # If current character in X[] and Y
            # are same, then current character
            # is part of LCS
            if X[i - 1] == Y[j - 1]:

                # Put current character in result
                lcs[index - 1] = X[i - 1]
                i -= 1
                j -= 1

                # reduce values of i, j and index
                index -= 1

            # If not same, then find the larger of
            # two and go in the direction of larger
            # value
            elif L[i - 1][j] > L[i][j - 1]:
                i -= 1

            else:
                j -= 1

        ans = ""

        for x, item in enumerate(lcs):
            ans += item

        return ans

    def lps(self, string):

        # Find reverse of str
        rev = string[::-1]

        # Return LCS of str and its reverse
        print(string, rev)
        return self.lcs_(string, rev)

    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2
