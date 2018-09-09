#设有n个整数，将他们连接成一排，组成一个最大的多位整数
#如：n=3时，3个整数13,312,343，连接成最大的整数位34331213
#如：n=4，4个整数7,13,4,246连接成最大整数位7424613

#code为

n=int(input())
str=input().split()
max_s=''
def find(num):
    global max_s
    if len(num)<=0:
        return
    a=num[0]
    for b in num:
        if a+b<b+a:
            a=b
    max_s+=a
    num.remove(a)
    find(num)
    return max_s
print(find(str))



