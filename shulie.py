#数列的第一项为n，以后各项为前一项的平方根，求数列的前m项的和。
#数列的第一项为n，以后各项为前一项的平方根，求数列的前m项的和。
#81 4  94.73
#2 2   3.41
import math
n,m=map(int,input().split())
sum=n
for i in range(m-1):
    n=math.sqrt(n)
    sum=sum+n
print('{:.2f}'.format(sum))