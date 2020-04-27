import math


def add(x):
    global current_answer, cnt
    current_answer -= cnt[x]*cnt[x]*x
    cnt[x] += 1
    current_answer += cnt[x]*cnt[x]*x


def remove(x):
    global current_answer, cnt
    current_answer -= cnt[x]*cnt[x]*x
    cnt[x] -= 1
    current_answer += cnt[x]*cnt[x]*x


def comp(l1, l2):
    global block_size
    if (int(l1[0]/block_size) > int(l2[0]/block_size)) or (int(l1[0]/block_size) == int(l2[0]/block_size) and l1[1] > l2[1]):
        return l2, l1
    else:
        return l1, l2


def sorting(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            arr[j], arr[j+1] = comp(arr[j], arr[j+1])
    return arr


current_answer = 0

arr = list(map(int, input("Array is ").split()))

q = int(input("No of Queries : "))

queries = []
count=0
for i in range(q):
    queries.append(list(map(int, input().split())))
    queries[count].append(count)
    count+=1
cnt = [0 for i in range(max(arr)+1)]

block_size = int(math.sqrt(len(arr)))

print(queries)

answers=[0]*q

queries = sorting(queries)

mo_right=-1
mo_left=0

for qq in queries:

    left=qq[0]
    right=qq[1]

    while(mo_right < right):
        mo_right+=1
        add(arr[mo_right])

    while(mo_right > right):
        remove(arr[mo_right])
        mo_right-=1

    while(mo_left < left):
        remove(arr[mo_left])
        mo_left+=1

    while(mo_left > left):
        mo_left-=1
        add(arr[mo_left])

    answers[qq[2]]=current_answer

print(*answers)