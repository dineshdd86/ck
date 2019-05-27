l=list(map(int,input().split()))
ak=l[0]
bk=l[1]
ck=l[2]
if ak>=bk and ak>=ck:
    print(ak)
elif bk>=ak and bk>=ck:
    print(bk)
else:
    print(ck)
