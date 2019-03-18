t1_num = int(input())-1
t1_header = list(map(str,input().split()))
t1_item = []
for _ in range(t1_num):
    t1_item.append(input().split())
t1_item.sort(key=lambda x: x[0], reverse=False)

t2_num = int(input()) -1
t2_header = list(map(str,input().split()))
t2_item = []

header = t1_header + t2_header[1:]
for _ in range(t2_num):
    t2_item.append(input().split())
t2_len = len(t2_header)-1
for x in t1_item:
    flag = 1
    for y in t2_item:
        if x[0] == y[0]:
            x += y[1:]
            flag = 0
            break
    if flag:
        for k in range(t2_len):
            x.append("NULL")

print(*header)
for x in t1_item:
    print(*x)