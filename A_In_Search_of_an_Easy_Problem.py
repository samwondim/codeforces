def ans()-> str:
    ppl = input().split(' ')
    arr = []
    
    for p in ppl:
        if p == '1':
            return 'HARD'
    return 'EASY'

n = int(input())
print(ans())