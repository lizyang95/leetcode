def bubbleSort(a):
    l=len(a)-2
    i=0
    while i<l:
        j=l
        while j>=i:
            if(a[j+1]<a[j]):
                a[j],a[j+1]=a[j+1],a[j]
            j-=1
        i+=1

def insertSort(arr):
    for i in range(1,len(arr)):
        '''''
        tmp=arr[i]
        j=i
        while j>0 and tmp<arr[j-1]:
            arr[j]=arr[j-1]
            j-=1
        arr[j]=tmp
        '''
        j=i
        while j>0 and arr[j-1]>arr[i]:
            j-=1
        arr.insert(j,arr[i])
        arr.pop(i+1)

def shellSort(arr):
    dist=len(arr)/2
    while dist>0:
        for i in range(dist,len(arr)):
            tmp=arr[i]
            j=i
            while j>=dist and tmp<arr[j-dist]:
                arr[j]=arr[j-dist]
                j-=dist
            arr[j]=tmp
        dist/=2


////////////////////////////////////////////////////////
'''
merge sort
'''
'''''
使用新分配的空间存储合并得到的新列表
arr：  原始列表（数组）
s：    需合并的第一段空间起始点
m：    需合并的第二段空间起始点
e：    需合并的第二段空间结束点
'''
def mergeWithNewSpace(arr,s,m,e):
    i,j=s,m
    t=0
    newArr=[]
    while i<m and j<=e:
        if(arr[i]<arr[j]):
            newArr.append(arr[i])
            i+=1
            t+=1
        else:
            newArr.append(arr[j])
            j+=1
            t+=1
    if i>=m:
        t=0
        for i in range(s,j):
            arr[i]=newArr[t]
            t+=1
    else:
        t=0
        for i in range(i,m):
            newArr.append(arr[i])
        for i in range(s,e+1):
            arr[i]=newArr[t]
            t+=1
    del newArr
def mergePassWithNewSpace(arr, n, d):
    i=0
    while i<(n-d) and i<(n+1-2*d):
        mergeWithNewSpace(arr,i,i+d,i+2*d-1)
        i=i+2*d
    if i<n-d:
        mergeWithNewSpace(arr,i,i+d,n-1)
    else:
        mergeWithNewSpace(arr,i-2*d,i,n-1)
def mergeSortWithNewSpace(arr):
    d=1
    while d<len(arr):
        mergePassWithNewSpace(arr,len(arr),d)
        d*=2
'''''
不分配新的空间存储合并得到的列表
而是使用原列表使用插入方式存储
arr：  原始列表（数组）
s：    需合并的第一段空间起始点
m：    需合并的第二段空间起始点
e：    需合并的第二段空间结束点
被注释掉的部分是c语言数组普通的插入方式
未被注释的部分则是使用python列表的插入和删除特性改善的
'''
def mergeWithoutNewSpace(arr,s,m,e):
    i,j=s,m
    while i<m and j<=e:
        if arr[i]>arr[j]:
            '''''
            tmp=arr[j]
            k=j
            while k>i:
                arr[k]=arr[k-1]
                k-=1
            arr[i]=tmp
            '''
            arr.insert(i,arr[j])
            arr.pop(j+1)
            j+=1
            m+=1
        else:
            i+=1
'''''
arr：  原始列表（数组）
n：    数组大小
d：    区间大小
'''
def mergePassWithoutNewSpace(arr, n, d):
    i=0
    while i<(n-d) and i<(n+1-2*d):
        mergeWithoutNewSpace(arr,i,i+d,i+2*d-1)
        i=i+2*d
    if i<n-d:
        mergeWithoutNewSpace(arr,i,i+d,n-1)
    else:
        mergeWithoutNewSpace(arr,i-2*d,i,n-1)
def mergeSortWithoutNewSpace(arr):
    d=1
    while d<len(arr):
        mergePassWithoutNewSpace(arr,len(arr),d)
        d*=2






///////////////////////////////////////
'''
quick sort
'''


def median(a,start,end):
    center=(start+end)/2
    if a[start]>a[center]:
        a[start],a[center]=a[center],a[start]
    if a[start]>a[end]:
        a[start],a[end]=a[end],a[start]
    if a[center]>a[end]:
        a[center],a[end]=a[end],a[center]
    a[start],a[center]=a[center],a[start]
def doSwap(a,start,end):
    if start>=end:
        return
    i,j=start,end
    median(a,start,end)
    tmp=a[start]
    while(True):
        while(a[j]>tmp and i<j):
            j-=1
        if i<j:
            a[i]=a[j]
            i+=1
        while(a[i]<tmp and i<j):
            i+=1
        if i<j:
            a[j]=a[i]
            j-=1
        else:
            break
    a[i]=tmp
    doSwap(a,start,i-1)
    doSwap(a,j+1,end)
def quickSort(a):
    #设置递归深度为10000000，放置数据量过大时超出递归最大深度发生exception
    sys.setrecursionlimit(1000000)
    doSwap(a,0,len(a)-1)
