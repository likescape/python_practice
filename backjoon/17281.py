#https://www.acmicpc.net/problem/17281
N = int(input())

player_list =[] 
for i in list(map(int, input().split())):
  player_list.append([i])
for i in range(N-1):
  player_list[i].append()