'''$$$
[Descriptoin]
Given N arrays, please find any two of the N whose sums are equal after you delete one element from each array.

[Tags]
hash, implementation

[Url]
https://codeforces.com/contest/988/problem/C

[Difficulty]
2
$$$'''

import sys
n = int(raw_input())

d = {}

for i in xrange(n):
    m = int(raw_input())
    ms = map(int, raw_input().split())
    s = sum(ms)
    dd = {}
    for j, item in enumerate(ms):
        u = s - item
        if u in d:
            print 'YES'
            print '%d %d' % d[u]
            print '%d %d' % (i + 1, j + 1)
            sys.exit(0)
        dd[u] = (i + 1, j + 1)
    d.update(dd)
print 'NO'
