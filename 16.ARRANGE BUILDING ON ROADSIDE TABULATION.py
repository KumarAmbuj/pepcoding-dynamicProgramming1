def arrangebuilding(n):
    building=[0 for i in range(n+1)]
    space=[0 for i in range(n+1)]

    building[1]=1
    space[1]=1

    for i in range(2,len(space)):
        building[i]=space[i-1]
        space[i]=building[i-1]+space[i-1]

    ans=building[n]+space[n]

    total=ans*ans

    print(total)

arrangebuilding(4)