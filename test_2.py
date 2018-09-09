#给定一个句子（只包含字母和空格）
# 将句子中的单词位置反转，单词用空格分割, 
# 单词之间只有一个空格，前后没有空格。 
# 比如： （1） “hello xiao mi”-> “mi xiao hello”
str_1=input().split()
def fn(tm):
    if len(tm)<1000:
        b=list(reversed(tm))
        c=" ".join([str(x) for x in b])
        return c
        #for i in b:
            #print(i)
    return ("cuwu")
print(fn(str_1))
#fn(str_1)