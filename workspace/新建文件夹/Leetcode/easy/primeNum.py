class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # num = 0
        
        # for i in range(2,n+1):
        #     if self.isPrime(i):
        #         num+=1
        if n <= 2:
            return 0
        
        prime = [True] * n
        prime[:2] = [False, False]
        for base in range(2, int((n - 1) ** 0.5) + 1):
            if prime[base]:
                prime[base ** 2::base] = [False] * len(prime[base ** 2::base])
        return sum(prime)  
    
s= Solution()

print (s.countPrimes(100))