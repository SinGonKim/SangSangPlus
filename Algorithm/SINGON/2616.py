import sys
input = sys.stdin.readline
def solution(n,p,c):
    s = [0]
    value = 0
    for t in p:
        value += t
        s.append(value)
    dp = [[0]*(n+1) for _ in range(4)]
    # 점화식을 활용해 최댓값 탐색
    for x in range(1,4):
        for m in range(x*c, n+1):
            if x ==1:
                dp[x][m] = max(dp[x][m-1], s[m]-s[m-c])
            else:
                dp[x][m] = max(dp[x][m-1], dp[x-1][m-c]+s[m]-s[m-c])
    return dp[3][n]
            
if __name__=="__main__":
    n = int(input()) #열차칸 개수
    p = list(map(int, input().split())) #각 칸 최대 인원수
    c = int(input()) #최대 연결개수
    print(solution(n,p,c))
