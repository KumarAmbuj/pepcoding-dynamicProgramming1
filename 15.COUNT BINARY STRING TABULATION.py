def countbinarystring(n):
    zeros=[0 for i in range(n+1)]
    ones=[0 for i in range(n+1)]

    zeros[1]=1
    ones[1]=1

    for i in range(2,len(zeros)):
        zeros[i]=ones[i-1]
        ones[i]=zeros[i-1]+ones[i-1]

    ans=zeros[n]+ones[n]
    print(ans)

countbinarystring(6)
