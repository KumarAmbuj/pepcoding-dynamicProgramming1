def countbinarystring(n):
    zeros=1
    ones=1

    for i in range(2,n+1):
        nzeros=ones
        nones=zeros+ones

        ones=nones
        zeros=nzeros

    ans=zeros+ones
    print(ans)

countbinarystring(6)