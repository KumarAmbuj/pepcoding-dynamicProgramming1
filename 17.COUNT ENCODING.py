def findencoding(s):
    if s[0]=='0':
        print('not possible')
        return

    dp=[0 for i in range(len(s))]
    dp[0]=1

    for i in range(1,len(s)):
        if s[i-1]=='0' and s[i]=='0':
            dp[i]=0
        elif s[i-1]=='0' and s[i]!='0':
            dp[i]=dp[i-1]

        elif s[i-1]!='0' and s[i]=='0':
            if s[i-1]=='0' or s[i-1]=='1':
                dp[i]=dp[i-2] if i>=2 else 1
            else:
                dp[i]=0

        else:
            if int(s[i-1:i+1])<=26:
                dp[i]=dp[i-1]+(dp[i-2] if i>=2 else 1)
            else:
                dp[i]=dp[i-1]

    print(dp[len(s)-1])

s='231011'
findencoding(s)

s='0231011'
findencoding(s)

s='30'
findencoding(s)

