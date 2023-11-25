#-*- coding:utf-8 -*-
# MST: Minimum Spannig Tree
# Spanning Tree: 모든 노드가 연결된 트리
# MST 최소의 비용으로 모든 노드가 연결된 트리

# Kruskal or Prim
# Kruskal: 전체 간선 중 작은것 부터 연결
# Prim: 현재 연결된 트리에서 이어진 간선중 가장 작은것을 추가

# 핵심 heap code

# heap = [[0, 1]]

# while heap:
#     w, next_node = heapq.heappop(heap)
#     if chk[next_node] == False:
#         chk[next_node] = True
#         rs += w
#         for next_edge in edge[next_node]:
#             if chk[next_edge[1]] == False:
#                 heapq.heappush(heap, next_edge)

# https://www.acmicpc.net/problem/1197

# 최소스패닝 트리 기본문제 (외우기)
# 간선을 인접 리스트 형태로 저장
# 시작점 부터 힙에 넣기
# 힙이 빌때까지 다음의 작업을 반복
#   힙의 최소값 꺼내서, 해당 노드 방문 안했다면,
#     방문표시, 해당 비용 추가, 연결된 간선들 힙에 넣어 주기

# O(ElogE)

# Egde 리스트에 저장: O(E)
# Heap안 모든 Edge에 연결된 간선 확인: O(E+E)
# 모든 간선 힙에 삽입: O(ElogE)
# O(E + 2E + ElogE) = O(3E + ElogE) = O(E(3+logE)) = O(ElogE)

# (W, next_node)

# 간선 저장 되는 인접리스트 : (무게, 노드번호)
# 힙: (무게, 노드번호)
# 방문 여부: bool[]
# MST 결과값: int

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
edge = [[] for _ in range(V+1)]
chk = [False]*(V+1)
rs = 0
for i in range(E):
    a, b, c = map(int, input().split())
    edge[a].append([c, b])
    edge[b].append([c, a])
# print(edge)

heap = [[0, 1]]

while heap:
    w, each_node = heapq.heappop(heap)
    if chk[each_node] == False:
        chk[each_node] = True
        rs += w
        for next_edge in edge[each_node]:
            if chk[next_edge[1]] == False:
                heapq.heappush(heap, next_edge)

print(rs)

