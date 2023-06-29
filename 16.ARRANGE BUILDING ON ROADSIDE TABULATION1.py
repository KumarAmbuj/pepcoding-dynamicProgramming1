def arrangebuilding(n):
    building=1
    space=1

    for i in range(2,n+1):
        nbuilding=space
        nspace=building+space

        building=nbuilding
        space=nspace

    total=building+space
    ans=total*total
    print(ans)

arrangebuilding(4)