# https://www.acmicpc.net/problem/11726
# Recurrence
# An = A(n-1) + A(n-2)
# 점화식 세우고 코드 짜기
# 하나씩 그려보면서 규칙 찾기

import sys
input = sys.stdin.readline

N = int(input())

rs = [0, 1, 2]

for i in range(3, N+1):
    rs.append((rs[i-1] + rs[i-2])%10007)

print(rs[N])