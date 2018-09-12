#现在有一棵合法的二叉树，树的节点都是用数字表示，现在给定这棵树上所有的父子关系，求这棵树的高度
#思路：用字典做数据结构，统计每个节点的所在层数和子节点数，返回最大层数
#'''

n = int(input())
tree = {'0':[1,0]}#节点‘0’的【层数，子节点数】
for i in range(n-1):#遍历所有节点,统计所有节点所在层数和子节点数
    father,son=input().split()#爹和儿子输入时是char类型
    if father in tree and tree[father][1]<2:#如果该节点已经存在（说明已经有一个子节点与之匹配了，但是没匹配完）
        tree[father][1]+=1 #这时该节点又出现一次，所以节点个数需要加1
        tree[son]=[tree[father][0]+1,0]#为子节点创建树状结构【层数=上一层层数+1，该新节点的子节点数】
 
#打印最大层数：
print("树的最大高度是：",max([i[0] for i in tree.values()]))#遍历tree.values()列表中的第一个值，即是最大层数，也是树的高度。