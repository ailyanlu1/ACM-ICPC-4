# Codeforces Round #165 (Div. 2) 解题报告

## A. Fancy Fence

SB题
可以算出，一个正n边形的内角和为(n*180)-360 (n>=3)
所以，判断``360 % (180-x) == 0``就OK

```Python
n = int(raw_input())
for i in xrange(n):
    x = int(raw_input())
    print 'YES' if 360 % (180-x) == 0 else 'NO'
```

## B. Multithreading

SB题
找出包含数列最后一个值的最长*连续*上升序列

```Python
n = int(raw_input())
nums = map(int,raw_input().split())[::-1]

idx = 0
pre = n + 1
for num in nums:
    if num < pre:
        idx += 1
        pre = num
    else:
        break
print n-idx
```

## C. Magical Boxes

因为看错题把自己坑成SB了。。。
其实很简单的，坑点是*要用一个新的箱子把所有现有的箱子包起来*

```Python
n = int(raw_input())
boxes = []

for i in xrange(n):
    a,b = map(int,raw_input().split())
    boxes.append({'sz': a, 'num': b})

boxes = sorted(boxes, key = lambda x : x['sz'])

sz, num = -1, -1

for i,item in enumerate(boxes):
    if sz == -1:
        sz, num = item['sz'], item['num']
    else:
        for i in xrange(item['sz']-sz):
            num = num / 4 + (1 if num % 4 != 0 else 0)
            if num == 1:
                break
        sz = item['sz']
        num = max(num, item['num'])

while num > 4:
    num = num / 4 + (1 if num % 4 != 0 else 0)
    sz += 1

print sz + 1
```

## D. Greenhouse Effect

不是很难的题目，因为C题没做出来就放弃了。。。= =。。。（_尼妹的！！！_

一个简单的LIS（不是*Lisa*哦~
找出一个最长不下降子序列，然后其余的点都插到子序列的中间

于是结果就是总点数n减去len(LIS)

```Python
def upper_bound(nums, x):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l + r + 1) >> 1
        if nums[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return l

if __name__ == "__main__":
    n, t = map(int,raw_input().split())
    dp = []
    for i in xrange(n):
        instr = raw_input().split()
        x = int(instr[0])
        if not dp:
            dp.append(x)
        else:
            if x >= dp[-1]:
                dp.append(x)
            else:
                dp[upper_bound(dp, x)] = x

    print n - len(dp)
```

## E. Flawed Flow

Div.2里面最难的一题了，基本没思路。
看过别人的代码才理解。

解法如下：
已知1是源点，n是汇点

对每一条边(a,b,c)，我们都设a,b两点都流出c的流量
然后从源点1开始进行BFS，维护流量数组
如果一个点的流入和流出的流量相同，则该点的流入流出关系已明确

我们搜索所有的点，就可以确定所有点的流量关系


```CPP
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <iostream>

using namespace std;

#define print(x) cout<<x<<endl
#define input(x) cin>>x
#define SIZE 200100

int n,m;
int flow[SIZE][2];
int start[SIZE];
int source[SIZE];

char vis[SIZE];
queue <int> q;

struct node
{
	int dest,cap,nr;
	int next;
	
	node(){}
	node(int idest,int icap,int inr,int inext)
	{
		dest=idest; cap=icap; nr=inr; next=inext;
	}
};

node edge[SIZE<<1];
int ind,head[SIZE];

inline void init()
{
	ind=0;
	memset(head,-1,sizeof(head));
}

inline void addedge(int a,int b,int f,int nr)
{
	edge[ind]=node(b,f,nr,head[a]);
	head[a]=ind++;
}

int main()
{
	int a,b,c;
	scanf("%d%d",&n,&m);
	
	init();
	
	for(int i=1;i<=m;i++)
	{
		scanf("%d%d%d",&a,&b,&c);
		start[i]=a;
		addedge(a,b,c,i); addedge(b,a,c,i);  
		flow[a][0]+=c; flow[b][0]+=c;
	}
	q.push(1); 
	vis[1]=1;
	while(!q.empty())
	{
		int now=q.front(); 
		q.pop();
		for(int i=head[now];i!=-1;i=edge[i].next)
		{
			int next=edge[i].dest;
			int cap=edge[i].cap;
			int nr=edge[i].nr;
			
			if(vis[next]) continue;
			source[nr]=now;
			
			flow[next][1]+=cap;
			flow[next][0]-=cap;
			
			if(next!=n && flow[next][1]==flow[next][0])
			{
				vis[next]=1;
				q.push(next);
			}
		}
	}
	for(int i=1;i<=m;i++)
	{
		if(source[i]==start[i]) printf("0\n");
		else printf("1\n");
	}
	return 0;
}
```
