L = int(input())
N = int(input())
cnt_pos = [int(i) for i in input().split()]
for i in range(len(cnt_pos)):
    cnt_pos.append(L-cnt_pos[i])
print(int(max(cnt_pos)))