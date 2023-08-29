class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        Y = customers.count('Y')
        min_p, hour, y_found, n_found = n, n, 0, 0
        for h in range(n + 1):
            y_remaining = Y - y_found
            pen = y_remaining + n_found
            if pen < min_p:
                hour = h
                min_p = pen
            if h < n:
                n_found += int(customers[h] == 'N')
                y_found += int(customers[h] == 'Y')
        return hour       