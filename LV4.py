def scholarship (end: int,classreview: int,leader: bool,west: bool,paper: bool )-> int :
    bonus=0
    if end >= 80 and paper == True:
        bonus+=8000
    if end >= 85 and classreview>=80:
        bonus+=4000
    if end >= 90:
        bonus+=2000
    if end >= 85 and west == True:
        bonus+=1000
    if end >= 80 and leader == True:
        bonus+=850
    return bonus
n=input()
m=n.split(" ")
k=5
m_len=len(m)
max_i=0
max_x=0
while k<m_len :
    x=scholarship(int(m[k-4]),int(m[k-3]),bool(m[k-2]),bool(m[k-1]),bool(m[k]))
    if x>max_x:
        max_x=x
        max_i=k-5
    k+=6
print(m[max_i], max_x)
