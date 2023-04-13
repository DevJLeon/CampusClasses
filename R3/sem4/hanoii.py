# m(n) = 2^n -1

def hanoii (p1,p2,p3,n):
    p1 = n
    pasos = 0
    while p3 != n:
        if p1 == n:
            p3 +=1