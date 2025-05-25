import sys
input = sys.stdin.read
INF = float('inf')

def tsp(n, W):
    dp = [[INF] * n for _ in range(1 << n)]

    def dfs(visited, current):
        if visited == (1 << n) - 1:
            return W[current][0] if W[current][0] > 0 else INF
        if dp[visited][current] != INF:
            return dp[visited][current]
        for next in range(n):
            if not visited & (1 << next) and W[current][next] > 0:
                dp[visited][current] = min(
                    dp[visited][current],
                    dfs(visited | (1 << next), next) + W[current][next]
                )
        return dp[visited][current]

    return dfs(1, 0)

# 입력 처리
data = input().split()
n = int(data[0])
W = [list(map(int, data[i*n+1:(i+1)*n+1])) for i in range(n)]

# 결과 출력
print(tsp(n, W))
