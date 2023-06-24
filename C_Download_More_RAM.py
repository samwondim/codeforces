from collections import defaultdict

def ans() -> int:
    nk = input().split(' ')

    n, k = int(nk[0]), int(nk[1])
    
    a = input().split(' ')
    b = input().split(' ')
    map = defaultdict(int)

    for i in range(n):
        a[i] = int(a[i])
        b[i] = int(b[i])

        count = map[a[i]]
        map[a[i]] = b[i] + count
    
    new_map = dict(sorted(map.items()))

    for key in new_map.keys():
        if key <= k:
            k += new_map[key]
    return k
    

n = int(input())
for i in range(n):
    print(ans())