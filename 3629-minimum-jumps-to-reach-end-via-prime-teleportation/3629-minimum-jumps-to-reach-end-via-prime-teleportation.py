class Solution:
    def minJumps(self, nums: List[int]) -> int:
        st = {i for i in nums}
        imap = defaultdict(list)
        for i in range(len(nums)):
            imap[nums[i]].append(i)
        to = defaultdict(list) 
        primes = set() 
        def is_prime(x):
            if x == 1 or x == 0:
                return False
            for i in range(2, int(x**.5)+1):
                if x % i == 0:
                    return False
            return True           
        MAX = max(nums)
        for i in sorted(nums):
            if is_prime(i) and i not in primes:
                primes.add(i)
                j = i
                while j <= MAX:
                    if j in st:
                        to[i].extend(imap[j])
                    j += i      
        q = deque()
        q.append(0)
        best = [float('inf')] * len(nums)
        best[0] = 0
        while len(q):
            cur = q.popleft()
            if cur - 1 >= 0:
                if best[cur - 1] > best[cur] + 1:
                    best[cur - 1] = best[cur] + 1
                    q.append(cur - 1)
            if cur + 1 < len(nums):
                if best[cur + 1] > best[cur] + 1:
                    best[cur + 1] = best[cur] + 1
                    q.append(cur + 1)
            if nums[cur] in primes:
                for nei in to[nums[cur]]:
                    if nei != cur:
                        if best[nei] > best[cur] + 1:
                            best[nei] = best[cur] + 1
                            q.append(nei)
                to.pop(nums[cur])  
        return best[len(nums) - 1]                      
                        