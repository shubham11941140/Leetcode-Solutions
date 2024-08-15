class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar_count = 0
        ten_dollar_count = 0
        for bill in bills:
            if bill == 5:
                five_dollar_count += 1
            elif bill == 10:
                if five_dollar_count == 0:
                    return False
                five_dollar_count -= 1
                ten_dollar_count += 1
            else:  # bill == 20
                if ten_dollar_count > 0 and five_dollar_count > 0:
                    ten_dollar_count -= 1
                    five_dollar_count -= 1
                elif five_dollar_count >= 3:
                    five_dollar_count -= 3
                else:
                    return False
        return True        
        