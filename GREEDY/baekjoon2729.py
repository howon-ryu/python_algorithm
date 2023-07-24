n = int(input())

for _ in range(n):
    m = int(input())
    a = m//25
    m = m-25*a
    b = m//10
    m = m - 10 * b
    c = m//5
    m = m - 5 * c
    d = m//1
    print(a,b,c,d)