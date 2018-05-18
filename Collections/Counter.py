from collections import Counter

l = [1, 1, 1, 1, 1, 1, 223, 23, 23, 43, 54, 65, 67, 76, 6, 34, 43, 34, 43, 43, 43, 43, 43, 43, 43, 43, 43]

a = Counter(l)
print(a)

s = 'aasvddkfnldsnvsklnsvd;knsvd;nv;sdnsvd;ndsv;nsv;svnsvd;nsvd;nsvd;nsdv;nsvd'
a = Counter(s)
print(a)
