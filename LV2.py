def reverse (x: int) -> int:
    m=0
    i=x<0
    while x!=0 :
        m*=10
        m+=x%10
        x//=10
    if i==1:
        m=-m
    return m
b=123
a=reverse(b)
print(a)