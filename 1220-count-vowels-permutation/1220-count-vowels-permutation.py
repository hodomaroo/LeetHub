class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[0] * 5 for _ in range(n + 1)]
        dp[1] = [1] * 5
        MOD = 10 ** 9 + 7
        
        for i in range(2,n + 1):
            dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][4]) % MOD #a는 e i u뒤에 올 수 있음
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD #e는 a i 뒤에 올 수 있음
            dp[i][2] = dp[i-1][3] + dp[i-1][1] #i는 e o 뒤에 올 수 있음
            dp[i][3] = dp[i-1][2] #o는 i뒤에 올 수 있음
            dp[i][4] = (dp[i-1][2] + dp[i-1][3]) % MOD #u는 i o뒤에 올 수 있음
        
        return sum(dp[n]) % MOD