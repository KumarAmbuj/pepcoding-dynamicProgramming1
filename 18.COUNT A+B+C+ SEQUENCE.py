def findcount(s):
    a=0
    ab=0
    abc=0

    for i in range(len(s)):
        if s[i]=='a':
            a=2*a+1
        elif s[i]=='b':
            ab=2*ab+a
        elif s[i]=='c':
            abc=2*abc+ab
    print(abc)

s='abcabc'
findcount(s)